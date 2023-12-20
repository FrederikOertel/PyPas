from pypas.model.safe import Safe, SafeAccount, SafeCreator
from typing import List
import urllib

from pypas.utils import remove_none_values_from_dict


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
        """List all safes.
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
            safe_creator = SafeCreator(**entry["Creator"])
            accounts = []
            for account in entry["accounts"]:
                accounts.append(SafeAccount(**account))

            safe = Safe(
                safeUrlId=entry["safeUrlId"],
                safeName=entry["safeName"],
                safeNumber=entry["safeNumber"],
                description=entry["description"],
                location=entry["location"],
                creator=safe_creator,
                olacEnabled=entry["olacEnabled"],
                managingCPM=entry["managingCPM"],
                numberOfVersionsRetention=entry["numberOfVersionsRetention"],
                numberOfDaysRetention=entry["numberOfDaysRetention"],
                autoPurgeEnabled=entry["autoPurgeEnabled"],
                creationTime=entry["creationTime"],
                lastModificationTime=entry["lastModificationTime"],
                accounts=accounts,
                isExiredMember=entry["isExiredMember"],
            )
            safes.append(safe)
        return safes

    def get(self, safe_identifier: str) -> Safe:
        """Get a single safe by its name.

        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safes%20Web%20Services%20-%20Get%20Safes%20Details.htm


        Args:
            safe_identifier (str): safeUrLId or safeName

        Returns:
            Safe: A safe object
        """

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes/{safe_identifier}/"

        response = self.vault.get_request(request_url)
        response.raise_for_status()

        safe_creator = SafeCreator(**response.json()["Creator"])

        accounts = []
        for account in response.json()["accounts"]:
            accounts.append(SafeAccount(**account))

        return Safe(
            safeUrlId=response.json()["safeUrlId"],
            safeName=response.json()["safeName"],
            safeNumber=response.json()["safeNumber"],
            description=response.json()["description"],
            location=response.json()["location"],
            creator=safe_creator,
            olacEnabled=response.json()["olacEnabled"],
            managingCPM=response.json()["managingCPM"],
            numberOfVersionsRetention=response.json()["numberOfVersionsRetention"],
            numberOfDaysRetention=response.json()["numberOfDaysRetention"],
            autoPurgeEnabled=response.json()["autoPurgeEnabled"],
            creationTime=response.json()["creationTime"],
            lastModificationTime=response.json()["lastModificationTime"],
            accounts=accounts,
            isExiredMember=response.json()["isExiredMember"],
        )

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

        response.raise_for_status()

        safe_creator = SafeCreator(**response.json()["Creator"])

        accounts = []
        for account in response.json()["accounts"]:
            accounts.append(SafeAccount(**account))

        return Safe(
            safeUrlId=response.json()["safeUrlId"],
            safeName=response.json()["safeName"],
            safeNumber=response.json()["safeNumber"],
            description=response.json()["description"],
            location=response.json()["location"],
            creator=safe_creator,
            olacEnabled=response.json()["olacEnabled"],
            managingCPM=response.json()["managingCPM"],
            numberOfVersionsRetention=response.json()["numberOfVersionsRetention"],
            numberOfDaysRetention=response.json()["numberOfDaysRetention"],
            autoPurgeEnabled=response.json()["autoPurgeEnabled"],
            creationTime=response.json()["creationTime"],
            lastModificationTime=response.json()["lastModificationTime"],
            accounts=accounts,
            isExiredMember=response.json()["isExiredMember"],
        )

    def update(
        self,
        safe_identifier: str,
        new_name: str = None,
        new_description: str = None,
        new_location: str = None,
        new_number_of_versions_retention: int = None,
        new_number_of_days_retention: int = None,
        new_managing_cpm: str = None,
        new_olac_enabled: bool = False,
    ) -> Safe:
        """Create a new safe."""

        if new_number_of_days_retention and new_number_of_versions_retention:
            raise ValueError("Only one of number_of_days_retention and number_of_versions_retention can be set.")
        if not new_number_of_days_retention and not new_number_of_versions_retention:
            raise ValueError("Either number_of_days_retention or number_of_versions_retention must be set.")

        pre_update_safe = self.get(safe_identifier)

        updated_name = new_name if new_name else pre_update_safe.safeName
        updated_description = new_description if new_description else pre_update_safe.description
        updated_location = new_location if new_location else pre_update_safe.location
        updated_managing_cpm = new_managing_cpm if new_managing_cpm else pre_update_safe.managingCPM
        updated_olac_enabled = new_olac_enabled if new_olac_enabled else pre_update_safe.olacEnabled

        if new_number_of_days_retention:
            updated_number_of_days_retention = new_number_of_days_retention
            updated_number_of_versions_retention = None
        elif new_number_of_versions_retention:
            updated_number_of_versions_retention = new_number_of_versions_retention
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

        response.raise_for_status()

        safe_creator = SafeCreator(**response.json()["Creator"])

        accounts = []
        for account in response.json()["accounts"]:
            accounts.append(SafeAccount(**account))

        return Safe(
            safeUrlId=response.json()["safeUrlId"],
            safeName=response.json()["safeName"],
            safeNumber=response.json()["safeNumber"],
            description=response.json()["description"],
            location=response.json()["location"],
            creator=safe_creator,
            olacEnabled=response.json()["olacEnabled"],
            managingCPM=response.json()["managingCPM"],
            numberOfVersionsRetention=response.json()["numberOfVersionsRetention"],
            numberOfDaysRetention=response.json()["numberOfDaysRetention"],
            autoPurgeEnabled=response.json()["autoPurgeEnabled"],
            creationTime=response.json()["creationTime"],
            lastModificationTime=response.json()["lastModificationTime"],
            accounts=accounts,
            isExiredMember=response.json()["isExiredMember"],
        )

    def delete(self, safe_identifier: str):
        """Delete a safe.

        Args:
            safe_identifier (str): safeUrlId or safeName (identifier of the safe)
        """

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes/{safe_identifier}"

        response = self.vault.delete_request(request_url)

        response.raise_for_status()
