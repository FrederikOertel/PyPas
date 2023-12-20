from dataclasses import dataclass


@dataclass
class Credential:
    Content: str
    UserName: str
    Address: str
    Database: str
    PasswordChangeInProcess: bool
