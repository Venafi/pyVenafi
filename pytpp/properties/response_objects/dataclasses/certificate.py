from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Certificate(PayloadModel):
    created_on: str = PayloadField(alias='CreatedOn')
    dn: str = PayloadField(alias='DN')
    guid: str = PayloadField(alias='Guid')
    name: str = PayloadField(alias='Name')
    parent_dn: str = PayloadField(alias='ParentDn')
    schema_class: str = PayloadField(alias='SchemaClass')
    x509: '_X509' = PayloadField(alias='X509')
    links: 'List[Link]' = PayloadField(alias='_links')


class Link(PayloadModel):
    details: str = PayloadField(alias='Details')
    next: str = PayloadField(alias='Next')
    previous: str = PayloadField(alias='Previous')


class CSR(PayloadModel):
    details: '_CSRDetails' = PayloadField('Details')
    enrollable: bool = PayloadField('Enrollable')


class Policy(PayloadModel):
    certificate_authority: '_LockedSingleValue' = PayloadField(alias='CertificateAuthority')
    csr_generation: '_LockedSingleValue' = PayloadField(alias='CsrGeneration')
    management_type: '_LockedSingleValue' = PayloadField(alias='ManagementType')
    key_generation: '_LockedSingleValue' = PayloadField(alias='KeyGeneration')
    key_pair: '_LockedKeyPair' = PayloadField(alias='KeyPair')
    private_key_reuse_allowed: bool = PayloadField(alias='PrivateKeyReuseAllowed')
    subj_alt_name_dns_allowed: bool = PayloadField(alias='SubjAltNameDnsAllowed')
    subj_alt_name_email_allowed: bool = PayloadField(alias='SubjAltNameEmailAllowed')
    subj_alt_name_ip_allowed: bool = PayloadField(alias='SubjAltNameIpAllowed')
    subj_alt_name_upn_allowed: bool = PayloadField(alias='SubjAltNameUpnAllowed')
    subj_alt_name_uri_allowed: bool = PayloadField(alias='SubjAltNameUriAllowed')
    subject: '_LockedSubject' = PayloadField(alias='Subject')
    unique_subject_enforced: bool = PayloadField(alias='UniqueSubjectEnforced')
    whitelisted_domains: list = PayloadField(alias='WhitelistedDomains')
    wildcards_allowed: bool = PayloadField(alias='WildcardsAllowed')


class CertificateDetails(PayloadModel):
    aia_ca_issuer_url: List[str] = PayloadField(alias='AIACAIssuerURL')
    aia_key_identifier: str = PayloadField(alias='AIAKeyIdentifier')
    c: str = PayloadField(alias='C')
    cdp_uri: str = PayloadField(alias='CDPURI')
    cn: str = PayloadField(alias='CN')
    elliptic_curve: str = PayloadField(alias='EllipticCurve')
    enhanced_key_usage: str = PayloadField(alias='EnhancedKeyUsage')
    issuer: str = PayloadField(alias='Issuer')
    key_algorithm: str = PayloadField(alias='KeyAlgorithm')
    key_size: int = PayloadField(alias='KeySize')
    key_usage: str = PayloadField(alias='KeyUsage')
    l: str = PayloadField(alias='L')
    o: str = PayloadField(alias='O')
    ou: str = PayloadField(alias='OU')
    public_key_hash: str = PayloadField(alias='PublicKeyHash')
    revocation_date: 'datetime' = PayloadField(alias='RevocationDate')
    revocation_status: 'datetime' = PayloadField(alias='RevocationStatus')
    s: str = PayloadField(alias='S')
    ski_key_identifier: str = PayloadField(alias='SKIKeyIdentifier')
    serial: str = PayloadField(alias='Serial')
    signature_algorithm: str = PayloadField(alias='SignatureAlgorithm')
    signature_algorithm_oid: str = PayloadField(alias='SignatureAlgorithmOID')
    store_added: str = PayloadField(alias='StoreAdded')
    subject: str = PayloadField(alias='Subject')
    subject_alt_name_dns: str = PayloadField(alias='SubjectAltNameDNS')
    subject_alt_name_email: str = PayloadField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: str = PayloadField(alias='SubjectAltNameIPAddress')
    subject_alt_name_other_name_upn: str = PayloadField(alias='SubjectAltNameOtherNameUPN')
    subject_alt_name_uri: str = PayloadField(alias='SubjectAltNameUri')
    template_major_version: str = PayloadField(alias='TemplateMajorVersion')
    template_minor_version: str = PayloadField(alias='TemplateMajorVersion')
    template_name: str = PayloadField(alias='TemplateName')
    template_oid: str = PayloadField(alias='TemplateOID')
    thumbprint: str = PayloadField(alias='Thumbprint')
    valid_from: 'datetime' = PayloadField(alias='ValidFrom')
    valid_to: 'datetime' = PayloadField(alias='ValidTo')


class PreviousVersions(PayloadModel):
    certificate_details: 'CertificateDetails' = PayloadField(alias='CertificateDetails')
    vault_id: int = PayloadField(alias='VaultId')


class ProcessingDetails(PayloadModel):
    in_error: bool = PayloadField(alias='InError')
    stage: int = PayloadField(alias='Stage')
    status: str = PayloadField(alias='Status')


