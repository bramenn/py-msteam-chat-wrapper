

from json import loads
from typing import Dict
from event import MSTeamsEvent
from message import EventMessage, MessageType

class Handler:


    def try_covert_to_json(self, body: str) -> Dict:
        try:
            return loads(body)
        except Exception as _:
            print("The body didn't can json searialize")
            return
        

    def general_handler(self, event: Dict):
        mstems_event = MSTeamsEvent(**event)
        message_json = self.try_covert_to_json(mstems_event.body)


        if message_json.get("resourceType") not in ["NewMessage", "MessageUpdate"]:    
            return
        
        print(message_json)
        try:
            message = EventMessage(**message_json)
        except Exception as e:
            print(f"Error: {e}")

        if message.resource.messagetype == MessageType.rich_text:
            self.teams_message_handler(message)



    def teams_message_handler(self, teams_message_event: EventMessage):
        print(teams_message_event.resource.to)
        print(teams_message_event.resource.imdisplayname)
        print(teams_message_event.resource.content, "\n\n")