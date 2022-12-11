from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class AdminCompanyDomainInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    domain: str = ApiField(alias='domain')
    emailResendingsRemaining: int = ApiField(alias='emailResendingsRemaining')
    emailSendDate: datetime = ApiField(alias='emailSendDate')
    id: UUID = ApiField(alias='id')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    status: Literal['AUTHORIZED', 'EXPIRED', 'PENDING'] = ApiField(alias='status')
    token: UUID = ApiField(alias='token')
    userId: UUID = ApiField(alias='userId')
    validationRetriesRemaining: int = ApiField(alias='validationRetriesRemaining')


class AdminCompanyDomainResponse(ObjectModel):
    companyDomains: List[AdminCompanyDomainInformation] = ApiField(alias='companyDomains', default_factory=list)


class CertificateBlockListEntryInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')


class CertificateBlockListPageResponse(ObjectModel):
    certificateBlockListEntryInformation: List[CertificateBlockListEntryInformation] = ApiField(
        alias='certificateBlockListEntryInformation', default_factory=list)
    nextPage: str = ApiField(alias='nextPage')


class CertificateBlockListRequest(ObjectModel):
    fingerprints: List[str] = ApiField(alias='fingerprints', default_factory=list)


class CertificateBlockListResponse(ObjectModel):
    certificateBlockListEntryInformation: List[CertificateBlockListEntryInformation] = ApiField(
        alias='certificateBlockListEntryInformation', default_factory=list)


class CertificateImportInformation(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    dekEncryptedPassword: str = ApiField(alias='dekEncryptedPassword')
    dekEncryptedPrivateKey: str = ApiField(alias='dekEncryptedPrivateKey')
    passwordEncryptedPrivateKey: str = ApiField(alias='passwordEncryptedPrivateKey')


class CertificateImportRequest(ObjectModel):
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    encryptionKeyId: str = ApiField(alias='encryptionKeyId')
    importInformation: List[CertificateImportInformation] = ApiField(alias='importInformation', default_factory=list)


class CertificateImportResponse(ObjectModel):
    creationDate: datetime = ApiField(alias='creationDate')
    id: str = ApiField(alias='id')


class CertificateImportStatusDetail(ObjectModel):
    certificateBytes: List[str] = ApiField(alias='certificateBytes', default_factory=list)
    fingerprint: str = ApiField(alias='fingerprint')
    reason: str = ApiField(alias='reason')
    status: Literal['FAILED', 'IMPORTED', 'PROCESSING', 'SKIPPED'] = ApiField(alias='status')


class CertificateImportStatusDetailResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    results: List[CertificateImportStatusDetail] = ApiField(alias='results', default_factory=list)
    status: Literal['COMPLETED', 'FAILED', 'PROCESSING', 'WAITING'] = ApiField(alias='status')


class CertificateInformation(ObjectModel):
    chainValidationStatus: List[Literal['CHAIN_BUILDING_FAILED', 'CHAIN_EXPIRE_BEFORE_EE', 'DISTRUSTED', 'INCOMPLETE_CHAIN',
                                        'OK', 'SELF_SIGNED', 'UNKNOWN_ERROR']] = ApiField(alias='chainValidationStatus', default_factory=list)
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='encryptionType')
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    keyStrength: int = ApiField(alias='keyStrength')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    subjectDN: str = ApiField(alias='subjectDN')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')


class CompanyDomainInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    domain: str = ApiField(alias='domain')
    emailSendDate: datetime = ApiField(alias='emailSendDate')
    id: UUID = ApiField(alias='id')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    status: Literal['AUTHORIZED', 'EXPIRED', 'PENDING'] = ApiField(alias='status')
    userId: UUID = ApiField(alias='userId')
    validationRetriesRemaining: int = ApiField(alias='validationRetriesRemaining')


class CompanyDomainRequest(ObjectModel):
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    status: Literal['AUTHORIZED', 'EXPIRED', 'PENDING'] = ApiField(alias='status')


class CompanyDomainResponse(ObjectModel):
    companyDomains: List[CompanyDomainInformation] = ApiField(alias='companyDomains', default_factory=list)


class CompanyProperty(ObjectModel):
    propertyType: str = ApiField(alias='propertyType')


class CompanyPropertyData(ObjectModel):
    propertyType: str = ApiField(alias='propertyType')


class CompanyPropertyInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: Literal['CERTIFICATE_RETIREMENT', 'PROPERTY_1', 'PROPERTY_2'] = ApiField(alias='type')
    value: CompanyProperty = ApiField(alias='value')


class CompanyPropertyRequest(ObjectModel):
    type: Literal['CERTIFICATE_RETIREMENT', 'PROPERTY_1', 'PROPERTY_2'] = ApiField(alias='type')
    value: CompanyPropertyData = ApiField(alias='value')


