from dataclasses import dataclass



@dataclass
class Application:
    AccessPermittedFrom: str
    AccessPermittedTo: str
    AllowExtendedAuthenticationRestrictions: bool
    AppID: str
    BusinessOwnerEmail: str
    BusinessOwnerFName: str
    BusinessOwnerLName: str
    BusinessOwnerPhone: str
    Description: str
    Disabled: bool
    ExpirationDate: str
    Location: str