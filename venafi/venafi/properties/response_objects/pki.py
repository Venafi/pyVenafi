class PKI:
    class PKI:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.certificate_dn = response_object.get('CertificateDN')  # type: str
            self.certificate_guid = response_object.get('CertificateGuid')  # type: str
            self.pki_dn = response_object.get('PkiDn')  # type: str
            self.pki_guid = response_object.get('PkiGuid')  # type: str

    class Certificate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.city = response_object.get('City')  # type: str
            self.common_name = city = response_object.get('CommonName')  # type: str
            self.country = city = response_object.get('Country')  # type: str
            self.key_algorithm = response_object.get('KeyAlgorithm')  # type: str
            self.key_bit_size = response_object.get('KeyBitSize')  # type: str
            self.organization = response_object.get('Organization')  # type: str
            self.organizational_units = response_object.get('OrganizationalUnits')  # type: list
            self.sans = [PKI.SANS(sans) for sans in response_object.get('SANs', [])]
            self.state = response_object.get('State')  # type: str

    class Installation:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.credential_dn = response_object.get('CredentialDn')  # type: str
            self.host = response_object.get('Host')  # type: str

    class SANS:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
                
            self.name = response_object.get('Name')  # type: str
            self.typename = response_object.get('TypeName')  # type: str
