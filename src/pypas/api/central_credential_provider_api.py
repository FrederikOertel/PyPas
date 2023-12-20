from typing import List
from pypas.model.reqresuser import ReqresUser
import urllib
import httpx

from pypas.utils import remove_none_values_from_dict


class Credentials:
    """Credentials endpoint of the Central Credential Provider."""

    def __init__(self, ccp):
        self.ccp = ccp

    def get_credential(
        self,
        app_id: str,
        safe: str,
        folder: str = None,
        object: str = None,
        user_name: str = None,
        address: str = None,
        database: str = None,
        policy_id: str = None,
        reason: str = None,
        connection_timeout: int = None,
        fail_on_password_change: bool = None,
        certificate_path: str = None,
        certificate_key_path: str = None,
        certificate_password: str = None,
    ) -> List[ReqresUser]:
        """Get a credential from a safe.
        Relevant CyberArk Documentation:
        https://docs.cyberark.com/AAM-CP/13.0/en/Content/CCP/Calling-the-Web-Service-using-REST.htm
        """
        params = {
            "AppID": app_id,
            "Safe": safe,
            "Folder": folder,
            "Object": object,
            "UserName": user_name,
            "Address": address,
            "Database": database,
            "PolicyID": policy_id,
            "Reason": reason,
            "ConnectionTimeout": connection_timeout,
            "FailOnPasswordChange": fail_on_password_change,
        }
        params = remove_none_values_from_dict(params)

        request_url = f"{self.ccp.ccp_base_url}{self.ccp.ccp_iis_site}/api/Accounts?{urllib.parse.urlencode(params)}"

        with self.ccp.get_session() as client:
            if not certificate_path:
                response = client.get(
                    request_url,
                )
            else:
                if certificate_path and certificate_key_path and certificate_password:
                    cert = (certificate_path, certificate_key_path, certificate_password)
                elif certificate_path and certificate_key_path:
                    cert = (certificate_path, certificate_key_path)
                else:
                    cert = certificate_path
                response = httpx.get(request_url, cert=cert)
            response.raise_for_status()

        users = []
        for user in response.json()["data"]:
            users.append(ReqresUser(**user))

        return users
