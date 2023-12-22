from typing import List
import urllib
from pypas.model.user import (
    User,
    UserBusinessAddress,
    UserInternet,
    UserPhones,
    UserPersonalDetails,
    UserAuthenticationMethod,
    UserInterface,
    UserSource,
    UserGroupsMembership,
    UserVaultAuthorization,
)

from pypas.utils import remove_none_values_from_dict


def __parse_user_from_cyberark_response(response: dict) -> User:
    if "personalDetails" in response:
        user_personal_details = UserPersonalDetails(**response["personalDetails"])
    if "userPhones" in response:
        user_phones = UserPhones(**response["phones"])
    if "userInternet" in response:
        user_internet = UserInternet(**response["internet"])
    if "userBusinessAddress" in response:
        user_business_address = UserBusinessAddress(**response["businessAddress"])
    if "groupsMembership" in response:
        group_memberships = []
        for group in response["groupsMembership"]:
            group = UserGroupsMembership(**group)
            group_memberships.append(group)
    if "vaultAuthorization" in response:
        vault_authorizations = []
        for vault_authorization in response["vaultAuthorization"]:
            vault_authorization = UserVaultAuthorization(vault_authorization)
            vault_authorizations.append(vault_authorization)

    user = User(
        id=response["id"],
        username=response["username"],
        first_name=response["firstName"],
        last_name=response["lastName"],
        email=response["email"],
        description=response["description"],
        user_personal_details=user_personal_details,
        user_phones=user_phones,
        user_internet=user_internet,
        user_business_address=user_business_address,
        user_authentication_method=UserAuthenticationMethod(response["authenticationMethod"]),
        user_interface=UserInterface(response["userInterface"]),
        user_source=UserSource(response["userSource"]),
        group_memberships=group_memberships,
        vault_authorizations=vault_authorizations,
    )
    return user


class Users:
    """Users Endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def list(self, filter: str = None) -> List[User]:
        """This method returns a list of users.
        The user who runs this web service requires View Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/get-users-api.htm

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

        users = []
        for entry in response.json()["users"]:
            user = __parse_user_from_cyberark_response(entry)
            users.append(user)

        return users

    def get(self, user_id: str) -> User:
        """This method returns information about a specific user in the Vault.
        To run this Web service, you must have Audit users permissions.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/get-users-api.htm

        Args:
            user_id (str): The ID of the user for which information is returned.

        Returns:
            User: The user.
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Users/{user_id}"
        if "." in user_id:
            request_url += "/"

        response = self.vault.get_request(request_url)

        user = __parse_user_from_cyberark_response(response.json())

        return user

    def activate(self, user_id: str):
        """This method activates an existing user who was suspended after entering incorrect credentials multiple times.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/activate-user-v10.htm

        Args:
            user_id (str): The user ID of the user to activate.
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Users/{user_id}/Activate"
        if "." in user_id:
            request_url += "/"

        self.vault.post_request(request_url)

    def enable(self, user_id: str):
        """This method enables a specific user in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Enable-user.htm

        Args:
            user_id (str): The user ID of the user to enable.
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Users/{user_id}/enable"
        if "." in user_id:
            request_url += "/"

        self.vault.post_request(request_url)

    def disable(self, user_id: str):
        """This method disables a specific user in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Disable-user.htm
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Users/{user_id}/disable"
        if "." in user_id:
            request_url += "/"

        self.vault.post_request(request_url)

    def reset_password(self, user_id: str, new_password: str):
        """This method resets an existing Vault user's password.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/reset-user-password.htm

        Args:
            user_id (str): The user ID of the user to reset the password for.
            new_password (str): The new password to set for the user.
        """

        request_url = f"{self.vault.base_url}PasswordVault/api/Users/{user_id}/ResetPassword"
        if "." in user_id:
            request_url += "/"

        body = {"id": new_password, "newPassword": new_password}

        self.vault.post_request(request_url, body=body)
