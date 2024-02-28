from __future__ import annotations
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field

class MessageType(Enum):
    rich_text: str = "RichText/Html"
    thread_activity: str = "ThreadActivity/MemberConsumptionHorizonUpdate"

class Emotions(Enum):
    _1f440_eyes: str = "1f440_eyes"
    heart: str = "heart"
    laugh: str = "laugh"

class User(BaseModel):
    mri: str
    time: int
    value: str

class Emotion(BaseModel):
    key: str
    users: List[User]
    
class Properties(BaseModel):
    mentions: Optional[str] = None
    cards: Optional[str] = None
    importance: str
    subject: str
    title: Optional[str] = None
    links: Optional[str] = None
    files: Optional[str] = None
    language_stamp: Optional[str] = Field(default=None, alias='languageStamp')
    emotions: Optional[List[Emotion]] = None


class AnnotationsSummary(BaseModel):
    emotions: Emotions

class Resource(BaseModel):
    clientmessageid: Optional[str] = None
    content: str
    from_: str = Field(..., alias='from')
    imdisplayname: Optional[str] = None
    prioritizeimdisplayname: Optional[Any] = None
    id: Optional[str] = None
    messagetype: MessageType
    originalarrivaltime: str
    properties: Optional[Properties] = None
    sequence_id: Optional[int] = Field(default=None, alias='sequenceId')
    version: Optional[str] = None
    composetime: Optional[str] = None
    type: Optional[str] = None
    conversation_link: str = Field(..., alias='conversationLink')
    to: Optional[str] = None
    contenttype: Optional[str] = None
    annotationsSummary: Optional[AnnotationsSummary] = None
    threadtype: Optional[str] = None
    isactive: Optional[bool] = None


class EventMessage(BaseModel):
    time: str
    type: str
    resource_link: str = Field(default=None, alias='resourceLink')
    resource_type: str = Field(..., alias='resourceType')
    resource: Resource
    isactive: bool
