from dataclasses import dataclass
from .api.central_credential_provider import CCP


@dataclass
class CentralCredentialProvider:
    """CentralCredentialProvider model class."""

    ccp_base_url: str
    ccp_iis_site: str = "AIMWebService"
    ccp_verify_requests: bool = True

    def __post_init__(self):
        self.ccp = CCP(self)
