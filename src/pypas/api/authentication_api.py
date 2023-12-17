from enum import Enum

from pypas.utils import remove_none_values_from_dict


class AuthMethod(Enum):
    """Authentication method enumeration"""

    CyberArk = 1
    Windows = 2
    LDAP = 3
    RADIUS = 4


class Authentication:
    """Authentication API endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def logon(
        self,
        username: str,
        password: str,
        new_password: str = None,
        auth_method: AuthMethod = AuthMethod.CyberArk,
        concurrent_session: bool = True,
    ):
        """Logon to the vault.
        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/CyberArk%20Authentication%20-%20Logon_v10.htm
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/auth/{auth_method}/Logon/"

        data = {
            "username": username,
            "password": password,
            "newPassword": new_password,
            "concurrentSession": concurrent_session,
        }

        data = remove_none_values_from_dict(data)

        response = self.vault.session.post(request_url, json=data, verify=self.vault.verify_requests)

        response.raise_for_status()

        return response.json()
