from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List, Literal

CertificateFormat = Literal['Base64', 'Base64 (PKCS #8)', 'DER', 'JKS', 'PKCS #7', 'PKCS #12']


class Link(PayloadModel):
    details: str = PayloadField(alias='Details')
    next: str = PayloadField(alias='Next')
    previous: str = PayloadField(alias='Previous')


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
    ou: List[str] = PayloadField(alias='OU')
    public_key_hash: str = PayloadField(alias='PublicKeyHash')
    revocation_date: datetime = PayloadField(alias='RevocationDate')
    revocation_status: str = PayloadField(alias='RevocationStatus')
    s: str = PayloadField(alias='S')
    ski_key_identifier: str = PayloadField(alias='SKIKeyIdentifier')
    serial: str = PayloadField(alias='Serial')
    signature_algorithm: str = PayloadField(alias='SignatureAlgorithm')
    signature_algorithm_oid: str = PayloadField(alias='SignatureAlgorithmOID')
    store_added: datetime = PayloadField(alias='StoreAdded')
    subject: str = PayloadField(alias='Subject')
    subject_alt_name_dns: List[str] = PayloadField(alias='SubjectAltNameDNS')
    subject_alt_name_email: List[str] = PayloadField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: List[str] = PayloadField(alias='SubjectAltNameIPAddress')
    subject_alt_name_other_name_upn: List[str] = PayloadField(alias='SubjectAltNameOtherNameUPN')
    subject_alt_name_uri: List[str] = PayloadField(alias='SubjectAltNameUri')
    template_major_version: str = PayloadField(alias='TemplateMajorVersion')
    template_minor_version: str = PayloadField(alias='TemplateMajorVersion')
    template_name: str = PayloadField(alias='TemplateName')
    template_oid: str = PayloadField(alias='TemplateOID')
    thumbprint: str = PayloadField(alias='Thumbprint')
    valid_from: datetime = PayloadField(alias='ValidFrom')
    valid_to: datetime = PayloadField(alias='ValidTo')


class PreviousVersions(PayloadModel):
    certificate_details: CertificateDetails = PayloadField(alias='CertificateDetails')
    vault_id: int = PayloadField(alias='VaultId')


class ProcessingDetails(PayloadModel):
    in_error: bool = PayloadField(alias='InError')
    stage: int = PayloadField(alias='Stage')
    status: str = PayloadField(alias='Status')


class RenewalDetails(PayloadModel):
    city: str = PayloadField(alias='City')
    country: str = PayloadField(alias='Country')
    organization: str = PayloadField(alias='Organization')
    organizational_unit: List[str] = PayloadField(alias='OrganizationalUnit')
    state: str = PayloadField(alias='State')
    subject: str = PayloadField(alias='Subject')
    subject_alt_name_dns: List[str] = PayloadField(alias='SubjectAltNameDns')
    subject_alt_name_email: List[str] = PayloadField(alias='SubjectAltNameEmail')
    subject_alt_name_ip_address: List[str] = PayloadField(alias='SubjectAltNameIpAddress')
    subject_alt_name_other_name_upn: List[str] = PayloadField(alias='SubjectAltNameOtherNameUpn')
    subject_alt_name_uri: List[str] = PayloadField(alias='SubjectAltNameUri')
    valid_from: datetime = PayloadField(alias='ValidFrom')
    valid_to: datetime = PayloadField(alias='ValidTo')


class ValidationDetails(PayloadModel):
    last_validation_state_update: str = PayloadField(alias='LastValidationStateUpdate')
    validation_state: str = PayloadField(alias='ValidationState')


class File(PayloadModel):
    installation: str = PayloadField(alias='Installation')
    performed_on: datetime = PayloadField(alias='PerformedOn')
    result: List[str] = PayloadField(alias='Result')


class BitMaskValues(PayloadModel):
    bitmask: int = PayloadField(alias='Bitmask')
    values: List[str] = PayloadField(alias='Values')


class SANS(PayloadModel):
    dns: List[str] = PayloadField(alias='Dns')
    ip: List[str] = PayloadField(alias='Ip')


class Compliant(PayloadModel):
    compliant: bool = PayloadField(alias='Compliant')


class CompliantSingleValue(Compliant):
    value: str = PayloadField(alias='Value')


class CompliantMultiValue(Compliant):
    values: List[str] = PayloadField(alias='Values')


class Locked(PayloadModel):
    locked: bool = PayloadField(alias='Locked')


class LockedSingleValue(Locked):
    value: str = PayloadField(alias='Value')


class LockedMultiValue(Locked):
    values: list = PayloadField(alias='Values')


class LockedKeyPair(PayloadModel):
    key_algorithm: LockedSingleValue = PayloadField(alias='KeyAlgorithm')
    key_size: LockedSingleValue = PayloadField(alias='KeySize')


