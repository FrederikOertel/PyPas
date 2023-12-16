from dataclasses import dataclass
from enum import Enum
from typing import List

from pypas.model.group import GroupType

class UserSource(Enum):
    CyberArk = 1
    LDAP = 2

class UserAuthenticationMethod(Enum):
    AuthTypePass  = 1
    AuthTypeRadius  = 2
    AuthTypeLDAP = 3

class UserInterface(Enum):
    PIMSU = 1
    PSM = 2
    PSMP    = 3
    PVWA   = 4
    WINCLIENT = 5
    PTA = 6
    PACLI    = 7
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
    workStreet: str
    workCity: str
    workState: str
    workZip: str
    workCountry: str

@dataclass
class UserInternet:
    homePage: str
    homeEmail: str
    businessEmail: str
    otherEmail: str

@dataclass
class UserPhones:
    homeNumber: str
    businessNumber: str
    cellularNumber: str
    faxNumber: str
    pagerNumber: str

@dataclass
class UserPersonalDetails:
    firstName: str
    middleName: str
    lastName: str
    street: str
    city:  str
    state: str
    zip: str
    country: str
    title: str
    organization: str
    department: str
    profession: str

@dataclass
class UserGroupsMembership:
    groupID: int
    groupName: str
    groupType: GroupType

@dataclass
class User:
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




