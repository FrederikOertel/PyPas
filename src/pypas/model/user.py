"""User model."""
from dataclasses import dataclass
from enum import Enum
from typing import List

from pypas.model.group import GroupType


class UserSource(Enum):
    """Describes the source of a user."""

    CyberArk = 1
    LDAP = 2


class UserAuthenticationMethod(Enum):
    """Describes the authentication method available for a user."""

    AuthTypePass = 1
    AuthTypeRadius = 2
    AuthTypeLDAP = 3


class UserInterface(Enum):
    """Describes possible interfaces for a user."""

    PIMSU = 1
    PSM = 2
    PSMP = 3
    PVWA = 4
    WINCLIENT = 5
    PTA = 6
    PACLI = 7
    HTTPGW = 8
    EVD = 9
    PIMSu = 10
    AIMApp = 11
    CPM = 12
    PVWAApp = 13
    PSMApp = 14
    AppPrv = 15
    PSMPApp = 17


@dataclass
class UserBusinessAddress:
    """Describes the business address of a user."""

    workStreet: str
    workCity: str
    workState: str
    workZip: str
    workCountry: str


@dataclass
class UserInternet:
    """Describes the internet presence of a user."""

    homePage: str
    homeEmail: str
    businessEmail: str
    otherEmail: str


@dataclass
class UserPhones:
    """Describes the phone numbers of a user."""

    homeNumber: str
    businessNumber: str
    cellularNumber: str
    faxNumber: str
    pagerNumber: str


@dataclass
class UserPersonalDetails:
    """Describes the personal details of a user."""

    firstName: str
    middleName: str
    lastName: str
    street: str
    city: str
    state: str
    zip: str
    country: str
    title: str
    organization: str
    department: str
    profession: str


@dataclass
class UserGroupsMembership:
    """Describes a group the user is a member of."""

    groupID: int
    groupName: str
    groupType: GroupType


@dataclass
class User:
    """Describes a user with their properties."""

    id: str
    username: str
    source: UserSource
    userType: str
    componentUser: bool
    vaultAuthorization: List[str]
    location: str
    enableUser: bool
    changePassOnNextLogon: bool
    expiryDate: int
    suspended: bool
    lastSuccessfulLoginDate: int
    unAuthorizedInterfaces: List[UserInterface]
    authenticationMethod: List[UserAuthenticationMethod]
    passwordNeverExpires: bool
    distinguishedName: str
    description: str
    businessAddress: UserBusinessAddress
    internet: UserInternet
    phones: UserPhones
    personalDetails: UserPersonalDetails
    groupsMembership: List[UserGroupsMembership]
