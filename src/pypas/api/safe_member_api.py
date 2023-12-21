from dataclasses import asdict
from pypas.model.safe_member import SafeMember, SafeMemberPermissions, SafeMemberType
from typing import List

from pypas.utils import remove_none_values_from_dict


def __parse_safe_member_from_cyberark_response(response: dict) -> SafeMember:
    permissions = SafeMemberPermissions(**response["permissions"])
    member = SafeMember(
        safeUrlId=response["safeUrlId"],
        safeName=response["safeName"],
        safeNumber=response["safeNumber"],
        memberId=response["memberId"],
        memberName=response["memberName"],
        memberType=SafeMemberType(response["memberType"]),
        membershipExpirationDate=response["membershipExpirationDate"],
        isExpiredMembershipEnable=response["isExpiredMembershipEnable"],
        isPredefinedUser=response["isPredefinedUser"],
        isReadOnly=response["isReadOnly"],
        permissions=permissions,
    )
    return member


class SafeMembers:
    """Safe Members API endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def list(self, safe_identifier: str) -> List[SafeMember]:
        """This method returns a list of the members of a Safe.
        The user who runs this web service requires View Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safe%20Members%20WS%20-%20List%20Safe%20Members.htm

        Args:
            safe_name (str): safeUrLId or safeName

        Returns:
            List[SafeMember]: List containing all safe Members
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Safes/{safe_identifier}/Members"

        response = self.vault.get_request(request_url)

        response.raise_for_status()

        members = []
        for entry in response.json()["members"]:
            member = __parse_safe_member_from_cyberark_response(entry)
            members.append(member)

        return members

    def get(self, safe_identifier: str, member_name: str, useCache: bool = False) -> SafeMember:
        """This method returns a member of a Safe.
        The user who runs this web service must have View Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safe%20Members%20WS%20-%20List%20Safe%20Member.htm

        Args:
            safe_name (str): safeUrLId or safeName
            member_name (str): memberName
            useCache (bool, optional): Whether to retrieve from session or not. Defaults to False.

        Returns:
            SafeMember: Safe Member
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Safes/{safe_identifier}/Members/{member_name}"

        if useCache:
            request_url += "?useCache=true"

        response = self.vault.get_request(request_url)

        response.raise_for_status()

        member = __parse_safe_member_from_cyberark_response(response.json())

        return member

    def add(
        self,
        safe_identifier: str,
        member_name: str,
        member_type: SafeMemberType,
        permissions: SafeMemberPermissions,
        search_in: str = "Vault",
        membership_expiration_date: str = None,
        is_read_only: bool = False,
    ) -> SafeMember:
        """This method adds an existing user or group as a Safe member.
        The user who runs this web service requires Manage Safe Members permissions in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safe%20Members%20WS%20-%20Add%20Safe%20Member.htm

        Args:
            safe_identifier (str):

            member_name (str): The Vault user name, Domain user name or group name of the Safe member.
            The following characters cannot be used in the Safe member name: \\ / : * < > “ | ? % & +

            member_type (SafeMemberType): The member type.

            permissions (SafeMemberPermissions): The permissions that the user or group has on this Safe.

            search_in (str, optional): The Vault or the domain where the user or group was found. Defaults to "Vault".

            membership_expiration_date (str, optional): The member's expiration date for this Safe.
            For members that do not have an expiration date, this value will be null.. Defaults to None.

            is_read_only (bool, optional): Whether or not the current user can update the permissions of the member.
            Defaults to False.

        Returns:
            SafeMember: Safe Member
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Safes/{safe_identifier}/Members"

        payload = {
            "memberName": member_name,
            "searchIn": search_in,
            "membershipExpirationDate": membership_expiration_date,
            "memberType": member_type.value,
            "permissions": asdict(permissions),
            "isReadOnly": is_read_only,
        }

        payload = remove_none_values_from_dict(payload)

        response = self.vault.post_request(request_url, payload)

        response.raise_for_status()

        member = __parse_safe_member_from_cyberark_response(response.json())

        return member

    def update(
        self,
        safe_identifier: str,
        member_name: str,
        permissions: SafeMemberPermissions,
        membership_expiration_date: int = None,
    ) -> SafeMember:
        """This method updates an existing Safe member.
        The user who runs this web service requires Manage Safe Members permissions in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Update%20Safe%20Member.htm

        Args:
            safe_identifier (str): safeUrLId or safeName
            member_name (str): memberName
            permissions (SafeMemberPermissions): The permissions that the user or group has on this Safe.
            membership_expiration_date (int, optional): The time when the member`s Safe membership expires.

        Returns:
            SafeMember: Safe Member
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Safes/{safe_identifier}/Members/{member_name}"

        payload = {
            "MembershipExpirationDate": membership_expiration_date,
            "permissions": asdict(permissions),
        }

        payload = remove_none_values_from_dict(payload)

        response = self.vault.put_request(request_url, payload)

        response.raise_for_status()

        member = __parse_safe_member_from_cyberark_response(response.json())

        return member

    def delete(self, safe_identifier: str, member_name: str) -> None:
        """This method removes a specific member from a Safe.
        The user who runs this web service must have Manage Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Delete%20Safe%20Member.htm

        Args:
            safe_identifier (str): safeUrLId or safeName
            member_name (str): memberName
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Safes/{safe_identifier}/Members/{member_name}"

        response = self.vault.delete_request(request_url)

        response.raise_for_status()
