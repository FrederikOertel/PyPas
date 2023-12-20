from dataclasses import dataclass
from .api.safe_api import Safes
from .api.authentication_api import Authentication


@dataclass
class Vault:
    """CyberArk Vault model class."""

    base_url: str
    verify_requests: bool = True

    def __post_init__(self):
        self.Safes = Safes(self)
        self.Authentication = Authentication(self)

    def get_request(self, url: str, params: dict = None) -> dict:
        """Make a GET request to the vault."""
        return {}

    def post_request(self, url: str, params: dict = None, body: dict = None) -> dict:
        """Make a POST request to the vault."""
        return {}

    def put_request(self, url: str, params: dict = None, body: dict = None) -> dict:
        """Make a PUT request to the vault."""
        return {}

    def delete_request(self, url: str, params: dict = None, body: dict = None) -> dict:
        """Make a DELETE request to the vault."""
        return {}