class CompanyPropertyResponse(ObjectModel):
    properties: List[CompanyPropertyInformation] = ApiField(alias='properties', default_factory=list)


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class ExtendedTrustedCACertificateInformation(ObjectModel):
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    certificatePolicies: List[TrustedCACertificatePolicyInformation] = ApiField(alias='certificatePolicies', default_factory=list)
    certificateType: Literal['CA', 'CROSS_CA', 'END_ENTITY', 'END_ENTITY_AC', 'ROOT_CA', 'SELF_ISSUED_CA'] = ApiField(alias='certificateType')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    crlDistributionPoints: List[str] = ApiField(alias='crlDistributionPoints', default_factory=list)
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='encryptionType')
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    issuerCertificates: List[CertificateInformation] = ApiField(alias='issuerCertificates', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerUrl: str = ApiField(alias='issuerUrl')
    keyStrength: int = ApiField(alias='keyStrength')
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    ocspUrl: str = ApiField(alias='ocspUrl')
    pathLength: int = ApiField(alias='pathLength')
    serialNumber: str = ApiField(alias='serialNumber')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    source: Literal['GLOBALLY_TRUSTED', 'USER_PROVIDED'] = ApiField(alias='source')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')
    version: int = ApiField(alias='version')


class FormDataContentDisposition(ObjectModel):
    creationDate: datetime = ApiField(alias='creationDate')
    fileName: str = ApiField(alias='fileName')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    parameters: Dict[str, str] = ApiField(alias='parameters', default_factory=dict)
    readDate: datetime = ApiField(alias='readDate')
    size: int = ApiField(alias='size')
    type: str = ApiField(alias='type')


class GeneralNamesData(ObjectModel):
    dNSName: List[str] = ApiField(alias='dNSName', default_factory=list)
    directoryName: List[str] = ApiField(alias='directoryName', default_factory=list)
    ediPartyName: List[str] = ApiField(alias='ediPartyName', default_factory=list)
    iPAddress: List[str] = ApiField(alias='iPAddress', default_factory=list)
    otherName: List[str] = ApiField(alias='otherName', default_factory=list)
    registeredID: List[str] = ApiField(alias='registeredID', default_factory=list)
    rfc822Name: List[str] = ApiField(alias='rfc822Name', default_factory=list)
    uniformResourceIdentifier: List[str] = ApiField(alias='uniformResourceIdentifier', default_factory=list)
    x400Address: List[str] = ApiField(alias='x400Address', default_factory=list)


class TrustedCACertificateDeletionRequest(ObjectModel):
    fingerprints: List[str] = ApiField(alias='fingerprints', default_factory=list)


class TrustedCACertificateInformation(ObjectModel):
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    certificatePolicies: List[TrustedCACertificatePolicyInformation] = ApiField(alias='certificatePolicies', default_factory=list)
    certificateType: Literal['CA', 'CROSS_CA', 'END_ENTITY', 'END_ENTITY_AC', 'ROOT_CA', 'SELF_ISSUED_CA'] = ApiField(alias='certificateType')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    crlDistributionPoints: List[str] = ApiField(alias='crlDistributionPoints', default_factory=list)
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='encryptionType')
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerUrl: str = ApiField(alias='issuerUrl')
    keyStrength: int = ApiField(alias='keyStrength')
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    ocspUrl: str = ApiField(alias='ocspUrl')
    pathLength: int = ApiField(alias='pathLength')
    serialNumber: str = ApiField(alias='serialNumber')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    source: Literal['GLOBALLY_TRUSTED', 'USER_PROVIDED'] = ApiField(alias='source')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')
    version: int = ApiField(alias='version')


class TrustedCACertificatePolicyInformation(ObjectModel):
    cps: str = ApiField(alias='cps')
    userNotice: List[str] = ApiField(alias='userNotice', default_factory=list)


class TrustedCACertificateResponse(ObjectModel):
    certificates: List[TrustedCACertificateInformation] = ApiField(alias='certificates', default_factory=list)
    certificatesCount: int = ApiField(alias='certificatesCount')


class TrustedCACertificatesRequest(ObjectModel):
    encodedCertificates: List[str] = ApiField(alias='encodedCertificates', default_factory=list)


class CertificateRetirementCompanyProperty(CompanyProperty):
    accessRole: Literal['ADMIN', 'EVERYONE'] = ApiField(alias='accessRole')
    custom: bool = ApiField(alias='custom')
    period: int = ApiField(alias='period')


class CertificateRetirementCompanyPropertyData(CompanyPropertyData):
    accessRole: Literal['ADMIN', 'EVERYONE'] = ApiField(alias='accessRole')
    custom: bool = ApiField(alias='custom')
    period: int = ApiField(alias='period')


AdminCompanyDomainInformation.update_forward_refs()
AdminCompanyDomainResponse.update_forward_refs()
CertificateBlockListEntryInformation.update_forward_refs()
CertificateBlockListPageResponse.update_forward_refs()
CertificateBlockListRequest.update_forward_refs()
CertificateBlockListResponse.update_forward_refs()
CertificateImportInformation.update_forward_refs()
CertificateImportRequest.update_forward_refs()
CertificateImportResponse.update_forward_refs()
CertificateImportStatusDetail.update_forward_refs()
CertificateImportStatusDetailResponse.update_forward_refs()
CertificateInformation.update_forward_refs()
CertificateRetirementCompanyProperty.update_forward_refs()
CertificateRetirementCompanyPropertyData.update_forward_refs()
CompanyDomainInformation.update_forward_refs()
CompanyDomainRequest.update_forward_refs()
CompanyDomainResponse.update_forward_refs()
CompanyProperty.update_forward_refs()
CompanyPropertyData.update_forward_refs()
CompanyPropertyInformation.update_forward_refs()
CompanyPropertyRequest.update_forward_refs()
CompanyPropertyResponse.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExtendedTrustedCACertificateInformation.update_forward_refs()
FormDataContentDisposition.update_forward_refs()
GeneralNamesData.update_forward_refs()
TrustedCACertificateDeletionRequest.update_forward_refs()
TrustedCACertificateInformation.update_forward_refs()
TrustedCACertificatePolicyInformation.update_forward_refs()
TrustedCACertificateResponse.update_forward_refs()
TrustedCACertificatesRequest.update_forward_refs()
