def test_ccp_get_password():
    from pypas.central_credential_provider import CentralCredentialProvider
    from pypas.model.reqresuser import ReqresUser

    ccp = CentralCredentialProvider("https://reqres.in/")

    creds = ccp.credentials.get_credential("2")
    print(creds)
    assert isinstance(creds, ReqresUser)
