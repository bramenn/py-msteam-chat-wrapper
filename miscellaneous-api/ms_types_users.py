from __future__ import annotations

from typing import List

from pydantic import BaseModel


class SkypeTeamsInfo(BaseModel):
    isSkypeTeamsUser: bool


class FeatureSettings(BaseModel):
    isPrivateChatEnabled: bool
    enableShiftPresence: bool
    coExistenceMode: str
    enableScheduleOwnerPermissions: bool


class Phone(BaseModel):
    type: str
    number: str


class Value(BaseModel):
    physicalDeliveryOfficeName: str
    userLocation: str
    accountEnabled: bool
    alias: str
    mail: str
    objectType: str
    telephoneNumber: str
    skypeTeamsInfo: SkypeTeamsInfo
    featureSettings: FeatureSettings
    sipProxyAddress: str
    smtpAddresses: List[str]
    isSipDisabled: bool
    isShortProfile: bool
    phones: List[Phone]
    responseSourceInformation: str
    companyName: str
    userPrincipalName: str
    givenName: str
    surname: str
    jobTitle: str
    department: str
    email: str
    userType: str
    tenantName: str
    displayName: str
    type: str
    mri: str
    objectId: str


class UserResponse(BaseModel):
    value: Value
    type: str
