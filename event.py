from __future__ import annotations

from pydantic import BaseModel, Field


class Headers(BaseModel):
    Content_Length: str = Field(..., alias='Content-Length')
    Content_Type: str = Field(..., alias='Content-Type')
    Host: str
    User_Agent: str = Field(..., alias='User-Agent')
    Trouter_Timeout: str = Field(..., alias='Trouter-Timeout')
    X_Trouter_Delivery_Control: str = Field(..., alias='X-Trouter-Delivery-Control')
    X_Microsoft_Skype_Message_ID: str = Field(..., alias='X-Microsoft-Skype-Message-ID')
    MS_CV: str = Field(..., alias='MS-CV')
    trouter_request: str = Field(..., alias='trouter-request')
    Trouter_TimeoutMs: str = Field(..., alias='Trouter-TimeoutMs')


class MSTeamsEvent(BaseModel):
    id: int
    method: str
    url: str
    headers: Headers
    body: str
