from dataclasses import dataclass
from enum import Enum

class SafeMemberType(Enum):
    User = 1
    Group = 2

@dataclass
class SafeMemberPermissions:
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

