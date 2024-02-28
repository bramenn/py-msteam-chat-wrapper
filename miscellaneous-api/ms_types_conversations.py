from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

class Consumptionhorizon(BaseModel):
    id: str
    consumptionhorizon: str
    messageVisibilityTime: int


class ConversationMembers(BaseModel):
    id: str
    version: str
    consumptionhorizons: List[Consumptionhorizon]


class Properties(BaseModel):
    consumptionhorizon: Optional[str] = None
    isemptyconversation: str
    consumptionHorizonBookmark: Optional[str] = None
    addedBy: Optional[str] = None
    addedByTenantId: Optional[str] = None
    favorite: Optional[str] = None
    lastimreceivedtime: Optional[str] = None
    lastimportantimreceivedtime: Optional[str] = None
    quickReplyAugmentation: Optional[str] = None
    lasturgentimreceivedtime: Optional[str] = None
    alerts: Optional[str] = None
    collapsed: Optional[str] = None


class ThreadProperties(BaseModel):
    isCreator: bool
    gapDetectionEnabled: str
    lastjoinat: str
    lastSequenceId: Optional[str] = None
    threadType: str
    productThreadType: str
    rosterVersion: int
    version: str
    topic: Optional[str] = None
    topicThreadTopic: Optional[str] = None
    spaceId: Optional[str] = None
    groupId: Optional[str] = None
    uniquerosterthread: Optional[str] = None
    createdat: Optional[str] = None
    privacy: Optional[str] = None
    hidden: Optional[str] = None
    ongoingCallChatEnforcement: Optional[str] = None
    spaceThreadTopic: Optional[str] = None
    topics: Optional[str] = None
    sharepointSiteUrl: Optional[str] = None
    lastleaveat: Optional[str] = None
    spaceType: Optional[str] = None


class RelationshipState(BaseModel):
    inQuarantine: bool


class MemberProperties(BaseModel):
    role: str
    isReader: bool
    memberExpirationTime: int
    relationshipState: Optional[RelationshipState] = None
    isIdentityMasked: Optional[bool] = None


class LastMessage(BaseModel):
    sequenceId: Optional[int] = None
    conversationid: Optional[str] = None
    conversationLink: Optional[str] = None
    type: Optional[str] = None
    id: Optional[str] = None
    clientmessageid: Optional[str] = None
    version: Optional[str] = None
    messagetype: Optional[str] = None
    content: Optional[str] = None
    from_: Optional[str] = Field(None, alias='from')
    imdisplayname: Optional[str] = None
    composetime: Optional[str] = None
    originalarrivaltime: Optional[str] = None
    s2spartnername: Optional[str] = None


class Conversation(BaseModel):
    type: str
    version: int
    properties: Properties
    threadProperties: ThreadProperties
    memberProperties: MemberProperties
    lastMessage: LastMessage
    messages: str
    lastUpdatedMessageId: int
    lastUpdatedMessageVersion: int
    targetLink: str
    id: str


class Metadata(BaseModel):
    totalCount: int
    forwardLink: Optional[str] = None
    backwardLink: Optional[str] = None
    syncState: Optional[str] = None


class ResponseConversations(BaseModel):
    conversations: List[Conversation]
    metadata: Metadata = Field(None, alias='_metadata')
