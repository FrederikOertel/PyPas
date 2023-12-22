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

    AIMApp = 1
    AppPrv = 2
    CPM = 3
    EVD = 4
    GUI = 5
    HTTPGW = 6
    NAPI = 7
    PACLI = 8
    PAPI = 9
    PIMSU = 10
    PIMSu = 11
    PSM = 12
    PSMP = 13
    PSMApp = 14
    PSMPApp = 15
    PTA = 16
    PVWA = 17
    PVWAApp = 18
    XAPI = 19
    WINCLIENT = 20


class UserVaultAuthorization(Enum):
    """The user permissions."""

    AddSafes = 1
    AuditUsers = 2
    AddUpdateUsers = 3
    ResetUsersPasswords = 4
    ActivateUsers = 5
    AddNetworkAreas = 6
    ManageDirectoryMapping = 7
    ManageServerFileCategories = 8
    BackupAllSafes = 9
    RestoreAllSafes = 10


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
    street: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
    title: str = None
    organization: str = None
    department: str = None
    profession: str = None


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
    enableUser: bool = None
    changePassOnNextLogon: bool = None
    expiryDate: int = None
    suspended: bool = None
    lastSuccessfulLoginDate: int = None
    authorizedInterfaces: List[UserInterface] = None
    authenticationMethod: List[UserAuthenticationMethod] = None
    passwordNeverExpires: bool = None
    distinguishedName: str = None
    description: str = None
    businessAddress: UserBusinessAddress = None
    internet: UserInternet = None
    phones: UserPhones = None
    personalDetails: UserPersonalDetails = None
    groupsMembership: List[UserGroupsMembership] = None
    userDN: str = None
