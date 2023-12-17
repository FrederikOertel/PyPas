from pypas.central_credential_provider import CentralCredentialProvider
from pypas.model.reqresuser import ReqresUser
from pypas.api.authentication_api import AuthMethod
import dataclasses

from pypas.vault import Vault

ccp = CentralCredentialProvider("https://reqres.in/")

creds = ccp.credentials.get_credential("ccp_appid", "ww_mysafe")

print(creds)
print(type(creds))
print(dataclasses.is_dataclass(creds))
for cred in creds:
    print(cred)
    print(type(cred))
    print(isinstance(cred, ReqresUser))


vault = Vault("https://reqres.in/")

vault.Authentication.logon("myuser", "mypassword", auth_method=AuthMethod.CyberArk)

safe = vault.Safes.get("ww_mysafe")
