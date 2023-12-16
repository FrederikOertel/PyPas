from dataclasses import dataclass

@dataclass
class SafeCreator:
    id: str
    name: str


@dataclass
class Safe:
    """Returned object from the Get Safe Details Endpoint
    """
    safeUrlId: str
    safeName: str
    safeNumber: int
    description: str
    location: str
    creator: SafeCreator
    olacEnabled: bool
    managingCPM: str
    numberOfVersionsRetention: int
    numberOfDaysRetention: int
    autoPurgeEnabled: bool
    creationTime: int
    lastModificationTime: int
    accounts: list
    isExiredMember: bool

