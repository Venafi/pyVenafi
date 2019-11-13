from enums.resultcodes import ResultCodes


class _SANS:
    def __init__(self, sans_dict: dict, api_type: str):
        if not isinstance(sans_dict, dict):
            sans_dict = {}

        if api_type.lower() == 'websdk':
            self.dns = sans_dict.get('DNS')
            self.ip = sans_dict.get('IP')

        elif api_type.lower() == 'aperture':
            pass


class _Link:
    def __init__(self, links_dict: dict):
        if not isinstance(links_dict, dict):
            links_dict = {}

        self.details = links_dict.get('Details')
        self.next = links_dict.get('Next')
        self.previous = links_dict.get('Previous')


class _X509:
    def __init__(self, x509_dict: dict):
        if not isinstance(x509_dict, dict):
            x509_dict = {}

        self.cn = x509_dict.get('CN')
        self.issuer = x509_dict.get('Issuer')
        self.key_algorithm = x509_dict.get('KeyAlgorithm')
        self.key_size = x509_dict.get('KeySize')
        self.sans = x509_dict.get('SANS')
        self.serial = x509_dict.get('Serial')
        self.subject = x509_dict.get('Subject')
        self.thumbprint = x509_dict.get('Thumbprint')
        self.valid_from = x509_dict.get('ValidFrom')
        self.valid_to = x509_dict.get('ValidTo')



class _Compliant:
    def __init__(self, comp_dict: dict):
        if not isinstance(comp_dict, dict):
            comp_dict = {}
        self.compliant = comp_dict.get('Compliant')


class _CompliantSingleValue(_Compliant):
    def __init__(self, comp_dict: dict):
        if not isinstance(comp_dict, dict):
            comp_dict = {}

        super().__init__(comp_dict)
        self.value = comp_dict.get('Value')


class _CompliantMultiValue(_Compliant):
    def __init__(self, comp_dict: dict):
        if not isinstance(comp_dict, dict):
            comp_dict = {}

        super().__init__(comp_dict)
        self.values = comp_dict.get('Values')


class _Locked:
    def __init__(self, locked_dict):
        if not isinstance(locked_dict, dict):
            locked_dict = {}

        self.locked = locked_dict.get('Locked')


class _LockedSingleValue(_Locked):
    def __init__(self, locked_dict: dict):
        if not isinstance(locked_dict, dict):
            locked_dict = {}

        super().__init__(locked_dict)
        self.value = locked_dict.get('Value')


class _LockedMultiValue(_Locked):
    def __init__(self, locked_dict: dict):
        if not isinstance(locked_dict, dict):
            locked_dict = {}

        super().__init__(locked_dict)
        self.values = locked_dict.get('Values')


class _LockedKeyPair:
    def __init__(self, locked_dict: dict):
        if not isinstance(locked_dict, dict):
            locked_dict = {}

        self.key_algorithm = _LockedSingleValue(locked_dict.get('KeyAlgorithm'))
        self.key_size = _LockedSingleValue(locked_dict.get('KeySize'))


class _LockedSubject:
    def __init__(self, locked_dict: dict):
        if not isinstance(locked_dict, dict):
            locked_dict = {}

        self.city = _LockedSingleValue(locked_dict.get('City'))
        self.country = _LockedSingleValue(locked_dict.get('Country'))
        self.organization = _LockedSingleValue(locked_dict.get('Organization'))
        self.organizational_units = _LockedMultiValue(locked_dict.get('OrganizationalUnit'))
        self.state = _LockedSingleValue(locked_dict.get('State'))


class _CSRDetails:
    def __init__(self, csr_details_dict: dict):
        if not isinstance(csr_details_dict, dict):
            csr_details_dict = {}

        self.city = _CompliantSingleValue(csr_details_dict.get('City'))
        self.common_name = _CompliantSingleValue(csr_details_dict.get('CommonName'))
        self.country = _CompliantSingleValue(csr_details_dict.get('Country'))
        self.key_algorithm = _CompliantSingleValue(csr_details_dict.get('KeyAlgorithm'))
        self.key_size = _CompliantSingleValue(csr_details_dict.get('KeySize'))
        self.organization = _CompliantSingleValue(csr_details_dict.get('Organization'))
        self.organizational_unit = _CompliantMultiValue(csr_details_dict.get('OrganizationalUnit'))
        self.private_key_reused = _CompliantSingleValue(csr_details_dict.get('PrivateKeyReused'))
        self.state = _CompliantSingleValue(csr_details_dict.get('State'))
        self.subj_alt_name_dns = _CompliantMultiValue(csr_details_dict.get('SubjAltNameDns'))
        self.subj_alt_name_email = _CompliantMultiValue(csr_details_dict.get('SubjAltNameEmail'))
        self.subj_alt_name_ip = _CompliantMultiValue(csr_details_dict.get('SubjAltNameIp'))
        self.subj_alt_name_upn = _CompliantMultiValue(csr_details_dict.get('SubjAltNameUpn'))
        self.subj_alt_name_uri = _CompliantMultiValue(csr_details_dict.get('SubjAltNameUri'))


