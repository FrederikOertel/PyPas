from pypas.model.safe import Safe


class Safes:
    """Safes API endpoint"""

    def __init__(self, vault):
        self.vault = vault

    def get(self, safe_identifier: str) -> Safe:
        """Get a single safe by its name.
        Relevant CyberArk Documentation:
        https://docs.cyberark.com/PAS/12.6/en/Content/SDK/Safes%20Web%20Services%20-%20Get%20Safes%20Details.htm
        """

        request_url = f"{self.vault.base_url}PasswordVault/API/Safes/{safe_identifier}/"

        self.vault.session.get(
        return
