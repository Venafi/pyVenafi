from typing import List
from pytpp.properties.resultcodes import ResultCodes


class SSHCertificate:
    class Response:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.success = response_object.get('Success')  # type: bool
            self.error_code = response_object.get('ErrorCode')  # type: int
            self.error_message = ResultCodes.SSHErrorCodes.get(self.error_code, 'Unknown') if self.error_code else None  # type: str

    class ProcessingDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.status = response_object.get('Status')  # type: str
            self.status_description = response_object.get('StatusDescription')  # type: str

    class CertificateDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.ca_fingerprint_sha256 = response_object.get('CAFingerprintSHA256') # type: str
            self.certificate_fingerprint_sha256 = response_object.get('CertificateFingerprintSHA256') # type: str
            self.certificate_type = response_object.get('CertificateType') # type: str
            self.extensions = response_object.get('Extensions') # type: dict
            self.key_id = response_object.get('KeyID') # type: str
            self.key_type = response_object.get('KeyType') # type: str
            self.principals = response_object.get('Principals') # type: List[str]
            self.public_key_fingerprint_sha256 = response_object.get('PublicKeyFingerprintSHA256') # type: str
            self.serial_number = response_object.get('SerialNumber') # type: str
            self.valid_from = response_object.get('ValidFrom') # type: int
            self.valid_to = response_object.get('ValidTo') # type: int

    class RequestDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.originating_ip = response_object.get('OriginatingIP') # type: str
            self.requested_by = response_object.get('RequestedBy') # type: str

    class APIClient:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allowed_to_request_certificate_identifier = response_object.get('AllowedToRequestCertificateIdentifier') # type: bool
            self.allowed_to_request_extensions = response_object.get('AllowedToRequestExtensions') # type: bool
            self.allowed_to_request_force_command = response_object.get('AllowedToRequestForceCommand') # type: bool
            self.allowed_to_request_principals = response_object.get('AllowedToRequestPrincipals') # type: bool
            self.allowed_to_request_source_addresses = response_object.get('AllowedToRequestSourceAddresses') # type: bool

    class Certificate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.allowed_private_key_algorithms = response_object.get('AllowedPrivateKeyAlgorithms') # type: List[str]
            self.allowed_private_key_reuse = response_object.get('AllowedPrivateKeyReuse') # type: bool
            self.certificate_destination_dn = response_object.get('CertificateDestinationDn') # type: str
            self.default_private_key_algorithm = response_object.get('DefaultPrivateKeyAlgorithm') # type: str
            self.signature_hashing_algorithm = response_object.get('SignatureHashingAlgorithm') # type: str
            self.type = response_object.get('Type') # type: str
            self.validity_period = response_object.get('ValidityPeriod') # type: str

    class CAKeyPair:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.created_on = response_object.get('CreatedOn') # type: str
            self.dn = response_object.get('DN') # type: str
            self.fingerprint_sha256 = response_object.get('FingerprintSHA256') # type: str
            self.guid = response_object.get('Guid') # type: str
            self.key_algorithm = response_object.get('KeyAlgorithm') # type: str
            self.name = response_object.get('Name') # type: str
            self.public_key_data = response_object.get('PublicKeyData') # type: str
