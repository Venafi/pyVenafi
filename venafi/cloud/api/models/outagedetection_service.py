from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from uuid import UUID
from typing import (Any, Dict, List, Literal)
from datetime import datetime


class ApiClientInformation(ObjectModel):
    type: str = ApiField(alias='type')
    identifier: str = ApiField(alias='identifier')


class ApplicationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    name: str = ApiField(alias='name')
    description: str = ApiField(alias='description')
    ownerIdsAndTypes: List[OwnerIdAndType] = ApiField(alias='ownerIdsAndTypes', default_factory=list)
    owningUsers: List[UserInformation] = ApiField(alias='owningUsers', default_factory=list)
    owningTeams: List[TeamInformation] = ApiField(alias='owningTeams', default_factory=list)
    fullyQualifiedDomainNames: List[str] = ApiField(alias='fullyQualifiedDomainNames', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    certificateIssuingTemplateAliasIdMap: Dict[str, UUID] = ApiField(alias='certificateIssuingTemplateAliasIdMap', default_factory=dict)
    ownership: DefaultOwnershipInformation = ApiField(alias='ownership')


class ApplicationRequest(ObjectModel):
    name: str = ApiField(alias='name')
    ownerIdsAndTypes: List[OwnerIdAndType] = ApiField(alias='ownerIdsAndTypes', default_factory=list)
    description: str = ApiField(alias='description')
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    internalFqdns: List[str] = ApiField(alias='internalFqdns', default_factory=list)
    internalIpRanges: List[str] = ApiField(alias='internalIpRanges', default_factory=list)
    externalIpRanges: List[str] = ApiField(alias='externalIpRanges', default_factory=list)
    internalPorts: List[str] = ApiField(alias='internalPorts', default_factory=list)
    fullyQualifiedDomainNames: List[str] = ApiField(alias='fullyQualifiedDomainNames', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    certificateIssuingTemplateAliasIdMap: Dict[str, UUID] = ApiField(alias='certificateIssuingTemplateAliasIdMap', default_factory=dict)
    startTargetedDiscovery: bool = ApiField(alias='startTargetedDiscovery')


class ApplicationResponse(ObjectModel):
    applications: List[ApplicationInformation] = ApiField(alias='applications', default_factory=list)
    totalCount: int = ApiField(alias='totalCount')
    ownershipCount: int = ApiField(alias='ownershipCount')


class ApplicationServerTypeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    keyStoreType: Literal['JKS', 'PEM', 'PKCS12'] = ApiField(alias='keyStoreType')
    applicationServerType: Literal['APACHE', 'CITRIX', 'F5', 'IIS', 'JETTY',
                                   'NGINX', 'OTHER', 'TOMCAT'] = ApiField(alias='applicationServerType')
    platformName: str = ApiField(alias='platformName')


class ApplicationServerTypeResponse(ObjectModel):
    applicationServerTypes: List[ApplicationServerTypeInformation] = ApiField(alias='applicationServerTypes', default_factory=list)


class ApplicationsAssignRequest(ObjectModel):
    action: Literal['ADD', 'DELETE', 'DELETE_ALL', 'REPLACE'] = ApiField(alias='action')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    targetedApplicationIds: List[UUID] = ApiField(alias='targetedApplicationIds', default_factory=list)


class ApplicationsAssignResponse(ObjectModel):
    certificates: List[CertificateInformation] = ApiField(alias='certificates', default_factory=list)


class BaseApplicationServerTypeRequest(ObjectModel):
    applicationServerType: Literal['APACHE', 'CITRIX', 'F5', 'IIS', 'JETTY',
                                   'NGINX', 'OTHER', 'TOMCAT'] = ApiField(alias='applicationServerType')
    platformName: str = ApiField(alias='platformName')
    keyStoreType: Literal['JKS', 'PEM', 'PKCS12'] = ApiField(alias='keyStoreType')


class CSRAttributesInformation(ObjectModel):
    commonName: str = ApiField(alias='commonName')
    organization: str = ApiField(alias='organization')
    organizationalUnits: List[str] = ApiField(alias='organizationalUnits', default_factory=list)
    locality: str = ApiField(alias='locality')
    state: str = ApiField(alias='state')
    country: str = ApiField(alias='country')
    subjectAlternativeNamesByType: SubjectAlternativeNamesByType = ApiField(alias='subjectAlternativeNamesByType')
    keyTypeParameters: KeyTypeParameters = ApiField(alias='keyTypeParameters')


class CertificateAggregatesRangeResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    certificateAggregatesMap: Dict[str, int] = ApiField(alias='certificateAggregatesMap', default_factory=dict)


class CertificateAggregatesResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    certificateAggregatesMap: Dict[str, CertificateCategoryInformation] = ApiField(alias='certificateAggregatesMap', default_factory=dict)


class CertificateAggregationsRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    facet: Facet = ApiField(alias='facet')
    includeRetired: bool = ApiField(alias='includeRetired')


class CertificateCategoryInformation(ObjectModel):
    certificatesCount: int = ApiField(alias='certificatesCount')
    certificateCategoryAggregatesMap: Dict[str, int] = ApiField(alias='certificateCategoryAggregatesMap', default_factory=dict)


class CertificateDeletionRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)


class CertificateImportInfo(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    issuerCertificates: List[str] = ApiField(alias='issuerCertificates', default_factory=list)
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(alias='certificateUsageMetadata', default_factory=list)


class CertificateImportRequest(ObjectModel):
    certificates: List[CertificateImportInfo] = ApiField(alias='certificates', default_factory=list)
    overrideBlocklist: bool = ApiField(alias='overrideBlocklist')


class CertificateImportResponse(ObjectModel):
    certificateInformations: List[ImportedCertificateInformation] = ApiField(alias='certificateInformations', default_factory=list)
    statistics: Dict[str, int] = ApiField(alias='statistics', default_factory=dict)


class CertificateInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')
    certificateRequestId: UUID = ApiField(alias='certificateRequestId')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    fingerprint: str = ApiField(alias='fingerprint')
    certificateName: str = ApiField(alias='certificateName')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    certificateStatus: Literal['ACTIVE', 'DELETED', 'RETIRED'] = ApiField(alias='certificateStatus')
    statusModificationUserId: UUID = ApiField(alias='statusModificationUserId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    archivedDate: datetime = ApiField(alias='archivedDate')
    statusModificationDate: datetime = ApiField(alias='statusModificationDate')
    validityStart: datetime = ApiField(alias='validityStart')
    validityEnd: datetime = ApiField(alias='validityEnd')
    selfSigned: bool = ApiField(alias='selfSigned')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='encryptionType')
    keyStrength: int = ApiField(alias='keyStrength')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    serialNumber: str = ApiField(alias='serialNumber')
    subjectDN: str = ApiField(alias='subjectDN')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: List[str] = ApiField(alias='subjectOU', default_factory=list)
    subjectST: str = ApiField(alias='subjectST')
    subjectL: str = ApiField(alias='subjectL')
    subjectC: str = ApiField(alias='subjectC')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectAlternativeNameDns: List[str] = ApiField(alias='subjectAlternativeNameDns', default_factory=list)
    subjectAlternativeNameNonDns: List[str] = ApiField(alias='subjectAlternativeNameNonDns', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerCN: List[str] = ApiField(alias='issuerCN', default_factory=list)
    issuerOU: List[str] = ApiField(alias='issuerOU', default_factory=list)
    issuerST: str = ApiField(alias='issuerST')
    issuerL: str = ApiField(alias='issuerL')
    issuerC: str = ApiField(alias='issuerC')
    issuerAlternativeNameDns: List[str] = ApiField(alias='issuerAlternativeNameDns', default_factory=list)
    issuerAlternativeNameNonDns: List[str] = ApiField(alias='issuerAlternativeNameNonDns', default_factory=list)
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    pathLength: int = ApiField(alias='pathLength')
    ocspNoCheck: bool = ApiField(alias='ocspNoCheck')
    requireExplicitPolicy: int = ApiField(alias='requireExplicitPolicy')
    inhibitPolicyMapping: int = ApiField(alias='inhibitPolicyMapping')
    inhibitAnyPolicy: int = ApiField(alias='inhibitAnyPolicy')
    versionType: Literal['CURRENT', 'OLD'] = ApiField(alias='versionType')
    totalInstanceCount: int = ApiField(alias='totalInstanceCount')
    totalActiveInstanceCount: int = ApiField(alias='totalActiveInstanceCount')
    instances: List[CertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)
    dekHash: str = ApiField(alias='dekHash')
    applicationServerTypeId: UUID = ApiField(alias='applicationServerTypeId')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    ownership: DefaultOwnershipInformation = ApiField(alias='ownership')


class CertificateInstallationsUsageResponse(ObjectModel):
    count: int = ApiField(alias='count')


class CertificateInstanceInformation(ObjectModel):
    certificateInstanceId: UUID = ApiField(alias='certificateInstanceId')
    certificateId: UUID = ApiField(alias='certificateId')
    certificateSource: Literal['DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'ON_PREM_CA_IMPORT', 'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL',
                               'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(alias='certificateSource')
    ipAddress: str = ApiField(alias='ipAddress')
    hostname: str = ApiField(alias='hostname')
    port: int = ApiField(alias='port')
    instanceChainValidationStatus: List[Literal['CHAIN_BUILDING_FAILED', 'CHAIN_EXPIRE_BEFORE_EE', 'DISTRUSTED', 'INCOMPLETE_CHAIN',
                                                'OK', 'SELF_SIGNED', 'UNKNOWN_ERROR']] = ApiField(alias='instanceChainValidationStatus', default_factory=list)
    sslValidationStatus: Literal['HOSTNAME_NOT_RESOLVABLE', 'INVALID_CERTIFICATE_FOUND', 'NO_CERTIFICATE_PRESENTED', 'OK',
                                 'OLD_VERSION_CERTIFICATE_FOUND', 'TARGET_UNREACHABLE', 'UNEXPECTED_CERTIFICATE_FOUND', 'UNKNOWN_ERROR'] = ApiField(alias='sslValidationStatus')
    sslValidationStatusMessage: str = ApiField(alias='sslValidationStatusMessage')
    sslValidationErrorArguments: List[str] = ApiField(alias='sslValidationErrorArguments', default_factory=list)
    sslProtocols: List[str] = ApiField(alias='sslProtocols', default_factory=list)
    lastScanDate: datetime = ApiField(alias='lastScanDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    serviceIds: List[UUID] = ApiField(alias='serviceIds', default_factory=list)
    deploymentStatus: Literal['IN_USE', 'SUPERSEDED', 'UNKNOWN'] = ApiField(alias='deploymentStatus')


class CertificateInstanceSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class CertificateInstanceValidationRequest(ObjectModel):
    instanceIds: List[UUID] = ApiField(alias='instanceIds', default_factory=list)


class CertificateIssuingTemplateInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    name: str = ApiField(alias='name')
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    priority: int = ApiField(alias='priority')
    systemGenerated: bool = ApiField(alias='systemGenerated')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['AVAILABLE', 'UNAVAILABLE'] = ApiField(alias='status')
    reason: str = ApiField(alias='reason')
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectORegexes: List[str] = ApiField(alias='subjectORegexes', default_factory=list)
    subjectOURegexes: List[str] = ApiField(alias='subjectOURegexes', default_factory=list)
    subjectSTRegexes: List[str] = ApiField(alias='subjectSTRegexes', default_factory=list)
    subjectLRegexes: List[str] = ApiField(alias='subjectLRegexes', default_factory=list)
    subjectCValues: List[str] = ApiField(alias='subjectCValues', default_factory=list)
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    sanDnsNameRegexes: List[str] = ApiField(alias='sanDnsNameRegexes', default_factory=list)
    sanRfc822NameRegexes: List[str] = ApiField(alias='sanRfc822NameRegexes', default_factory=list)
    sanIpAddressRegexes: List[str] = ApiField(alias='sanIpAddressRegexes', default_factory=list)
    sanUniformResourceIdentifierRegexes: List[str] = ApiField(alias='sanUniformResourceIdentifierRegexes', default_factory=list)
    keyTypes: List[KeyTypeInformation] = ApiField(alias='keyTypes', default_factory=list)
    keyReuse: bool = ApiField(alias='keyReuse')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    keyGeneratedByVenafiAllowed: bool = ApiField(alias='keyGeneratedByVenafiAllowed')
    recommendedSettings: RecommendedSettingsInformation = ApiField(alias='recommendedSettings')
    productEntitlement: Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(alias='productEntitlement')
    resourceConsumerUserIds: List[UUID] = ApiField(alias='resourceConsumerUserIds', default_factory=list)
    resourceConsumerTeamIds: List[UUID] = ApiField(alias='resourceConsumerTeamIds', default_factory=list)
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    validityPeriod: str = ApiField(alias='validityPeriod')
    productEntitlements: Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(alias='productEntitlements')


class CertificateKeystoreRequest(ObjectModel):
    exportFormat: Literal['JKS', 'PEM', 'PKCS12'] = ApiField(alias='exportFormat')
    encryptedPrivateKeyPassphrase: str = ApiField(alias='encryptedPrivateKeyPassphrase')
    encryptedKeystorePassphrase: str = ApiField(alias='encryptedKeystorePassphrase')
    certificateLabel: str = ApiField(alias='certificateLabel')


class CertificateRecoveryRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)


class CertificateRequestDocumentInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    applicationId: UUID = ApiField(alias='applicationId')
    status: Literal['CANCELLED', 'DELETED', 'FAILED', 'ISSUED', 'NEW', 'PENDING', 'REJECTED', 'REQUESTED', 'REVOKED'] = ApiField(alias='status')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    caOrderId: str = ApiField(alias='caOrderId')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectCN: str = ApiField(alias='subjectCN')
    keyLength: int = ApiField(alias='keyLength')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    validityPeriod: str = ApiField(alias='validityPeriod')


class CertificateRequestDocumentResponse(ObjectModel):
    certificateRequests: List[CertificateRequestDocumentInformation] = ApiField(alias='certificateRequests', default_factory=list)


class CertificateRequestInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    applicationId: UUID = ApiField(alias='applicationId')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['CANCELLED', 'DELETED', 'FAILED', 'ISSUED', 'NEW', 'PENDING', 'REJECTED', 'REQUESTED', 'REVOKED'] = ApiField(alias='status')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    caOrderId: str = ApiField(alias='caOrderId')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    certificateSigningRequest: str = ApiField(alias='certificateSigningRequest')
    subjectDN: str = ApiField(alias='subjectDN')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(alias='certificateUsageMetadata', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')


class CertificateRequestRequest(ObjectModel):
    isVaaSGenerated: bool = ApiField(alias='isVaaSGenerated')
    csrAttributes: CSRAttributesInformation = ApiField(alias='csrAttributes')
    applicationServerTypeId: UUID = ApiField(alias='applicationServerTypeId')
    certificateSigningRequest: str = ApiField(alias='certificateSigningRequest')
    applicationId: UUID = ApiField(alias='applicationId')
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    existingCertificateId: UUID = ApiField(alias='existingCertificateId')
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(alias='certificateUsageMetadata', default_factory=list)
    reuseCSR: bool = ApiField(alias='reuseCSR')
    validityPeriod: str = ApiField(alias='validityPeriod')


class CertificateRequestResponse(ObjectModel):
    certificateRequests: List[CertificateRequestInformation] = ApiField(alias='certificateRequests', default_factory=list)


class CertificateRequestResubmissionRequest(ObjectModel):
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(alias='certificateUsageMetadata', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')


class CertificateRequestsSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class CertificateResponse(ObjectModel):
    count: int = ApiField(alias='count')
    certificates: List[CertificateInformation] = ApiField(alias='certificates', default_factory=list)


class CertificateRetirementRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    addToBlocklist: bool = ApiField(alias='addToBlocklist')


class CertificateSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class CertificateUsageMetadata(ObjectModel):
    appName: str = ApiField(alias='appName')
    nodeName: str = ApiField(alias='nodeName')
    automationMetadata: str = ApiField(alias='automationMetadata')


class CertificateValidationRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)


class CertificationRequestInformation(ObjectModel):
    subjectDN: str = ApiField(alias='subjectDN')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    hashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                           'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='hashAlgorithm')
    publicKeyHash: str = ApiField(alias='publicKeyHash')


class DefaultOwnershipInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: str = ApiField(alias='type')
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)


class ECKeyTypeInformation(ObjectModel):
    pass


class ErrorInformation(ObjectModel):
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class Expression(ObjectModel):
    pass


class ExtendedCertificateInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')
    certificateRequestId: UUID = ApiField(alias='certificateRequestId')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    fingerprint: str = ApiField(alias='fingerprint')
    certificateName: str = ApiField(alias='certificateName')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    certificateStatus: Literal['ACTIVE', 'DELETED', 'RETIRED'] = ApiField(alias='certificateStatus')
    statusModificationUserId: UUID = ApiField(alias='statusModificationUserId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    archivedDate: datetime = ApiField(alias='archivedDate')
    statusModificationDate: datetime = ApiField(alias='statusModificationDate')
    validityStart: datetime = ApiField(alias='validityStart')
    validityEnd: datetime = ApiField(alias='validityEnd')
    selfSigned: bool = ApiField(alias='selfSigned')
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='encryptionType')
    keyStrength: int = ApiField(alias='keyStrength')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    serialNumber: str = ApiField(alias='serialNumber')
    subjectDN: str = ApiField(alias='subjectDN')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: List[str] = ApiField(alias='subjectOU', default_factory=list)
    subjectST: str = ApiField(alias='subjectST')
    subjectL: str = ApiField(alias='subjectL')
    subjectC: str = ApiField(alias='subjectC')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectAlternativeNameDns: List[str] = ApiField(alias='subjectAlternativeNameDns', default_factory=list)
    subjectAlternativeNameNonDns: List[str] = ApiField(alias='subjectAlternativeNameNonDns', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerCN: List[str] = ApiField(alias='issuerCN', default_factory=list)
    issuerOU: List[str] = ApiField(alias='issuerOU', default_factory=list)
    issuerST: str = ApiField(alias='issuerST')
    issuerL: str = ApiField(alias='issuerL')
    issuerC: str = ApiField(alias='issuerC')
    issuerAlternativeNameDns: List[str] = ApiField(alias='issuerAlternativeNameDns', default_factory=list)
    issuerAlternativeNameNonDns: List[str] = ApiField(alias='issuerAlternativeNameNonDns', default_factory=list)
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    pathLength: int = ApiField(alias='pathLength')
    ocspNoCheck: bool = ApiField(alias='ocspNoCheck')
    requireExplicitPolicy: int = ApiField(alias='requireExplicitPolicy')
    inhibitPolicyMapping: int = ApiField(alias='inhibitPolicyMapping')
    inhibitAnyPolicy: int = ApiField(alias='inhibitAnyPolicy')
    versionType: Literal['CURRENT', 'OLD'] = ApiField(alias='versionType')
    totalInstanceCount: int = ApiField(alias='totalInstanceCount')
    totalActiveInstanceCount: int = ApiField(alias='totalActiveInstanceCount')
    instances: List[CertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)
    dekHash: str = ApiField(alias='dekHash')
    applicationServerTypeId: UUID = ApiField(alias='applicationServerTypeId')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    ownership: DefaultOwnershipInformation = ApiField(alias='ownership')
    issuerCertificates: List[CertificateInformation] = ApiField(alias='issuerCertificates', default_factory=list)


class ExtendedCertificateInstanceInformation(ObjectModel):
    certificateInstanceId: UUID = ApiField(alias='certificateInstanceId')
    certificateId: UUID = ApiField(alias='certificateId')
    certificateSource: Literal['DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'ON_PREM_CA_IMPORT', 'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL',
                               'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(alias='certificateSource')
    ipAddress: str = ApiField(alias='ipAddress')
    hostname: str = ApiField(alias='hostname')
    port: int = ApiField(alias='port')
    instanceChainValidationStatus: List[Literal['CHAIN_BUILDING_FAILED', 'CHAIN_EXPIRE_BEFORE_EE', 'DISTRUSTED', 'INCOMPLETE_CHAIN',
                                                'OK', 'SELF_SIGNED', 'UNKNOWN_ERROR']] = ApiField(alias='instanceChainValidationStatus', default_factory=list)
    sslValidationStatus: Literal['HOSTNAME_NOT_RESOLVABLE', 'INVALID_CERTIFICATE_FOUND', 'NO_CERTIFICATE_PRESENTED', 'OK',
                                 'OLD_VERSION_CERTIFICATE_FOUND', 'TARGET_UNREACHABLE', 'UNEXPECTED_CERTIFICATE_FOUND', 'UNKNOWN_ERROR'] = ApiField(alias='sslValidationStatus')
    sslValidationStatusMessage: str = ApiField(alias='sslValidationStatusMessage')
    sslValidationErrorArguments: List[str] = ApiField(alias='sslValidationErrorArguments', default_factory=list)
    sslProtocols: List[str] = ApiField(alias='sslProtocols', default_factory=list)
    lastScanDate: datetime = ApiField(alias='lastScanDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    serviceIds: List[UUID] = ApiField(alias='serviceIds', default_factory=list)
    deploymentStatus: Literal['IN_USE', 'SUPERSEDED', 'UNKNOWN'] = ApiField(alias='deploymentStatus')
    certificate: CertificateInformation = ApiField(alias='certificate')


class ExtendedCertificateInstanceResponse(ObjectModel):
    count: int = ApiField(alias='count')
    instances: List[ExtendedCertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)


class Facet(ObjectModel):
    facets: List[Facet] = ApiField(alias='facets', default_factory=list)
    name: str = ApiField(alias='name')


class FacetResponse(ObjectModel):
    aggregates: Dict[str, str] = ApiField(alias='aggregates', default_factory=dict)
    buckets: List[PairStringListFacetResponse] = ApiField(alias='buckets', default_factory=list)


class FlattenedCertificateSavedSearch(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class GeneralNamesData(ObjectModel):
    otherName: List[str] = ApiField(alias='otherName', default_factory=list)
    rfc822Name: List[str] = ApiField(alias='rfc822Name', default_factory=list)
    dNSName: List[str] = ApiField(alias='dNSName', default_factory=list)
    x400Address: List[str] = ApiField(alias='x400Address', default_factory=list)
    directoryName: List[str] = ApiField(alias='directoryName', default_factory=list)
    ediPartyName: List[str] = ApiField(alias='ediPartyName', default_factory=list)
    uniformResourceIdentifier: List[str] = ApiField(alias='uniformResourceIdentifier', default_factory=list)
    iPAddress: List[str] = ApiField(alias='iPAddress', default_factory=list)
    registeredID: List[str] = ApiField(alias='registeredID', default_factory=list)


class ImportedCertificateInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')
    companyId: UUID = ApiField(alias='companyId')
    fingerprint: str = ApiField(alias='fingerprint')
    base64Certificate: str = ApiField(alias='base64Certificate')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    certificateSource: Literal['DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'ON_PREM_CA_IMPORT', 'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL',
                               'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(alias='certificateSource')
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(alias='certificateUsageMetadata', default_factory=list)


class InvitationInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    userId: UUID = ApiField(alias='userId')
    companyId: UUID = ApiField(alias='companyId')
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)


class InvitationRequest(ObjectModel):
    role: Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                  'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN'] = ApiField(alias='role')


class InvitationResponse(ObjectModel):
    invitations: List[InvitationInformation] = ApiField(alias='invitations', default_factory=list)


class KeyTypeInformation(ObjectModel):
    keyType: str = ApiField(alias='keyType')


class KeyTypeParameters(ObjectModel):
    keyType: Literal['EC', 'RSA'] = ApiField(alias='keyType')
    keyLength: int = ApiField(alias='keyLength')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')


class MetadataInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    productEntitlement: Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(alias='productEntitlement')


class OrderObject(ObjectModel):
    field: str = ApiField(alias='field')
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')


class Ordering(ObjectModel):
    orders: List[OrderObject] = ApiField(alias='orders', default_factory=list)


class OtherApplicationServerTypeRequest(ObjectModel):
    pass


class OwnerIdAndType(ObjectModel):
    ownerId: UUID = ApiField(alias='ownerId')
    ownerType: Literal['TEAM', 'USER'] = ApiField(alias='ownerType')


class OwnershipInformation(ObjectModel):
    type: str = ApiField(alias='type')
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    id: UUID = ApiField(alias='id')


class Paging(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')


class PairStringListFacetResponse(ObjectModel):
    first: str = ApiField(alias='first')
    second: List[FacetResponse] = ApiField(alias='second', default_factory=list)


class ProviderConfigInformation(ObjectModel):
    api_key: str = ApiField(alias='api_key')
    endpoint: str = ApiField(alias='endpoint')


class ProviderInformation(ObjectModel):
    type: str = ApiField(alias='type')
    config: ProviderConfigInformation = ApiField(alias='config')
    inputs: List[ProviderInputInformation] = ApiField(alias='inputs', default_factory=list)


class ProviderInputInformation(ObjectModel):
    type: str = ApiField(alias='type')
    subnet: str = ApiField(alias='subnet')
    hosts: List[str] = ApiField(alias='hosts', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)


class RSAKeyTypeInformation(ObjectModel):
    pass


class RecommendedSettingsInformation(ObjectModel):
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectOValue: str = ApiField(alias='subjectOValue')
    subjectOUValue: str = ApiField(alias='subjectOUValue')
    subjectSTValue: str = ApiField(alias='subjectSTValue')
    subjectLValue: str = ApiField(alias='subjectLValue')
    subjectCValue: str = ApiField(alias='subjectCValue')
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    key: RecommendedSettingsKeyTypeInformation = ApiField(alias='key')


class RecommendedSettingsKeyTypeInformation(ObjectModel):
    type: Literal['EC', 'RSA'] = ApiField(alias='type')
    length: int = ApiField(alias='length')
    curve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='curve')


class SavedSearchInfo(ObjectModel):
    id: UUID = ApiField(alias='id')
    userId: UUID = ApiField(alias='userId')
    companyId: UUID = ApiField(alias='companyId')
    name: str = ApiField(alias='name')
    searchDetails: FlattenedCertificateSavedSearch = ApiField(alias='searchDetails')
    type: Literal['FULL_TEXT', 'PREDEFINED_FILTER'] = ApiField(alias='type')
    isDefault: bool = ApiField(alias='isDefault')


class SavedSearchRequest(ObjectModel):
    name: str = ApiField(alias='name')
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')
    type: Literal['FULL_TEXT', 'PREDEFINED_FILTER'] = ApiField(alias='type')
    isDefault: bool = ApiField(alias='isDefault')


class SavedSearchResponse(ObjectModel):
    savedSearchInfo: List[SavedSearchInfo] = ApiField(alias='savedSearchInfo', default_factory=list)


class ScanafiConfigResponseV1(ObjectModel):
    id: str = ApiField(alias='id')
    metadata: MetadataInformation = ApiField(alias='metadata')
    provider: ProviderInformation = ApiField(alias='provider')


class SubjectAlternativeNamesByType(ObjectModel):
    dnsNames: List[str] = ApiField(alias='dnsNames', default_factory=list)
    rfc822Names: List[str] = ApiField(alias='rfc822Names', default_factory=list)
    ipAddresses: List[str] = ApiField(alias='ipAddresses', default_factory=list)
    uniformResourceIdentifiers: List[str] = ApiField(alias='uniformResourceIdentifiers', default_factory=list)


class TeamInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    companyId: UUID = ApiField(alias='companyId')
    ownership: Dict[str, List[UUID]] = ApiField(alias='ownership', default_factory=dict)


class UnassignedCertificateAggregatesResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    certificateAggregatesMap: Dict[str, int] = ApiField(alias='certificateAggregatesMap', default_factory=dict)


class UserInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    username: str = ApiField(alias='username')
    firstname: str = ApiField(alias='firstname')
    lastname: str = ApiField(alias='lastname')
    userStatus: str = ApiField(alias='userStatus')
    userType: str = ApiField(alias='userType')
    userAccountType: str = ApiField(alias='userAccountType')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN',
                                         'PKI_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    creationDate: datetime = ApiField(alias='creationDate')
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    admin: bool = ApiField(alias='admin')
    teamsIds: List[UUID] = ApiField(alias='teamsIds', default_factory=list)


class entityTag(ObjectModel):
    value: str = ApiField(alias='value')
    weak: bool = ApiField(alias='weak')


class language(ObjectModel):
    language: str = ApiField(alias='language')
    script: str = ApiField(alias='script')
    variant: str = ApiField(alias='variant')
    displayName: str = ApiField(alias='displayName')
    country: str = ApiField(alias='country')
    unicodeLocaleAttributes: List[str] = ApiField(alias='unicodeLocaleAttributes', default_factory=list)
    unicodeLocaleKeys: List[str] = ApiField(alias='unicodeLocaleKeys', default_factory=list)
    displayLanguage: str = ApiField(alias='displayLanguage')
    displayScript: str = ApiField(alias='displayScript')
    displayCountry: str = ApiField(alias='displayCountry')
    displayVariant: str = ApiField(alias='displayVariant')
    extensionKeys: List[str] = ApiField(alias='extensionKeys', default_factory=list)
    iso3Language: str = ApiField(alias='iso3Language')
    iso3Country: str = ApiField(alias='iso3Country')


class mediaType(ObjectModel):
    type: str = ApiField(alias='type')
    subtype: str = ApiField(alias='subtype')
    parameters: Dict[str, str] = ApiField(alias='parameters', default_factory=dict)
    wildcardType: bool = ApiField(alias='wildcardType')
    wildcardSubtype: bool = ApiField(alias='wildcardSubtype')


class statusInfo(ObjectModel):
    family: Literal['CLIENT_ERROR', 'INFORMATIONAL', 'OTHER', 'REDIRECTION', 'SERVER_ERROR', 'SUCCESSFUL'] = ApiField(alias='family')
    statusCode: int = ApiField(alias='statusCode')
    reasonPhrase: str = ApiField(alias='reasonPhrase')


ApiClientInformation.update_forward_refs()
ApplicationInformation.update_forward_refs()
ApplicationRequest.update_forward_refs()
ApplicationResponse.update_forward_refs()
ApplicationServerTypeInformation.update_forward_refs()
ApplicationServerTypeResponse.update_forward_refs()
ApplicationsAssignRequest.update_forward_refs()
ApplicationsAssignResponse.update_forward_refs()
BaseApplicationServerTypeRequest.update_forward_refs()
CSRAttributesInformation.update_forward_refs()
CertificateAggregatesRangeResponse.update_forward_refs()
CertificateAggregatesResponse.update_forward_refs()
CertificateAggregationsRequest.update_forward_refs()
CertificateCategoryInformation.update_forward_refs()
CertificateDeletionRequest.update_forward_refs()
CertificateImportInfo.update_forward_refs()
CertificateImportRequest.update_forward_refs()
CertificateImportResponse.update_forward_refs()
CertificateInformation.update_forward_refs()
CertificateInstallationsUsageResponse.update_forward_refs()
CertificateInstanceInformation.update_forward_refs()
CertificateInstanceSearchRequest.update_forward_refs()
CertificateInstanceValidationRequest.update_forward_refs()
CertificateIssuingTemplateInformation.update_forward_refs()
CertificateKeystoreRequest.update_forward_refs()
CertificateRecoveryRequest.update_forward_refs()
CertificateRequestDocumentInformation.update_forward_refs()
CertificateRequestDocumentResponse.update_forward_refs()
CertificateRequestInformation.update_forward_refs()
CertificateRequestRequest.update_forward_refs()
CertificateRequestResponse.update_forward_refs()
CertificateRequestResubmissionRequest.update_forward_refs()
CertificateRequestsSearchRequest.update_forward_refs()
CertificateResponse.update_forward_refs()
CertificateRetirementRequest.update_forward_refs()
CertificateSearchRequest.update_forward_refs()
CertificateUsageMetadata.update_forward_refs()
CertificateValidationRequest.update_forward_refs()
CertificationRequestInformation.update_forward_refs()
DefaultOwnershipInformation.update_forward_refs()
ECKeyTypeInformation.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Expression.update_forward_refs()
ExtendedCertificateInformation.update_forward_refs()
ExtendedCertificateInstanceInformation.update_forward_refs()
ExtendedCertificateInstanceResponse.update_forward_refs()
Facet.update_forward_refs()
FacetResponse.update_forward_refs()
FlattenedCertificateSavedSearch.update_forward_refs()
GeneralNamesData.update_forward_refs()
ImportedCertificateInformation.update_forward_refs()
InvitationInformation.update_forward_refs()
InvitationRequest.update_forward_refs()
InvitationResponse.update_forward_refs()
KeyTypeInformation.update_forward_refs()
KeyTypeParameters.update_forward_refs()
MetadataInformation.update_forward_refs()
OrderObject.update_forward_refs()
Ordering.update_forward_refs()
OtherApplicationServerTypeRequest.update_forward_refs()
OwnerIdAndType.update_forward_refs()
OwnershipInformation.update_forward_refs()
Paging.update_forward_refs()
PairStringListFacetResponse.update_forward_refs()
ProviderConfigInformation.update_forward_refs()
ProviderInformation.update_forward_refs()
ProviderInputInformation.update_forward_refs()
RSAKeyTypeInformation.update_forward_refs()
RecommendedSettingsInformation.update_forward_refs()
RecommendedSettingsKeyTypeInformation.update_forward_refs()
SavedSearchInfo.update_forward_refs()
SavedSearchRequest.update_forward_refs()
SavedSearchResponse.update_forward_refs()
ScanafiConfigResponseV1.update_forward_refs()
SubjectAlternativeNamesByType.update_forward_refs()
TeamInformation.update_forward_refs()
UnassignedCertificateAggregatesResponse.update_forward_refs()
UserInformation.update_forward_refs()
entityTag.update_forward_refs()
language.update_forward_refs()
mediaType.update_forward_refs()
statusInfo.update_forward_refs()
