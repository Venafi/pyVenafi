from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Certificate(PayloadModel):
    created_on: str = PayloadField(alias='CreatedOn', default=None)
    dn: str = PayloadField(alias='DN', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    name: str = PayloadField(alias='Name', default=None)
    parent_dn: str = PayloadField(alias='ParentDn', default=None)
    schema_class: str = PayloadField(alias='SchemaClass', default=None)
    x509: '_X509' = PayloadField(alias='X509', default=None)
    links: 'List[Link]' = PayloadField(alias='_links', default=None)


class Link(PayloadModel):
    details: str = PayloadField(alias='Details', default=None)
    next: str = PayloadField(alias='Next', default=None)
    previous: str = PayloadField(alias='Previous', default=None)


class CSR(PayloadModel):
    details: '_CSRDetails' = PayloadField('Details')
    enrollable: bool = PayloadField('Enrollable')


class Policy(PayloadModel):
    certificate_authority: '_LockedSingleValue' = PayloadField(alias='CertificateAuthority', default=None)
    csr_generation: '_LockedSingleValue' = PayloadField(alias='CsrGeneration', default=None)
    management_type: '_LockedSingleValue' = PayloadField(alias='ManagementType', default=None)
    key_generation: '_LockedSingleValue' = PayloadField(alias='KeyGeneration', default=None)
    key_pair: '_LockedKeyPair' = PayloadField(alias='KeyPair', default=None)
    private_key_reuse_allowed: bool = PayloadField(alias='PrivateKeyReuseAllowed', default=None)
    subj_alt_name_dns_allowed: bool = PayloadField(alias='SubjAltNameDnsAllowed', default=None)
    subj_alt_name_email_allowed: bool = PayloadField(alias='SubjAltNameEmailAllowed', default=None)
    subj_alt_name_ip_allowed: bool = PayloadField(alias='SubjAltNameIpAllowed', default=None)
    subj_alt_name_upn_allowed: bool = PayloadField(alias='SubjAltNameUpnAllowed', default=None)
    subj_alt_name_uri_allowed: bool = PayloadField(alias='SubjAltNameUriAllowed', default=None)
    subject: '_LockedSubject' = PayloadField(alias='Subject', default=None)
    unique_subject_enforced: bool = PayloadField(alias='UniqueSubjectEnforced', default=None)
    whitelisted_domains: list = PayloadField(alias='WhitelistedDomains', default=None)
    wildcards_allowed: bool = PayloadField(alias='WildcardsAllowed', default=None)


class CertificateDetails(PayloadModel):
    aia_ca_issuer_url: List[str] = PayloadField(alias='AIACAIssuerURL', default=None)
    aia_key_identifier: str = PayloadField(alias='AIAKeyIdentifier', default=None)
    c: str = PayloadField(alias='C', default=None)
    cdp_uri: str = PayloadField(alias='CDPURI', default=None)
    cn: str = PayloadField(alias='CN', default=None)
    elliptic_curve: str = PayloadField(alias='EllipticCurve', default=None)
    enhanced_key_usage: str = PayloadField(alias='EnhancedKeyUsage', default=None)
    issuer: str = PayloadField(alias='Issuer', default=None)
    key_algorithm: str = PayloadField(alias='KeyAlgorithm', default=None)
    key_size: int = PayloadField(alias='KeySize', default=None)
    key_usage: str = PayloadField(alias='KeyUsage', default=None)
    l: str = PayloadField(alias='L', default=None)
    o: str = PayloadField(alias='O', default=None)
    ou: str = PayloadField(alias='OU', default=None)
    public_key_hash: str = PayloadField(alias='PublicKeyHash', default=None)
    revocation_date: 'datetime' = PayloadField(alias='RevocationDate', default=None)
    revocation_status: 'datetime' = PayloadField(alias='RevocationStatus', default=None)
    s: str = PayloadField(alias='S', default=None)
    ski_key_identifier: str = PayloadField(alias='SKIKeyIdentifier', default=None)
    serial: str = PayloadField(alias='Serial', default=None)
    signature_algorithm: str = PayloadField(alias='SignatureAlgorithm', default=None)
    signature_algorithm_oid: str = PayloadField(alias='SignatureAlgorithmOID', default=None)
    store_added: str = PayloadField(alias='StoreAdded', default=None)
    subject: str = PayloadField(alias='Subject', default=None)
    subject_alt_name_dns: str = PayloadField(alias='SubjectAltNameDNS', default=None)
    subject_alt_name_email: str = PayloadField(alias='SubjectAltNameEmail', default=None)
    subject_alt_name_ip_address: str = PayloadField(alias='SubjectAltNameIPAddress', default=None)
    subject_alt_name_other_name_upn: str = PayloadField(alias='SubjectAltNameOtherNameUPN', default=None)
    subject_alt_name_uri: str = PayloadField(alias='SubjectAltNameUri', default=None)
    template_major_version: str = PayloadField(alias='TemplateMajorVersion', default=None)
    template_minor_version: str = PayloadField(alias='TemplateMajorVersion', default=None)
    template_name: str = PayloadField(alias='TemplateName', default=None)
    template_oid: str = PayloadField(alias='TemplateOID', default=None)
    thumbprint: str = PayloadField(alias='Thumbprint', default=None)
    valid_from: 'datetime' = PayloadField(alias='ValidFrom', default=None)
    valid_to: 'datetime' = PayloadField(alias='ValidTo', default=None)


class PreviousVersions(PayloadModel):
    certificate_details: 'CertificateDetails' = PayloadField(alias='CertificateDetails', default=None)
    vault_id: int = PayloadField(alias='VaultId', default=None)


class ProcessingDetails(PayloadModel):
    in_error: bool = PayloadField(alias='InError', default=None)
    stage: int = PayloadField(alias='Stage', default=None)
    status: str = PayloadField(alias='Status', default=None)


class RenewalDetails(PayloadModel):
    city: str = PayloadField(alias='City', default=None)
    country: str = PayloadField(alias='Country', default=None)
    organization: str = PayloadField(alias='Organization', default=None)
    organizational_unit: str = PayloadField(alias='OrganizationalUnit', default=None)
    state: str = PayloadField(alias='State', default=None)
    subject: str = PayloadField(alias='Subject', default=None)
    subject_alt_name_dns: str = PayloadField(alias='SubjectAltNameDns', default=None)
    subject_alt_name_email: str = PayloadField(alias='SubjectAltNameEmail', default=None)
    subject_alt_name_ip_address: str = PayloadField(alias='SubjectAltNameIpAddress', default=None)
    subject_alt_name_other_name_upn: str = PayloadField(alias='SubjectAltNameOtherNameUpn', default=None)
    subject_alt_name_uri: str = PayloadField(alias='SubjectAltNameUri', default=None)
    valid_from: 'datetime' = PayloadField(alias='ValidFrom', default=None)
    valid_to: 'datetime' = PayloadField(alias='ValidTo', default=None)


class ValidationDetails(PayloadModel):
    last_validation_state_update: str = PayloadField(alias='LastValidationStateUpdate', default=None)
    validation_state: str = PayloadField(alias='ValidationState', default=None)


class SslTls(PayloadModel):
    host: str = PayloadField(alias='Host', default=None)
    ip_address: str = PayloadField(alias='IpAddress', default=None)
    port: int = PayloadField(alias='Port', default=None)
    result: '_SslTlsResult' = PayloadField(alias='Result', default=None)
    sources: list = PayloadField(alias='Sources', default=None)


class File(PayloadModel):
    installation: str = PayloadField(alias='Installation', default=None)
    performed_on: 'datetime' = PayloadField(alias='PerformedOn', default=None)
    result: List[str] = PayloadField(alias='Result', default=None)


class _SslTlsResult(PayloadModel):
    chain: '_BitMaskValues' = PayloadField(alias='Chain', default=None)
    end_entity: '_BitMaskValues' = PayloadField(alias='EndEntity', default=None)
    id: int = PayloadField(alias='Id', default=None)
    protocols: '_BitMaskValues' = PayloadField(alias='Protocols', default=None)


class _BitMaskValues(PayloadModel):
    bitmask: int = PayloadField(alias='Bitmask', default=None)
    values: List[str] = PayloadField(alias='Values', default=None)


class _SANS(PayloadModel):
    dns: str = PayloadField(alias='Dns', default=None)
    ip: str = PayloadField(alias='Ip', default=None)


class _X509(PayloadModel):
    cn: str = PayloadField(alias='Cn', default=None)
    issuer: str = PayloadField(alias='Issuer', default=None)
    key_algorithm: str = PayloadField(alias='KeyAlgorithm', default=None)
    key_size: str = PayloadField(alias='KeySize', default=None)
    sans: str = PayloadField(alias='Sans', default=None)
    serial: str = PayloadField(alias='Serial', default=None)
    subject: str = PayloadField(alias='Subject', default=None)
    thumbprint: str = PayloadField(alias='Thumbprint', default=None)
    valid_from: 'datetime' = PayloadField(alias='ValidFrom', default=None)
    valid_to: 'datetime' = PayloadField(alias='ValidTo', default=None)


class _Compliant(PayloadModel):
    compliant: bool = PayloadField(alias='Compliant', default=None)


class _CompliantSingleValue(_Compliant):
    value: str = PayloadField(alias='Value', default=None)


class _CompliantMultiValue(_Compliant):
    values: list = PayloadField(alias='Values', default=None)


class _Locked(PayloadModel):
    locked: bool = PayloadField(alias='Locked', default=None)


class _LockedSingleValue(_Locked):
    value: str = PayloadField(alias='Value', default=None)


class _LockedMultiValue(_Locked):
    values: list = PayloadField(alias='Values', default=None)


class _LockedKeyPair(PayloadModel):
    key_algorithm: '_LockedSingleValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_size: '_LockedSingleValue' = PayloadField(alias='KeySize', default=None)


class _LockedSubject(PayloadModel):
    city: '_LockedSingleValue' = PayloadField(alias='City', default=None)
    country: '_LockedSingleValue' = PayloadField(alias='Country', default=None)
    organization: '_LockedSingleValue' = PayloadField(alias='Organization', default=None)
    organizational_units: '_LockedMultiValue' = PayloadField(alias='OrganizationalUnits', default=None)
    state: '_LockedSingleValue' = PayloadField(alias='State', default=None)


class _CSRDetails(PayloadModel):
    city: '_CompliantSingleValue' = PayloadField(alias='City', default=None)
    common_name: '_CompliantSingleValue' = PayloadField(alias='CommonName', default=None)
    country: '_CompliantSingleValue' = PayloadField(alias='Country', default=None)
    key_algorithm: '_CompliantSingleValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_size: '_CompliantSingleValue' = PayloadField(alias='KeySize', default=None)
    organization: '_CompliantSingleValue' = PayloadField(alias='Organization', default=None)
    organizational_unit: '_CompliantMultiValue' = PayloadField(alias='OrganizationalUnit', default=None)
    private_key_reused: '_CompliantSingleValue' = PayloadField(alias='PrivateKeyReused', default=None)
    state: '_CompliantSingleValue' = PayloadField(alias='State', default=None)
    subj_alt_name_dns: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameDns', default=None)
    subj_alt_name_email: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameEmail', default=None)
    subj_alt_name_ip: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameIp', default=None)
    subj_alt_name_upn: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameUpn', default=None)
    subj_alt_name_uri: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameUri', default=None)
