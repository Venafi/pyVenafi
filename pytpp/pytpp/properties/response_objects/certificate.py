from typing import List
from pytpp.tools.helpers.date_converter import from_date_string


class Certificate:
    class Certificate:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.created_on = response_object.get('CreatedOn')  # type: str
            self.dn = response_object.get('DN')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.name = response_object.get('Name')  # type: str
            self.parent_dn = response_object.get('ParentDn')  # type: str
            self.schema_class = response_object.get('SchemaClass')  # type: str
            self.x509 = Certificate._X509(response_object.get('X509'))
            self.links = [Certificate.Link(link) for link in response_object.get('_links', [])]

    class Link:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.details = response_object.get('Details')  # type: str
            self.next = response_object.get('Next')  # type: str
            self.previous = response_object.get('Previous')  # type: str

    class CSR:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.details = Certificate._CSRDetails(response_object.get('Details'))
            self.enrollable = response_object.get('Enrollable')  # type: bool

    class Policy:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.certificate_authority = Certificate._LockedSingleValue(response_object.get('CertificateAuthority'))
            self.csr_generation = Certificate._LockedSingleValue(response_object.get('CsrGeneration'))
            self.key_generation = Certificate._LockedSingleValue(response_object.get('KeyGeneration'))
            self.key_pair = Certificate._LockedKeyPair(response_object.get('KeyPair'))
            self.management_type = Certificate._LockedSingleValue(response_object.get('ManagementType'))
            self.private_key_reuse_allowed = response_object.get('PrivateKeyReuseAllowed')  # type: bool
            self.subj_alt_name_dns_allowed = response_object.get('SubjAltNameDnsAllowed')  # type: bool
            self.subj_alt_name_email_allowed = response_object.get('SubjAltNameEmailAllowed')  # type: bool
            self.subj_alt_name_ip_allowed = response_object.get('SubjAltNameIpAllowed')  # type: bool
            self.subj_alt_name_upn_allowed = response_object.get('SubjAltNameUpnAllowed')  # type: bool
            self.subj_alt_name_uri_allowed = response_object.get('SubjAltNameUriAllowed')  # type: bool
            self.subject = Certificate._LockedSubject(response_object.get('Subject'))
            self.unique_subject_enforced = response_object.get('UniqueSubjectEnforced')  # type: bool
            self.whitelisted_domains = response_object.get('WhitelistedDomains')  # type: list
            self.wildcards_allowed = response_object.get('WildcardsAllowed')  # type: bool

    class CertificateDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.c = response_object.get('C')  # type: str
            self.cn = response_object.get('CN')  # type: str
            self.enhanced_key_usage = response_object.get('EnhancedKeyUsage')  # type: str
            self.issuer = response_object.get('Issuer')  # type: str
            self.key_algorithm = response_object.get('KeyAlgorithm')  # type: str
            self.key_size = response_object.get('KeySize')  # type: int
            self.key_usage = response_object.get('KeyUsage')  # type: str
            self.l = response_object.get('L')  # type: str
            self.o = response_object.get('O')  # type: str
            self.ou = response_object.get('OU')  # type: str
            self.public_key_hash = response_object.get('PublicKeyHash')  # type: str
            self.s = response_object.get('S')  # type: str
            self.ski_key_identifier = response_object.get('SKIKeyIdentifier')  # type: str
            self.serial = response_object.get('Serial')  # type: str
            self.signature_algorithm = response_object.get('SignatureAlgorithm')  # type: str
            self.signature_algorithm_oid = response_object.get('SignatureAlgorithmOID')  # type: str
            self.store_added = response_object.get('StoreAdded')  # type: str
            self.subject = response_object.get('Subject')  # type: str
            self.subject_alt_name_dns = response_object.get('SubjectAltNameDNS')  # type: str
            self.subject_alt_name_email = response_object.get('SubjectAltNameEmail')  # type: str
            self.subject_alt_name_ip = response_object.get('SubjectAltNameIp')  # type: str
            self.subject_alt_name_upn = response_object.get('SubjectAltNameUpn')  # type: str
            self.subject_alt_name_uri = response_object.get('SubjectAltNameUri')  # type: str
            self.thumbprint = response_object.get('Thumbprint')  # type: str
            self.valid_from = from_date_string(response_object.get('ValidFrom'))
            self.valid_to = from_date_string(response_object.get('ValidTo'))

    class PreviousVersions:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.certificate_details = Certificate.CertificateDetails(response_object.get('CertificateDetails'))
            self.vault_id = response_object.get('VaultId')  # type: int

    class ProcessingDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.in_error = response_object.get('InError')  # type: bool
            self.stage = response_object.get('Stage')  # type: int
            self.status = response_object.get('Status')  # type: str

    class RenewalDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.city = response_object.get('City')  # type: str
            self.country = response_object.get('Country')  # type: str
            self.organization = response_object.get('Organization')  # type: str
            self.organizational_unit = response_object.get('OrganizationUnit')  # type: str
            self.state = response_object.get('State')  # type: str
            self.subject = response_object.get('Subject')  # type: str
            self.subject_alt_name_dns = response_object.get('SubjectAltNameDNS')  # type: str
            self.subject_alt_name_email = response_object.get('SubjectAltNameEmail')  # type: str
            self.subject_alt_name_ip_address = response_object.get('SubjectAltNameIPAddress')  # type: str
            self.subject_alt_name_other_name_upn = response_object.get('SubjectAltNameOtherNameUPN')  # type: str
            self.subject_alt_name_uri = response_object.get('SubjectAltNameURI')  # type: str
            self.valid_from = from_date_string(response_object.get('ValidFrom'))
            self.valid_to = from_date_string(response_object.get('ValidTo'))

    class ValidationDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.last_validation_state_update = response_object.get('LastValidationStateUpdate')  # type: str
            self.validation_state = response_object.get('ValidationState')  # type: str

    class SslTls:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.host = response_object.get('Host')  # type: str
            self.ip_address = response_object.get('IpAddress')  # type: str
            self.port = response_object.get('Port')  # type: int
            self.result = Certificate._SslTlsResult(response_object.get('Result'))
            self.sources = response_object.get('Sources')  # type: list

    class File:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.installation = response_object.get('Installation')  # type: str
            self.performed_on = from_date_string(response_object.get('PerformedOn'))
            self.result = response_object.get('Result')  # type: List[str]

    class _SslTlsResult:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.chain = Certificate._BitMaskValues(response_object.get('Chain'))
            self.end_entity = Certificate._BitMaskValues(response_object.get('EndEntity'))
            self.id = response_object.get('ID')  # type: int
            self.protocols = Certificate._BitMaskValues(response_object.get('Protocols'))

    class _BitMaskValues:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.bitmask = response_object.get('BitMask')  # type: int
            self.values = response_object.get('Values')  # type: List[str]

    class _SANS:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.dns = response_object.get('DNS')  # type: str
            self.ip = response_object.get('IP')  # type: str

    class _X509:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.cn = response_object.get('CN')  # type: str
            self.issuer = response_object.get('Issuer')  # type: str
            self.key_algorithm = response_object.get('KeyAlgorithm')  # type: str
            self.key_size = response_object.get('KeySize')  # type: str
            self.sans = response_object.get('SANS')  # type: str
            self.serial = response_object.get('Serial')  # type: str
            self.subject = response_object.get('Subject')  # type: str
            self.thumbprint = response_object.get('Thumbprint')  # type: str
            self.valid_from = from_date_string(response_object.get('ValidFrom'))
            self.valid_to = from_date_string(response_object.get('ValidTo'))

    class _Compliant:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
            self.compliant = response_object.get('Compliant')  # type: bool

    class _CompliantSingleValue(_Compliant):
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            super().__init__(response_object)
            self.value = response_object.get('Value')  # type: str

    class _CompliantMultiValue(_Compliant):
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            super().__init__(response_object)
            self.values = response_object.get('Values')  # type: list

    class _Locked:
        def __init__(self, response_object):
            if not isinstance(response_object, dict):
                response_object = {}

            self.locked = response_object.get('Locked')  # type: bool

    class _LockedSingleValue(_Locked):
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            super().__init__(response_object)
            self.value = response_object.get('Value')  # type: str

    class _LockedMultiValue(_Locked):
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            super().__init__(response_object)
            self.values = response_object.get('Values')  # type: list

    class _LockedKeyPair:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key_algorithm = Certificate._LockedSingleValue(response_object.get('KeyAlgorithm'))
            self.key_size = Certificate._LockedSingleValue(response_object.get('KeySize'))

    class _LockedSubject:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.city = Certificate._LockedSingleValue(response_object.get('City'))
            self.country = Certificate._LockedSingleValue(response_object.get('Country'))
            self.organization = Certificate._LockedSingleValue(response_object.get('Organization'))
            self.organizational_units = Certificate._LockedMultiValue(response_object.get('OrganizationalUnit'))
            self.state = Certificate._LockedSingleValue(response_object.get('State'))

    class _CSRDetails:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.city = Certificate._CompliantSingleValue(response_object.get('City'))
            self.common_name = Certificate._CompliantSingleValue(response_object.get('CommonName'))
            self.country = Certificate._CompliantSingleValue(response_object.get('Country'))
            self.key_algorithm = Certificate._CompliantSingleValue(response_object.get('KeyAlgorithm'))
            self.key_size = Certificate._CompliantSingleValue(response_object.get('KeySize'))
            self.organization = Certificate._CompliantSingleValue(response_object.get('Organization'))
            self.organizational_unit = Certificate._CompliantMultiValue(response_object.get('OrganizationalUnit'))
            self.private_key_reused = Certificate._CompliantSingleValue(response_object.get('PrivateKeyReused'))
            self.state = Certificate._CompliantSingleValue(response_object.get('State'))
            self.subj_alt_name_dns = Certificate._CompliantMultiValue(response_object.get('SubjAltNameDns'))
            self.subj_alt_name_email = Certificate._CompliantMultiValue(response_object.get('SubjAltNameEmail'))
            self.subj_alt_name_ip = Certificate._CompliantMultiValue(response_object.get('SubjAltNameIp'))
            self.subj_alt_name_upn = Certificate._CompliantMultiValue(response_object.get('SubjAltNameUpn'))
            self.subj_alt_name_uri = Certificate._CompliantMultiValue(response_object.get('SubjAltNameUri'))
