from venafi.properties.resultcodes import ResultCodes


class Certificate:
    class Certificate:
        def __init__(self, certificate_dict: dict):
            if not isinstance(certificate_dict, dict):
                certificate_dict = {}

            self.created_on = certificate_dict.get('CreatedOn')  # type: str
            self.dn = certificate_dict.get('DN')  # type: str
            self.guid = certificate_dict.get('Guid')  # type: str
            self.name = certificate_dict.get('Name')  # type: str
            self.parent_dn = certificate_dict.get('ParentDn')  # type: str
            self.schema_class = certificate_dict.get('SchemaClass')  # type: str
            self.x509 = Certificate._X509(certificate_dict.get('X509'))
            self.links = [Certificate.Link(link) for link in certificate_dict.get('_links', [])]

    class Link:
        def __init__(self, links_dict: dict):
            if not isinstance(links_dict, dict):
                links_dict = {}
            self.details = links_dict.get('Details')  # type: str
            self.next = links_dict.get('Next')  # type: str
            self.previous = links_dict.get('Previous')  # type: str

    class CSR:
        def __init__(self, csr_dict: dict):
            if not isinstance(csr_dict, dict):
                csr_dict = {}

            self.details = Certificate._CSRDetails(csr_dict.get('Details'))
            self.enrollable = csr_dict.get('Enrollable') # type: bool

    class Policy:
        def __init__(self, policy_dict: dict):
            if not isinstance(policy_dict, dict):
                policy_dict = {}

            self.certificate_authority = Certificate._LockedSingleValue(policy_dict.get('CertificateAuthority'))
            self.csr_generation = Certificate._LockedSingleValue(policy_dict.get('CsrGeneration'))
            self.key_generation = Certificate._LockedSingleValue(policy_dict.get('KeyGeneration'))
            self.key_pair = Certificate._LockedKeyPair(policy_dict.get('KeyPair'))
            self.management_type = Certificate._LockedSingleValue(policy_dict.get('ManagementType'))
            self.private_key_reuse_allowed = policy_dict.get('PrivateKeyReuseAllowed')  # type: bool
            self.subj_alt_name_dns_allowed = policy_dict.get('SubjAltNameDnsAllowed')  # type: bool
            self.subj_alt_name_email_allowed = policy_dict.get('SubjAltNameEmailAllowed')  # type: bool
            self.subj_alt_name_ip_allowed = policy_dict.get('SubjAltNameIpAllowed')  # type: bool
            self.subj_alt_name_upn_allowed = policy_dict.get('SubjAltNameUpnAllowed')  # type: bool
            self.subj_alt_name_uri_allowed = policy_dict.get('SubjAltNameUriAllowed')  # type: bool
            self.subject = Certificate._LockedSubject(policy_dict.get('Subject'))
            self.unique_subject_enforced = policy_dict.get('UniqueSubjectEnforced')  # type: bool
            self.whitelisted_domains = policy_dict.get('WhitelistedDomains')  # type: list
            self.wildcards_allowed = policy_dict.get('WildcardsAllowed')  # type: bool

    class CertificateDetails:
        def __init__(self, certificate_dict: dict):
            if not isinstance(certificate_dict, dict):
                certificate_dict = {}

            self.c = certificate_dict.get('C')  # type: str
            self.cn = certificate_dict.get('CN')  # type: str
            self.enhanced_key_usage = certificate_dict.get('EnhancedKeyUsage')  # type: str
            self.issuer = certificate_dict.get('Issuer')  # type: str
            self.key_algorithm = certificate_dict.get('KeyAlgorithm')  # type: str
            self.key_size = certificate_dict.get('KeySize')  # type: int
            self.key_usage = certificate_dict.get('KeyUsage')  # type: str
            self.l = certificate_dict.get('L')  # type: str
            self.o = certificate_dict.get('O')  # type: str
            self.ou = certificate_dict.get('OU')  # type: str
            self.public_key_hash = certificate_dict.get('PublicKeyHash')  # type: str
            self.s = certificate_dict.get('S')  # type: str
            self.ski_key_identifier = certificate_dict.get('SKIKeyIdentifier')  # type: str
            self.serial = certificate_dict.get('Serial')  # type: str
            self.signature_algorithm = certificate_dict.get('SignatureAlgorithm')  # type: str
            self.signature_algorithm_oid = certificate_dict.get('SignatureAlgorithmOID')  # type: str
            self.store_added = certificate_dict.get('StoreAdded')  # type: str
            self.subject = certificate_dict.get('Subject')  # type: str
            self.subject_alt_name_dns = certificate_dict.get('SubjectAltNameDNS')  # type: str
            self.subject_alt_name_email = certificate_dict.get('SubjectAltNameEmail')  # type: str
            self.subject_alt_name_ip = certificate_dict.get('SubjectAltNameIp')  # type: str
            self.subject_alt_name_upn = certificate_dict.get('SubjectAltNameUpn')  # type: str
            self.subject_alt_name_uri = certificate_dict.get('SubjectAltNameUri')  # type: str
            self.thumbprint = certificate_dict.get('Thumbprint')  # type: str
            self.valid_from = certificate_dict.get('ValidFrom')  # type: str
            self.valid_to = certificate_dict.get('ValidTo')  # type: str

    class PreviousVersions:
        def __init__(self, prev_vers_dict: dict):
            if not isinstance(prev_vers_dict, dict):
                prev_vers_dict = {}

            self.certificate_details = Certificate.CertificateDetails(prev_vers_dict.get('CertificateDetails'))
            self.vault_id = prev_vers_dict.get('VaultId')  # type: int

    class ProcessingDetails:
        def __init__(self, proc_details_dict: dict):
            if not isinstance(proc_details_dict, dict):
                proc_details_dict = {}

            self.in_error = proc_details_dict.get('InError')  # type: bool
            self.stage = proc_details_dict.get('Stage')  # type: int
            self.status = proc_details_dict.get('Status')  # type: str

    class RenewalDetails:
        def __init__(self, renewal_dict: dict):
            if not isinstance(renewal_dict, dict):
                renewal_dict = {}

            self.city = renewal_dict.get('City')  # type: str
            self.city = renewal_dict.get('Country')  # type: str
            self.city = renewal_dict.get('Organization')  # type: str
            self.city = renewal_dict.get('OrganizationUnit')  # type: str
            self.city = renewal_dict.get('State')  # type: str
            self.subject = renewal_dict.get('Subject')  # type: str
            self.subject_alt_name_dns = renewal_dict.get('SubjectAltNameDNS')  # type: str
            self.subject_alt_name_email = renewal_dict.get('SubjectAltNameEmail')  # type: str
            self.subject_alt_name_ip_address = renewal_dict.get('SubjectAltNameIPAddress')  # type: str
            self.subject_alt_name_other_name_upn = renewal_dict.get('SubjectAltNameOtherNameUPN')  # type: str
            self.subject_alt_name_uri = renewal_dict.get('SubjectAltNameURI')  # type: str
            self.valid_from = renewal_dict.get('ValidFrom')  # type: str
            self.valid_to = renewal_dict.get('ValidTo')  # type: str

    class ValidationDetails:
        def __init__(self, validation_dict: dict):
            if not isinstance(validation_dict, dict):
                validation_dict = {}

            self.last_validation_state_update = validation_dict.get('LastValidationStateUpdate')  # type: str
            self.validation_state = validation_dict.get('ValidationState')  # type: str

    class SslTls:
        def __init__(self, ssl_tls_dict: dict):
            if not isinstance(ssl_tls_dict, dict):
                ssl_tls_dict = {}

            self.host = ssl_tls_dict.get('Host')  # type: str
            self.ip_address = ssl_tls_dict.get('IpAddress')  # type: str
            self.port = ssl_tls_dict.get('Port')  # type: int
            self.result = Certificate._SslTlsResult(ssl_tls_dict.get('Result'))
            self.sources = ssl_tls_dict.get('Sources')  # type: list

    class File:
        def __init__(self, file_dict: dict):
            if not isinstance(file_dict, dict):
                file_dict = {}

            self.installation = file_dict.get('Installation')  # type: str
            self.performed_on = file_dict.get('PerformedOn')  # type: str
            self.result = file_dict.get('Result')  # type: list

    class _SslTlsResult:
        def __init__(self, results_dict: dict):
            if not isinstance(results_dict, dict):
                results_dict = {}

            self.chain = Certificate._BitMaskValues(results_dict.get('Chain'))
            self.end_entity = Certificate._BitMaskValues(results_dict.get('EndEntity'))
            self.id = results_dict.get('ID')  # type: int
            self.protocols = Certificate._BitMaskValues(results_dict.get('Protocols'))

    class _BitMaskValues:
        def __init__(self, bit_mask_dict: dict):
            if not isinstance(bit_mask_dict, dict):
                bit_mask_dict = {}

            self.bitmask = bit_mask_dict.get('BitMask')  # type: int
            self.values = bit_mask_dict.get('Values')  # type: list

    class _SANS:
        def __init__(self, sans_dict: dict, api_type: str):
            if not isinstance(sans_dict, dict):
                sans_dict = {}

            if api_type.lower() == 'websdk':
                self.dns = sans_dict.get('DNS')  # type: str
                self.ip = sans_dict.get('IP')  # type: str

            elif api_type.lower() == 'aperture':
                pass

    class _X509:
        def __init__(self, x509_dict: dict):
            if not isinstance(x509_dict, dict):
                x509_dict = {}

            self.cn = x509_dict.get('CN')  # type: str
            self.issuer = x509_dict.get('Issuer')  # type: str
            self.key_algorithm = x509_dict.get('KeyAlgorithm')  # type: str
            self.key_size = x509_dict.get('KeySize')  # type: str
            self.sans = x509_dict.get('SANS')  # type: str
            self.serial = x509_dict.get('Serial')  # type: str
            self.subject = x509_dict.get('Subject')  # type: str
            self.thumbprint = x509_dict.get('Thumbprint')  # type: str
            self.valid_from = x509_dict.get('ValidFrom')  # type: str
            self.valid_to = x509_dict.get('ValidTo')  # type: str

    class _Compliant:
        def __init__(self, comp_dict: dict):
            if not isinstance(comp_dict, dict):
                comp_dict = {}
            self.compliant = comp_dict.get('Compliant')  # type: bool

    class _CompliantSingleValue(_Compliant):
        def __init__(self, comp_dict: dict):
            if not isinstance(comp_dict, dict):
                comp_dict = {}

            super().__init__(comp_dict)
            self.value = comp_dict.get('Value')  # type: str

    class _CompliantMultiValue(_Compliant):
        def __init__(self, comp_dict: dict):
            if not isinstance(comp_dict, dict):
                comp_dict = {}

            super().__init__(comp_dict)
            self.values = comp_dict.get('Values')  # type: list

    class _Locked:
        def __init__(self, locked_dict):
            if not isinstance(locked_dict, dict):
                locked_dict = {}

            self.locked = locked_dict.get('Locked')  # type: bool

    class _LockedSingleValue(_Locked):
        def __init__(self, locked_dict: dict):
            if not isinstance(locked_dict, dict):
                locked_dict = {}

            super().__init__(locked_dict)
            self.value = locked_dict.get('Value')  # type: str

    class _LockedMultiValue(_Locked):
        def __init__(self, locked_dict: dict):
            if not isinstance(locked_dict, dict):
                locked_dict = {}

            super().__init__(locked_dict)
            self.values = locked_dict.get('Values')  # type: list

    class _LockedKeyPair:
        def __init__(self, locked_dict: dict):
            if not isinstance(locked_dict, dict):
                locked_dict = {}

            self.key_algorithm = Certificate._LockedSingleValue(locked_dict.get('KeyAlgorithm'))
            self.key_size = Certificate._LockedSingleValue(locked_dict.get('KeySize'))

    class _LockedSubject:
        def __init__(self, locked_dict: dict):
            if not isinstance(locked_dict, dict):
                locked_dict = {}

            self.city = Certificate._LockedSingleValue(locked_dict.get('City'))
            self.country = Certificate._LockedSingleValue(locked_dict.get('Country'))
            self.organization = Certificate._LockedSingleValue(locked_dict.get('Organization'))
            self.organizational_units = Certificate._LockedMultiValue(locked_dict.get('OrganizationalUnit'))
            self.state = Certificate._LockedSingleValue(locked_dict.get('State'))

    class _CSRDetails:
        def __init__(self, csr_details_dict: dict):
            if not isinstance(csr_details_dict, dict):
                csr_details_dict = {}

            self.city = Certificate._CompliantSingleValue(csr_details_dict.get('City'))
            self.common_name = Certificate._CompliantSingleValue(csr_details_dict.get('CommonName'))
            self.country = Certificate._CompliantSingleValue(csr_details_dict.get('Country'))
            self.key_algorithm = Certificate._CompliantSingleValue(csr_details_dict.get('KeyAlgorithm'))
            self.key_size = Certificate._CompliantSingleValue(csr_details_dict.get('KeySize'))
            self.organization = Certificate._CompliantSingleValue(csr_details_dict.get('Organization'))
            self.organizational_unit = Certificate._CompliantMultiValue(csr_details_dict.get('OrganizationalUnit'))
            self.private_key_reused = Certificate._CompliantSingleValue(csr_details_dict.get('PrivateKeyReused'))
            self.state = Certificate._CompliantSingleValue(csr_details_dict.get('State'))
            self.subj_alt_name_dns = Certificate._CompliantMultiValue(csr_details_dict.get('SubjAltNameDns'))
            self.subj_alt_name_email = Certificate._CompliantMultiValue(csr_details_dict.get('SubjAltNameEmail'))
            self.subj_alt_name_ip = Certificate._CompliantMultiValue(csr_details_dict.get('SubjAltNameIp'))
            self.subj_alt_name_upn = Certificate._CompliantMultiValue(csr_details_dict.get('SubjAltNameUpn'))
            self.subj_alt_name_uri = Certificate._CompliantMultiValue(csr_details_dict.get('SubjAltNameUri'))
