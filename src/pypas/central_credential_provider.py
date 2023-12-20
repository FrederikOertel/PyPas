from dataclasses import dataclass
from .api.central_credential_provider_api import Credentials
import httpx
from httpx import Client


@dataclass
class CentralCredentialProvider:
    """CentralCredentialProvider model class."""

    ccp_base_url: str
    ccp_iis_site: str = "AIMWebService"
    ccp_verify_requests: bool = True
    session: httpx.Client = None

    def __post_init__(self):
        self.credentials = Credentials(self)

    def get_session(self) -> Client:
        """Get a session for the CCP."""
        if self.session:
            return self.session

        return Client(
            base_url=self.ccp_base_url,
            verify=self.ccp_verify_requests,
            headers={"Content-Type": "application/json"},
        )
