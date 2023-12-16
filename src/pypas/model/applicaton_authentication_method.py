"""ApplicationAuthenticationMethod model class."""
from dataclasses import dataclass
from enum import Enum


class ApplicationAuthenticationMethodType(Enum):
    """ApplicationAuthenticationMethodType enum.
    Describes the type of authentication method set for an application.
    """

    machineAddress = 1
    osUser = 2
    path = 3
    hashValue = 4
    certificateattr = 5


@dataclass
class ApplicationAuthenticationMethod:
    """ApplicationAuthenticationMethod model class."""

    AppID: str
    AuthType: ApplicationAuthenticationMethodType
    AuthValue: str
    Comment: str
    IsFolder: str
    authId: int
    AllowInternalScripts: bool
    Subject: str
    Issuer: str
    SubjectAlternativeName: str
