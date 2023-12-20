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
        extendedDetails: bool = False,
    ) -> List[Safe]:
        """List all safes.
        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safes%20Web%20Services%20-%20List%20Safes.htm
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
        for safe in response.json()["safes"]:
            safe_creator = SafeCreator(**response.json()["Creator"])
            accounts = []
            for account in response.json()["accounts"]:
                accounts.append(SafeAccount(**account))

            safe = Safe(
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
        """Create a new safe."""
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
