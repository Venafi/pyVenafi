class PKI:
    class PKI:
        def __init__(self, pki_dict: dict):
            if not isinstance(pki_dict, dict):
                pki_dict = {}

            self.certificate_dn = pki_dict.get('CertificateDN')  # type: str
            self.certificate_guid = pki_dict.get('CertificateGuid')  # type: str
            self.pki_dn = pki_dict.get('PkiDn')  # type: str
            self.pki_guid = pki_dict.get('PkiGuid')  # type: str

    class Certificate:
        def __init__(self, certificate_dict: dict):
            if not isinstance(certificate_dict, dict):
                certificate_dict = {}

            self.city = certificate_dict.get('City')  # type: str
            self.common_name = city = certificate_dict.get('CommonName')  # type: str
            self.country = city = certificate_dict.get('Country')  # type: str
            self.key_algorithm = certificate_dict.get('KeyAlgorithm')  # type: str
            self.key_bit_size = certificate_dict.get('KeyBitSize')  # type: str
            self.organization = certificate_dict.get('Organization')  # type: str
            self.organizational_units = certificate_dict.get('OrganizationalUnits')  # type: list
            self.sans = [PKI.SANS(sans) for sans in certificate_dict.get('SANs', [])]
            self.state = certificate_dict.get('State')  # type: str

    class Installation:
        def __init__(self, installation_dict: dict):
            if not isinstance(installation_dict, dict):
                installation_dict = {}

            self.credential_dn = installation_dict.get('CredentialDn')  # type: str
            self.host = installation_dict.get('Host')  # type: str

    class SANS:
        def __init__(self, sans_dict: dict):
            if not isinstance(sans_dict, dict):
                sans_dict = {}
                
            self.name = sans_dict.get('Name')  # type: str
            self.typename = sans_dict.get('TypeName')  # type: str
