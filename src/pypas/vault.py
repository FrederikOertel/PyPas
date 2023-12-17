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