class Certificate:
    class Certificate:
        def __init__(self, certificate_dict: dict):
            if not isinstance(certificate_dict, dict):
                certificate_dict = {}

            self.created_on = certificate_dict.get('CreatedOn')
            self.dn = certificate_dict.get('DN')
            self.guid = certificate_dict.get('Guid')
            self.name = certificate_dict.get('Name')
            self.parent_dn = certificate_dict.get('ParentDn')
            self.schema_class = certificate_dict.get('SchemaClass')
            self.x509 = _X509(certificate_dict.get('X509'))
            self.links = [_Link(link) for link in certificate_dict.get('_links', [])]

    class Link(_Link):
        def __init__(self, links_dict: dict):
            if not isinstance(links_dict, dict):
                links_dict = {}

            super().__init__(links_dict)

    class CSR:
        def __init__(self, csr_dict: dict):
            if not isinstance(csr_dict, dict):
                csr_dict = {}

            self.details = _CSRDetails(csr_dict.get('Details'))
            self.enrollable = csr_dict.get('Enrollable')

    class Policy:
        def __init__(self, policy_dict: dict):
            if not isinstance(policy_dict, dict):
                policy_dict = {}

            self.certificate_authority = _LockedSingleValue(policy_dict.get('CertificateAuthority'))
            self.csr_generation = _LockedSingleValue(policy_dict.get('CsrGeneration'))
            self.key_generation = _LockedSingleValue(policy_dict.get('KeyGeneration'))
            self.key_pair = _LockedKeyPair(policy_dict.get('KeyPair'))
            self.management_type = _LockedSingleValue(policy_dict.get('ManagementType'))
            self.private_key_reuse_allowed = policy_dict.get('PrivateKeyReuseAllowed')
            self.subj_alt_name_dns_allowed = policy_dict.get('SubjAltNameDnsAllowed')
            self.subj_alt_name_email_allowed = policy_dict.get('SubjAltNameEmailAllowed')
            self.subj_alt_name_ip_allowed = policy_dict.get('SubjAltNameIpAllowed')
            self.subj_alt_name_upn_allowed = policy_dict.get('SubjAltNameUpnAllowed')
            self.subj_alt_name_uri_allowed = policy_dict.get('SubjAltNameUriAllowed')
            self.subject = _LockedSubject(policy_dict.get('Subject'))
            self.unique_subject_enforced = policy_dict.get('UniqueSubjectEnforced')
            self.whitelisted_domains = policy_dict.get('WhitelistedDomains')
            self.wildcards_allowed = policy_dict.get('WildcardsAllowed')

    class CertificateDetails:
        def __init__(self, certificate_dict: dict):
            if not isinstance(certificate_dict, dict):
                certificate_dict = {}

            self.cn = certificate_dict.get('CN')
            self.enhanced_key_usage = certificate_dict.get('EnhancedKeyUsage')
            self.issuer = certificate_dict.get('Issuer')
            self.key_algorithm = certificate_dict.get('KeyAlgorithm')
            self.key_size = certificate_dict.get('KeySize')
            self.public_key_hash = certificate_dict.get('PublicKeyHash')
            self.serial = certificate_dict.get('Serial')
            self.signature_algorithm = certificate_dict.get('SignatureAlgorithm')
            self.signature_algorithm_oid = certificate_dict.get('SignatureAlgorithmOID')
            self.store_added = certificate_dict.get('StoreAdded')
            self.subject = certificate_dict.get('Subject')
            self.thumbprint = certificate_dict.get('Thumbprint')
            self.valid_from = certificate_dict.get('ValidFrom')
            self.valid_to = certificate_dict.get('ValidTo')

    class ProcessingDetails:
        def __init__(self, proc_details_dict: dict):
            if not isinstance(proc_details_dict, dict):
                proc_details_dict = {}

            self.in_error = proc_details_dict.get('InError')
            self.stage = proc_details_dict.get('Stage')
            self.status = proc_details_dict.get('Status')

    class RenewalDetails:
        def __init__(self, renewal_dict: dict):
            if not isinstance(renewal_dict, dict):
                renewal_dict = {}

            self.subject = renewal_dict.get('Subject')

    class ValidationDetails:
        def __init__(self, validation_dict: dict):
            if not isinstance(validation_dict, dict):
                validation_dict = {}

            self.last_validation_state_update = validation_dict.get('LastValidationStateUpdate')
            self.validation_state = validation_dict.get('ValidationState')
