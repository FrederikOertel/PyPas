"""SafeMember model class."""
from dataclasses import dataclass
from enum import Enum


class SafeMemberType(Enum):
    """Describes the type of a safe member.

    Options:
        User: A user.
        Group: A group.
    """

    User = 1
    Group = 2


@dataclass
class SafeMemberPermissions:
    """Describes the permissions of a safe member.

    Attributes:
        useAccounts (bool): Use accounts but cannot view passwords.

        retrieveAccounts (bool): Retrieve and view accounts in the Safe.

        listAccounts (bool): View the Accounts list.

        addAccounts (bool): Add accounts in the Safe.
        Users who have this permission automatically have UpdateAccountProperties permissions as well.

        updateAccountContent (bool): Update existing account content.

        updateAccountProperties (bool): Update existing account properties.

        initiateCPMAccountManagementOperations (bool): Initiate password management operations through CPM,
        such as changing, verifying, and reconciling passwords.
        When this parameter is set to False, the SpecifyNextAccountContent parameter is also automatically set to False.

        specifyNextAccountContent (bool): Specify the password that is used when the CPM changes the password value.
        This parameter can only be specified when the InitiateCPMAccountManagementOperations parameter is set to True.
        When InitiateCPMAccountManagementOperations is set to False, this parameter is automatically set to False.

        renameAccounts (bool): Rename existing accounts in the Safe.

        deleteAccounts (bool): Delete existing passwords in the Safe.

        unlockAccounts (bool): Unlock accounts that are locked by other users.

        manageSafe (bool): Perform administrative tasks in the Safe, including:
        Update Safe properties, Recover the Safe and Delete the Safe

        manageSafeMembers (bool): Add and remove Safe members, and update their authorizations in the Safe.

        backupSafe (bool): Create a backup of a Safe and its contents, and store in another location.

        viewAuditLog (bool): View account and user activity in the Safe.

        viewSafeMembers (bool): View Safe members` permissions.

        accessWithoutConfirmation (bool): Access the Safe without confirmation from authorized users.
        This overrides the Safe properties that specify that Safe members require confirmation to access the Safe.

        createFolders (bool): Create folders in the Safe.

        deleteFolders (bool): Delete folders from the Safe.

        moveAccountsAndFolders (bool): Move accounts and folders in the Safe to different folders and subfolders.

        requestsAuthorizationLevel1 (bool): Request Authorization Level 1.

        requestsAuthorizationLevel2 (bool): Request Authorization Level 2.
    """

    useAccounts: bool = False
    retrieveAccounts: bool = False
    listAccounts: bool = False
    addAccounts: bool = False
    updateAccountContent: bool = False
    updateAccountProperties: bool = False
    initiateCPMAccountManagementOperations: bool = False
    specifyNextAccountContent: bool = False
    renameAccounts: bool = False
    deleteAccounts: bool = False
    unlockAccounts: bool = False
    manageSafe: bool = False
    manageSafeMembers: bool = False
    backupSafe: bool = False
    viewAuditLog: bool = False
    viewSafeMembers: bool = False
    accessWithoutConfirmation: bool = False
    createFolders: bool = False
    deleteFolders: bool = False
    moveAccountsAndFolders: bool = False
    requestsAuthorizationLevel1: bool = False
    requestsAuthorizationLevel2: bool = False


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
