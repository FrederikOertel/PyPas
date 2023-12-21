from typing import List
import urllib

from pypas.utils import remove_none_values_from_dict


class Users:
    """Users Endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def list(self, filter: str = None) -> List[ReqresUser]:
        """This method returns a list of users.
        The user who runs this web service requires View Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safe%20Members%20WS%20-%20List%20Safe%20Members.htm

        Args:
            safe_name (str): safeUrLId or safeName

        Returns:
            List[SafeMember]: List containing all safe Members
        """

        params = {
            "filter": filter,
        }
        params = remove_none_values_from_dict(params)

        request_url = f"{self.vault.base_url}PasswordVault/api/Users?{urllib.parse.urlencode(params)}"

        response = self.vault.get_request(request_url)

        response.raise_for_status()

        users = []
        for entry in response.json()["users"]:
            user = ReqresUser(**entry)
            users.append(user)

        return users