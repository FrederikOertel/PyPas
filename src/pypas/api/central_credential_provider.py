from dataclasses import dataclass

from pypas.central_credential_provider import CentralCredentialProvider
from pypas.model.credential import Credential


@dataclass
class CCP:
    ccp: CentralCredentialProvider

    def get_credential(self, safe_name: str, account_name: str) -> Credential:
        """Get a credential from a safe.
        Relevant CyberArk Documentation: https://docs.cyberark.com/AAM-CP/13.0/en/Content/CCP/Calling-the-Web-Service-using-REST.htm
        """
        return
