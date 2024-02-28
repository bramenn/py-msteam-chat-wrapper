from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Properties(BaseModel):
    languageStamp: Optional[str] = ""


class Message(BaseModel):
    sequenceId: Optional[int] = None
    conversationid: str
    conversationLink: str
    contenttype: str
    type: str
    amsreferences: Optional[List] = []
    id: str
    clientmessageid: str
    version: str
    messagetype: str
    content: str
    from_: str = Field(..., alias='from')
    imdisplayname: str
    prioritizeImDisplayName: Optional[bool] = False
    composetime: str
    originalarrivaltime: str
    properties: Properties


class _Metadata(BaseModel):
    lastCompleteSegmentStartTime: int
    lastCompleteSegmentEndTime: int
    backwardLink: str
    syncState: str


class ResponseMessages(BaseModel):
    messages: List[Message]
    tenantId: str
    _metadata: _Metadata