class RenewalDetails(PayloadModel):
    city: str = PayloadField(alias='City')
    country: str = PayloadField(alias='Country')
    organization: str = PayloadField(alias='Organization')
    organizational_unit: str = PayloadField(alias='OrganizationalUnit')
    state: str = PayloadField(alias='State')
    subject: str = PayloadField(alias='Subject')
    subject_alt_name_dns: str = PayloadField(alias='SubjectAltNameDns')
    subject_alt_name_email: str = PayloadField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: str = PayloadField(alias='SubjectAltNameIpAddress')
    subject_alt_name_other_name_upn: str = PayloadField(alias='SubjectAltNameOtherNameUpn')
    subject_alt_name_uri: str = PayloadField(alias='SubjectAltNameUri')
    valid_from: 'datetime' = PayloadField(alias='ValidFrom')
    valid_to: 'datetime' = PayloadField(alias='ValidTo')


class ValidationDetails(PayloadModel):
    last_validation_state_update: str = PayloadField(alias='LastValidationStateUpdate')
    validation_state: str = PayloadField(alias='ValidationState')


class SslTls(PayloadModel):
    host: str = PayloadField(alias='Host')
    ip_address: str = PayloadField(alias='IpAddress')
    port: int = PayloadField(alias='Port')
    result: '_SslTlsResult' = PayloadField(alias='Result')
    sources: list = PayloadField(alias='Sources')


class File(PayloadModel):
    installation: str = PayloadField(alias='Installation')
    performed_on: 'datetime' = PayloadField(alias='PerformedOn')
    result: List[str] = PayloadField(alias='Result')


class _SslTlsResult(PayloadModel):
    chain: '_BitMaskValues' = PayloadField(alias='Chain')
    end_entity: '_BitMaskValues' = PayloadField(alias='EndEntity')
    id: int = PayloadField(alias='Id')
    protocols: '_BitMaskValues' = PayloadField(alias='Protocols')


class _BitMaskValues(PayloadModel):
    bitmask: int = PayloadField(alias='Bitmask')
    values: List[str] = PayloadField(alias='Values')


class _SANS(PayloadModel):
    dns: str = PayloadField(alias='Dns')
    ip: str = PayloadField(alias='Ip')


class _X509(PayloadModel):
    cn: str = PayloadField(alias='Cn')
    issuer: str = PayloadField(alias='Issuer')
    key_algorithm: str = PayloadField(alias='KeyAlgorithm')
    key_size: str = PayloadField(alias='KeySize')
    sans: str = PayloadField(alias='Sans')
    serial: str = PayloadField(alias='Serial')
    subject: str = PayloadField(alias='Subject')
    thumbprint: str = PayloadField(alias='Thumbprint')
    valid_from: 'datetime' = PayloadField(alias='ValidFrom')
    valid_to: 'datetime' = PayloadField(alias='ValidTo')


class _Compliant(PayloadModel):
    compliant: bool = PayloadField(alias='Compliant')


class _CompliantSingleValue(_Compliant):
    value: str = PayloadField(alias='Value')


class _CompliantMultiValue(_Compliant):
    values: list = PayloadField(alias='Values')


class _Locked(PayloadModel):
    locked: bool = PayloadField(alias='Locked')


class _LockedSingleValue(_Locked):
    value: str = PayloadField(alias='Value')


class _LockedMultiValue(_Locked):
    values: list = PayloadField(alias='Values')


class _LockedKeyPair(PayloadModel):
    key_algorithm: '_LockedSingleValue' = PayloadField(alias='KeyAlgorithm')
    key_size: '_LockedSingleValue' = PayloadField(alias='KeySize')


class _LockedSubject(PayloadModel):
    city: '_LockedSingleValue' = PayloadField(alias='City')
    country: '_LockedSingleValue' = PayloadField(alias='Country')
    organization: '_LockedSingleValue' = PayloadField(alias='Organization')
    organizational_units: '_LockedMultiValue' = PayloadField(alias='OrganizationalUnits')
    state: '_LockedSingleValue' = PayloadField(alias='State')


class _CSRDetails(PayloadModel):
    city: '_CompliantSingleValue' = PayloadField(alias='City')
    common_name: '_CompliantSingleValue' = PayloadField(alias='CommonName')
    country: '_CompliantSingleValue' = PayloadField(alias='Country')
    key_algorithm: '_CompliantSingleValue' = PayloadField(alias='KeyAlgorithm')
    key_size: '_CompliantSingleValue' = PayloadField(alias='KeySize')
    organization: '_CompliantSingleValue' = PayloadField(alias='Organization')
    organizational_unit: '_CompliantMultiValue' = PayloadField(alias='OrganizationalUnit')
    private_key_reused: '_CompliantSingleValue' = PayloadField(alias='PrivateKeyReused')
    state: '_CompliantSingleValue' = PayloadField(alias='State')
    subj_alt_name_dns: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameDns')
    subj_alt_name_email: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameEmail')
    subj_alt_name_ip: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameIp')
    subj_alt_name_upn: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameUpn')
    subj_alt_name_uri: '_CompliantMultiValue' = PayloadField(alias='SubjAltNameUri')
