from pypas.model.safe_member import SafeMember, SafeMemberPermissions, SafeMemberType
from typing import List
import urllib

from pypas.utils import remove_none_values_from_dict


class SafeMembers:
    """Safe Members API endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def list(self, safe_identifier: str) -> List[SafeMember]:
        """List all members of a safe.
        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Safe%20Members%20-%20Get%20Safe%20Members.htm

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
            permissions = SafeMemberPermissions(**entry["permissions"])
            member = SafeMember(
                safeUrlId=entry["safeUrlId"],
                safeName=entry["safeName"],
                memberId=entry["memberId"],
                memberName=entry["memberName"],
                memberType=SafeMemberType(entry["memberType"]),
                membershipExpirationDate=entry["membershipExpirationDate"],
                isExpiredMembershipEnable=entry["isExpiredMembershipEnable"],
                isPredefinedUser=entry["isPredefinedUser"],
                isReadOnly=entry["isReadOnly"],
                permissions=permissions,
            )
            members.append(member)

        return members
