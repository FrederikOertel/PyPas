"""Safe model""" ""
from dataclasses import dataclass


@dataclass
class SafeCreator:
    """Describes the creator of a safe."""

    id: str
    name: str


@dataclass
class Safe:
    """Describes a safe with its properties and accounts."""

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
