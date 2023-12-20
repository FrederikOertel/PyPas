"""Safe model""" ""
from dataclasses import dataclass
from typing import List


@dataclass
class SafeCreator:
    """
    Describes the creator of a safe.

    Attributes:
        id (str): The unique ID of the creator.

        name (str): The unique name of the creator.
    """

    id: str
    name: str


@dataclass
class SafeAccount:
    """
    Describe a minimal representation of an account in a safe.

    Attributes:
        id (str): The unique ID of the account.

        name (str): The unique name of the account.
    """

    id: str
    name: str


@dataclass
class Safe:
    """
    Information about a specific safe in the vault.


    Attributes:
        safeUrlId (str): The unique ID of the Safe used when calling Safe APIs.

        safeName (str): The unique name of the Safe.

        safeNumber (int): The unique numerical ID of the Safe.

        description (str): The description of the Safe.

        location (str): The location of the Safe in the Vault.

        creator (SafeCreator): The safe's creator.

        olacEnabled (bool): Whether or not Object Level Access Control is enabled for the Safe.

        managingCPM (str): The name of the CPM user managing the Safe.

        numberOfVersionsRetention (int): The number of retained versions of every password that is stored in the Safe.

        numberOfDaysRetention (int): The number of days that password versions are saved in the Safe.

        autoPurgeEnabled (bool): Whether or not files will be automatically purged after the end of the
        Object History Retention Period defined in the Safe properties.
        Report Safes and PSM Recording Safes are created automatically with AutoPurgeEnabled set to Yes.
        These Safes cannot be managed by the CPM.

        creationTime (int): The Unix creation time of the Safe.

        lastModificationTime (int): The Unix time when the Safe was last updated.

        accounts (List[SafeAccount]): The safe's accounts.

        isExiredMember (bool): Whether or not the membership for the Safe is expired.
        For expired members, the value is True.
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
    accounts: List[SafeAccount]
    isExiredMember: bool
