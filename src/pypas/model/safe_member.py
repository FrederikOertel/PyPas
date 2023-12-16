"""SafeMember model class."""
from dataclasses import dataclass
from enum import Enum


class SafeMemberType(Enum):
    """Describes the type of a safe member."""

    User = 1
    Group = 2


@dataclass
class SafeMemberPermissions:
    """Describes the permissions of a safe member."""

    useAccounts: bool
    retrieveAccounts: bool
    listAccounts: bool
    addAccounts: bool
    updateAccountContent: bool
    updateAccountProperties: bool
    initiateCPMAccountManagementOperations: bool
    specifyNextAccountContent: bool
    renameAccounts: bool
    deleteAccounts: bool
    unlockAccounts: bool
    manageSafe: bool
    manageSafeMembers: bool
    backupSafe: bool
    viewAuditLog: bool
    viewSafeMembers: bool
    accessWithoutConfirmation: bool
    createFolders: bool
    deleteFolders: bool
    moveAccountsAndFolders: bool
    requestsAuthorizationLevel1: bool
    requestsAuthorizationLevel2: bool


@dataclass
class SafeMember:
    """Describes a safe member with their permissions."""

    safeUrlId: str
    safeName: str
    safeNumber: int
    memberId: int
    memberName: str
    memberType: SafeMemberType
    membershipExpirationDate: str
    isExpiredMembershipEnable: bool
    isPredefinedUser: bool
    permissions: SafeMemberPermissions
    isReadOnly: bool
