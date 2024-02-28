from typing import Dict
from aiohttp import ClientSession, ClientResponse
import asyncio
import uuid

from ms_types_conversations import ResponseConversations, ConversationMembers
from ms_types_messages import ResponseMessages
from ms_types_users import UserResponse

class MSClient:
    skypetoken: str
    msteams_token: str
    messages_base_path: str = "https://emea.ng.msg.teams.microsoft.com"
    # messages_base_path: str = "https://amer.ng.msg.teams.microsoft.com.mcas.ms"
    teams_base_path: str = "https://teams.microsoft.com"
    my_msteams_id = "PUT_HERE_YOUR_ID"
    my_conversation_notes = "48:notes"
    m_cas_ctx = ""
    report_my_activity_path = "https://presence.teams.microsoft.com.mcas.ms/v1/me/reportmyactivity"

    def __init__(self, skypetoken: str, msteams_token: str) -> None:
        self.skypetoken = skypetoken
        self.msteams_token = msteams_token
        self.http_client = ClientSession(headers=self.default_headers)

    @property
    def default_headers(self):
        return {
            "authentication": f"skypetoken={self.skypetoken}",
            "authorization": f"Bearer " + self.msteams_token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

    async def get(self, endpoint: str, params: Dict = {}) -> ClientResponse:
        return await self.http_client.get(url=endpoint, params=params)

    async def post(self, endpoint: str, json: Dict, params: Dict = {}):
        return await self.http_client.post(url=endpoint, json=json, params=params)

    async def get_my_conversations(self, sync_state: str = "") -> ResponseConversations:

        if sync_state:
            params = {"syncState": sync_state}
        else:
            params = {}

        response = await self.get(
            endpoint=f"{self.messages_base_path}/v1/users/ME/conversations", params=params
        )

        if response.status == 401:
            print("Authentication error at: ", self.messages_base_path)
            return
        if response.status != 200:
            return

        return ResponseConversations(**await response.json())

    async def get_messages_by_conversation(self, conversation_id: str, page_size: int = 10):
        query_params = {"pageSize": page_size}
        response = await self.get(
            endpoint=f"{self.messages_base_path}/v1/users/ME/conversations/{conversation_id}/messages",
            params=query_params,
        )
        if response.status == 401:
            print("Authentication error at: ", self.messages_base_path)
            return
        if response.status != 200:
            return
        return ResponseMessages(**await response.json())

    async def get_user_info(self, msteams_user_id: str):
        response = await self.get(
            endpoint=f"{self.teams_base_path}/api/mt/emea/beta/users/{msteams_user_id}"
        )

        if response.status == 401:
            print("Authentication error at: ", self.teams_base_path)
            return
        if response.status != 200:
            return

        return UserResponse(**await response.json())

    async def get_owner_conversation(self, msteams_conversation_id: str) -> str:

        url = f"{self.teams_base_path}/api/chatsvc/amer/v1/threads/{msteams_conversation_id}/consumptionhorizons"
        response = await self.get(endpoint=url)
        if response.status == 401:
            print("Authentication error at: ", self.teams_base_path)
            return
        if response.status != 200:
            print(
                "Error at: ",
                url,
                response.status,
                await response.text(),
            )
            return
        conversation_members = ConversationMembers(**await response.json())

        for member in conversation_members.consumptionhorizons:
            if member.id != self.my_msteams_id:
                return member.id

    async def send_message(self, conversation_id: str, message: str):
        params = {"McasCtx": self.m_cas_ctx}

        # Need to generate a message id each time a message is to be sent
        new_uuid = uuid.uuid4()
        integer_number = int(new_uuid)
        uuid_message = integer_number % (10**19)

        json = {
            "content": f"<p>{message}</p>",
            "messagetype": "RichText/Html",
            "contenttype": "text",
            "amsreferences": [],
            "clientmessageid": uuid_message,
            "imdisplayname": "I am the FBI",
            "properties": {"importance": "", "subject": ""},
        }
        return await self.post(
            endpoint=f"{self.messages_base_path}/v1/users/ME/conversations/{conversation_id}/messages",
            params=params,
            json=json,
        )

    async def report_my_activity(self):

        params = {
            "McasUserAuth": "TODO"
        }
        response = await self.post(
            endpoint=self.report_my_activity_path,
            params=params,
            json={"endpointId": "TODO", "isActive": "true"},
        )

        print(response.status, await response.text())
        if response.status == 401:
            print("Authentication error at: ", self.teams_base_path)
            return
        if response.status != 200:
            return

    async def report_my_activity_constantly(self):
        while True:
            print("Reporting activity")
            await self.report_my_activity()
            await asyncio.sleep(180)
            print("Activity reported")
