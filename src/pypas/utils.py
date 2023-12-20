import ipaddress


def verify_is_valid_ip_address(ip_address: str) -> bool:
    """Verify if the given IP address is valid.

    Args:
        ip_address (str): The IP address to be verified.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def validate_pem_format(pem: str) -> bool:
    """Validate if the given string is in PEM format.

    Args:
        pem (str): The string to be validated.

    Returns:
        bool: True if the string is in PEM format, False otherwise.
    """
    # Pure certificate without private key
    if pem.startswith("-----BEGIN CERTIFICATE-----") and pem.endswith("-----END CERTIFICATE-----"):
        return True
    # Certificate with private key
    elif pem.startswith("-----BEGIN PRIVATE KEY-----") and pem.endswith("-----END CERTIFICATE-----"):
        return True
    return False


def remove_none_values_from_dict(d: dict) -> dict:
    """Remove None values from a dictionary.

    Args:
        d (dict): The dictionary to be cleaned.

    Returns:
        dict: The cleaned dictionary.
    """
    return {k: v for k, v in d.items() if v is not None}
