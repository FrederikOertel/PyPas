from pypas.model.safe import Safe, SafeAccount, SafeCreator
from typing import List
import urllib

from pypas.utils import remove_none_values_from_dict


def __parse_safe_from_cyberark_response(response: dict) -> Safe:
    safe_creator = SafeCreator(**response["Creator"])
    accounts = []
    for account in response["accounts"]:
        accounts.append(SafeAccount(**account))

    safe = Safe(
        safeUrlId=response["safeUrlId"],
        safeName=response["safeName"],
        safeNumber=response["safeNumber"],
        description=response["description"],
        location=response["location"],
        creator=safe_creator,
        olacEnabled=response["olacEnabled"],
        managingCPM=response["managingCPM"],
        numberOfVersionsRetention=response["numberOfVersionsRetention"],
        numberOfDaysRetention=response["numberOfDaysRetention"],
        autoPurgeEnabled=response["autoPurgeEnabled"],
        creationTime=response["creationTime"],
        lastModificationTime=response["lastModificationTime"],
        accounts=accounts,
        isExiredMember=response["isExiredMember"],
    )
    return safe


class Safes:
    """Safes API endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def list(
        self,
        limt: int = None,
        offset: int = None,
        useCache: bool = False,
        sort: bool = False,
        search: str = None,
        includeAccounts: bool = False,
        extendedDetails: bool = True,
    ) -> List[Safe]:
        """This method returns a list of all Safes in the Vault that the user has permissions for.
        The user who runs this web service must be a member of the Safes in the Vault that are returned in the list.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safes%20Web%20Services%20-%20List%20Safes.htm

        Args:
            limt (int, optional): The maximum number of Safes that are returned. Defaults to None.

            offset (int, optional): Offset of the first Safe that is returned in the collection of results.
            Defaults to None.

            useCache (bool, optional): Whether or not to retrieve the cache from a session. Defaults to False.

            sort (bool, optional): Sorts according to the safeName property in ascending order (default) or
            descending order to control the sort direction. Defaults to False.

            search (str, optional): Searches according to the Safe name. Search is performed according to
            the REST standard (search="search word"). Defaults to None.

            includeAccounts (bool, optional): Whether or not to return accounts for each Safe as part of the response.
            Defaults to False.

            extendedDetails (bool, optional): Whether or not to return all Safe details or only
            safeName as part of the response. Defaults to True.

        Returns:
            List[Safe]: List of Safe objects
        """

        params = {
            "limit": limt,
            "offset": offset,
            "useCache": useCache,
            "sort": sort,
            "search": search,
            "includeAccounts": includeAccounts,
            "extendedDetails": extendedDetails,
        }
        params = remove_none_values_from_dict(params)

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes?{urllib.parse.urlencode(params)}"

        response = self.vault.get_request(request_url)

        safes = []
        for entry in response.json()["safes"]:
            safe = __parse_safe_from_cyberark_response(entry)
            safes.append(safe)

        return safes

    def get(self, safe_identifier: str) -> Safe:
        """This method returns information about a specific Safe in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safes%20Web%20Services%20-%20Get%20Safes%20Details.htm


        Args:
            safe_identifier (str): safeUrLId or safeName

        Returns:
            Safe: A safe object
        """

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes/{safe_identifier}/"

        response = self.vault.get_request(request_url)

        safe = __parse_safe_from_cyberark_response(response.json())

        return safe

    def create(
        self,
        name: str,
        description: str = None,
        location: str = None,
        number_of_versions_retention: int = None,
        number_of_days_retention: int = None,
        managing_cpm: str = None,
        olac_enabled: bool = False,
    ) -> Safe:
        """
        This method adds a new Safe to the Vault.
        The user who runs this web service must have Add Safes permission in the Vault.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Add%20Safe.htm

        Args:
            name (str): Name of the new safe

            description (str, optional): The description of the Safe. Defaults to None.

            location (str, optional): The location of the Safe in the Vault. Defaults to None.

            number_of_versions_retention (int, optional):
            The number of retained versions of every password that is stored in the Safe. Defaults to None.

            number_of_days_retention (int, optional):
            The number of days that password versions are saved in the Safe. Defaults to None.

            managing_cpm (str, optional): The name of the CPM user who will manage the Safe. Defaults to None.

            olac_enabled (bool, optional): Whether or not to enable Object Level Access Control for the Safe.
            Defaults to False.

        Raises:
            ValueError: Only one of number_of_days_retention and number_of_versions_retention can be set.
            ValueError: Either number_of_days_retention or number_of_versions_retention must be set.

        Returns:
            Safe: A safe object
        """
        if number_of_days_retention and number_of_versions_retention:
            raise ValueError("Only one of number_of_days_retention and number_of_versions_retention can be set.")
        if not number_of_days_retention and not number_of_versions_retention:
            raise ValueError("Either number_of_days_retention or number_of_versions_retention must be set.")

        body = {
            "SafeName": name,
            "Description": description,
            "Location": location,
            "NumberOfVersionsRetention": number_of_versions_retention,
            "NumberOfDaysRetention": number_of_days_retention,
            "ManagingCPM": managing_cpm,
            "OlacEnabled": olac_enabled,
        }
        body = remove_none_values_from_dict(body)

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes"

        response = self.vault.post_request(request_url, body=body)

        safe = __parse_safe_from_cyberark_response(response.json())

        return safe

    def update(
        self,
        safe_identifier: str,
        name: str = None,
        description: str = None,
        location: str = None,
        number_of_versions_retention: int = None,
        number_of_days_retention: int = None,
        managing_cpm: str = None,
        olac_enabled: bool = False,
    ) -> Safe:
        """This method updates a single Safe in the Vault.
        The user who runs this web service must have Manage Safes permissions in the
        Vault and View Safe Members permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Update%20Safe.htm

        Args:
            safe_identifier (str): safeUrLId or safeName

            name (str, optional): The unique name of the Safe. Defaults to None.

            description (str, optional): The description of the Safe. Defaults to None.

            location (str, optional): The location of the Safe in the Vault. Defaults to None.

            number_of_versions_retention (int, optional): The number of retained versions of
            every password that is stored in the Safe. Defaults to None.

            number_of_days_retention (int, optional): The number of days that password versions are saved in the Safe.
            Defaults to None.

            managing_cpm (str, optional): The name of the CPM user who will manage the new Safe. Defaults to None.

            olac_enabled (bool, optional): Whether to enable Object Level Access Control for the new Safe.
            If you set the default value to True, you cannot revert to False.
            Defaults to False.

        Raises:
            ValueError: Only one of number_of_days_retention and number_of_versions_retention can be set.
            ValueError: Either number_of_days_retention or number_of_versions_retention must be set.

        Returns:
            Safe: The updated Safe
        """

        if number_of_days_retention and number_of_versions_retention:
            raise ValueError("Only one of number_of_days_retention and number_of_versions_retention can be set.")
        if not number_of_days_retention and not number_of_versions_retention:
            raise ValueError("Either number_of_days_retention or number_of_versions_retention must be set.")

        pre_update_safe = self.get(safe_identifier)

        updated_name = name if name else pre_update_safe.safeName
        updated_description = description if description else pre_update_safe.description
        updated_location = location if location else pre_update_safe.location
        updated_managing_cpm = managing_cpm if managing_cpm else pre_update_safe.managingCPM
        updated_olac_enabled = olac_enabled if olac_enabled else pre_update_safe.olacEnabled

        if number_of_days_retention:
            updated_number_of_days_retention = number_of_days_retention
            updated_number_of_versions_retention = None
        elif number_of_versions_retention:
            updated_number_of_versions_retention = number_of_versions_retention
            updated_number_of_days_retention = None
        else:
            updated_number_of_days_retention = pre_update_safe.numberOfDaysRetention
            updated_number_of_versions_retention = pre_update_safe.numberOfVersionsRetention

        body = {
            "SafeName": updated_name,
            "Description": updated_description,
            "Location": updated_location,
            "NumberOfVersionsRetention": updated_number_of_versions_retention,
            "NumberOfDaysRetention": updated_number_of_days_retention,
            "ManagingCPM": updated_managing_cpm,
            "OlacEnabled": updated_olac_enabled,
        }

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes"

        response = self.vault.put_request(request_url, body=body)

        safe = __parse_safe_from_cyberark_response(response.json())

        return safe

    def delete(self, safe_identifier: str):
        """This method deletes a Safe from the Vault.
        The user who runs this web service must have Manage Safe permissions in the Safe.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/WebServices/Delete%20Safe.htm

        Args:
            safe_identifier (str): safeUrlId or safeName (identifier of the safe)
        """

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes/{safe_identifier}"

        self.vault.delete_request(request_url)
