from dataclasses import dataclass
from enum import Enum


class ApplicationAuthenticationMethodType(Enum):
    machineAddress = 1
    osUser = 2
    path = 3
    hashValue = 4
    certificateattr = 5

@dataclass
class ApplicationAuthenticationMethod:
    AppID: str
    AuthType: ApplicationAuthenticationMethodType
    AuthValue: str
    Comment: str
    IsFolder: str
    authId : int
    AllowInternalScripts: bool
    Subject: str
    Issuer: str
    SubjectAlternativeName: str