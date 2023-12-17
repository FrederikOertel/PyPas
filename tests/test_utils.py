VALID_IPV4_ADDRESS = "127.0.0.1"
VALID_IPV6_ADDRESS = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
INVALID_IPADDRESS = "abc"

VALID_PEM_CERTIFICATE = """-----BEGIN CERTIFICATE-----
MIIFaDCCBFCgAwIBAgISESHkvZFwK9Qz0KsXD3x8p44aMA0GCSqGSIb3DQEBCwUA
VQQDDBcqLmF3cy10ZXN0LnByb2dyZXNzLmNvbTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAMGPTyynn77hqcYnjWsMwOZDzdhVFY93s2OJntMbuKTHn39B
bml6YXRpb252YWxzaGEyZzIuY3JsMIGgBggrBgEFBQcBAQSBkzCBkDBNBggrBgEF
BQcwAoZBaHR0cDovL3NlY3VyZS5nbG9iYWxzaWduLmNvbS9jYWNlcnQvZ3Nvcmdh
bml6YXRpb252YWxzaGEyZzJyMS5jcnQwPwYIKwYBBQUHMAGGM2h0dHA6Ly9vY3Nw
lffygD5IymCSuuDim4qB/9bh7oi37heJ4ObpBIzroPUOthbG4gv/5blW3Dc=
-----END CERTIFICATE-----"""
INVALID_PEM_CERTIFICATE = """---this is a random text---"""

TEST_DICT_WITH_NONES = {
    "key1": "value1",
    "key2": None,
    "key3": "value3",
    "key4": None,
}

TEST_DICT_WITHOUT_NONES = {
    "key1": "value1",
    "key3": "value3",
}


def test_verify_is_valid_ip_address():
    from pypas.utils import verify_is_valid_ip_address

    assert verify_is_valid_ip_address(VALID_IPV4_ADDRESS) is True
    assert verify_is_valid_ip_address(VALID_IPV6_ADDRESS) is True
    assert verify_is_valid_ip_address(INVALID_IPADDRESS) is False


def test_validate_pem_format():
    from pypas.utils import validate_pem_format

    assert validate_pem_format(VALID_PEM_CERTIFICATE) is True
    assert validate_pem_format(INVALID_PEM_CERTIFICATE) is False


def test_remove_none_values_from_dict():
    from pypas.utils import remove_none_values_from_dict

    assert remove_none_values_from_dict(TEST_DICT_WITH_NONES) == TEST_DICT_WITHOUT_NONES