class LockedSubject(PayloadModel):
    city: LockedSingleValue = PayloadField(alias='City')
    country: LockedSingleValue = PayloadField(alias='Country')
    organization: LockedSingleValue = PayloadField(alias='Organization')
    organizational_units: LockedMultiValue = PayloadField(alias='OrganizationalUnits')
    state: LockedSingleValue = PayloadField(alias='State')


class CSRDetails(PayloadModel):
    city: CompliantSingleValue = PayloadField(alias='City')
    common_name: CompliantSingleValue = PayloadField(alias='CommonName')
    country: CompliantSingleValue = PayloadField(alias='Country')
    key_algorithm: CompliantSingleValue = PayloadField(alias='KeyAlgorithm')
    key_size: CompliantSingleValue = PayloadField(alias='KeySize')
    organization: CompliantSingleValue = PayloadField(alias='Organization')
    organizational_unit: CompliantMultiValue = PayloadField(alias='OrganizationalUnit')
    private_key_reused: CompliantSingleValue = PayloadField(alias='PrivateKeyReused')
    state: CompliantSingleValue = PayloadField(alias='State')
    subj_alt_name_dns: CompliantMultiValue = PayloadField(alias='SubjAltNameDns')
    subj_alt_name_email: CompliantMultiValue = PayloadField(alias='SubjAltNameEmail')
    subj_alt_name_ip: CompliantMultiValue = PayloadField(alias='SubjAltNameIp')
    subj_alt_name_upn: CompliantMultiValue = PayloadField(alias='SubjAltNameUpn')
    subj_alt_name_uri: CompliantMultiValue = PayloadField(alias='SubjAltNameUri')


class NameTypeValue(PayloadModel):
    name: str = PayloadField(alias='Name')
    type: str = PayloadField(alias='Type')
    value: str = PayloadField(alias='Value')


class SslTlsResult(PayloadModel):
    chain: BitMaskValues = PayloadField(alias='Chain')
    end_entity: BitMaskValues = PayloadField(alias='EndEntity')
    id: int = PayloadField(alias='Id')
    protocols: BitMaskValues = PayloadField(alias='Protocols')


class SslTls(PayloadModel):
    host: str = PayloadField(alias='Host')
    ip_address: str = PayloadField(alias='IpAddress')
    port: int = PayloadField(alias='Port')
    result: SslTlsResult = PayloadField(alias='Result')
    sources: List[str] = PayloadField(alias='Sources')


class Policy(PayloadModel):
    certificate_authority: LockedSingleValue = PayloadField(alias='CertificateAuthority')
    csr_generation: LockedSingleValue = PayloadField(alias='CsrGeneration')
    management_type: LockedSingleValue = PayloadField(alias='ManagementType')
    key_generation: LockedSingleValue = PayloadField(alias='KeyGeneration')
    key_pair: LockedKeyPair = PayloadField(alias='KeyPair')
    private_key_reuse_allowed: bool = PayloadField(alias='PrivateKeyReuseAllowed')
    subj_alt_name_dns_allowed: bool = PayloadField(alias='SubjAltNameDnsAllowed')
    subj_alt_name_email_allowed: bool = PayloadField(alias='SubjAltNameEmailAllowed')
    subj_alt_name_ip_allowed: bool = PayloadField(alias='SubjAltNameIpAllowed')
    subj_alt_name_upn_allowed: bool = PayloadField(alias='SubjAltNameUpnAllowed')
    subj_alt_name_uri_allowed: bool = PayloadField(alias='SubjAltNameUriAllowed')
    subject: LockedSubject = PayloadField(alias='Subject')
    unique_subject_enforced: bool = PayloadField(alias='UniqueSubjectEnforced')
    whitelisted_domains: List[str] = PayloadField(alias='WhitelistedDomains')
    wildcards_allowed: bool = PayloadField(alias='WildcardsAllowed')


class CSR(PayloadModel):
    details: CSRDetails = PayloadField('Details')
    enrollable: bool = PayloadField('Enrollable')


class X509(PayloadModel):
    cn: str = PayloadField(alias='Cn')
    issuer: str = PayloadField(alias='Issuer')
    key_algorithm: str = PayloadField(alias='KeyAlgorithm')
    key_size: int = PayloadField(alias='KeySize')
    sans: SANS = PayloadField(alias='Sans')
    serial: str = PayloadField(alias='Serial')
    subject: str = PayloadField(alias='Subject')
    thumbprint: str = PayloadField(alias='Thumbprint')
    valid_from: datetime = PayloadField(alias='ValidFrom')
    valid_to: datetime = PayloadField(alias='ValidTo')


class Certificate(PayloadModel):
    created_on: datetime = PayloadField(alias='CreatedOn')
    dn: str = PayloadField(alias='DN')
    guid: str = PayloadField(alias='Guid')
    name: str = PayloadField(alias='Name')
    parent_dn: str = PayloadField(alias='ParentDn')
    schema_class: str = PayloadField(alias='SchemaClass')
    x509: X509 = PayloadField(alias='X509')
    links: List[Link] = PayloadField(alias='_links')
