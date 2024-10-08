from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Union,
)
from uuid import UUID

AnyValue = Any

class ApiClientInformation(ObjectModel):
    identifier: str = ApiField(alias='identifier')
    type: str = ApiField(alias='type')

class ApplicationInformation(ObjectModel):
    certificateIssuingTemplateAliasIdMap: Dict[str, UUID] = ApiField(
        alias='certificateIssuingTemplateAliasIdMap',
        default_factory=dict
    )
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    description: str = ApiField(alias='description')
    fullyQualifiedDomainNames: List[str] = ApiField(alias='fullyQualifiedDomainNames', default_factory=list)
    id: UUID = ApiField(alias='id')
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    ownerIdsAndTypes: List[OwnerIdAndType] = ApiField(alias='ownerIdsAndTypes', default_factory=list)
    ownership: ApplicationOwnership = ApiField(alias='ownership')
    owningServiceAccounts: List[ServiceAccountInformation] = ApiField(
        alias='owningServiceAccounts',
        default_factory=list
    )
    owningTeams: List[TeamInformation] = ApiField(alias='owningTeams', default_factory=list)
    owningUsers: List[UserInformation] = ApiField(alias='owningUsers', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)

class ApplicationOwnership(ObjectModel):
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)

class ApplicationRequest(ObjectModel):
    certificateIssuingTemplateAliasIdMap: Dict[str, UUID] = ApiField(
        alias='certificateIssuingTemplateAliasIdMap',
        default_factory=dict
    )
    description: str = ApiField(alias='description')
    externalIpRanges: List[str] = ApiField(alias='externalIpRanges', default_factory=list)
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    fullyQualifiedDomainNames: List[str] = ApiField(alias='fullyQualifiedDomainNames', default_factory=list)
    internalFqdns: List[str] = ApiField(alias='internalFqdns', default_factory=list)
    internalIpRanges: List[str] = ApiField(alias='internalIpRanges', default_factory=list)
    internalPorts: List[str] = ApiField(alias='internalPorts', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    name: str = ApiField(alias='name')
    ownerIdsAndTypes: List[OwnerIdAndType] = ApiField(alias='ownerIdsAndTypes', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    startTargetedDiscovery: bool = ApiField(alias='startTargetedDiscovery')

class ApplicationResponse(ObjectModel):
    applications: List[ApplicationInformation] = ApiField(alias='applications', default_factory=list)
    ownershipCount: int = ApiField(alias='ownershipCount')
    totalCount: int = ApiField(alias='totalCount')

class ApplicationsAssignRequest(ObjectModel):
    action: Literal['ADD', 'DELETE', 'DELETE_ALL', 'REPLACE'] = ApiField(alias='action')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    targetedApplicationIds: List[UUID] = ApiField(alias='targetedApplicationIds', default_factory=list)

class ApplicationsAssignResponse(ObjectModel):
    certificates: List[CertificateInformation] = ApiField(alias='certificates', default_factory=list)

class BaseFilter(ObjectModel):
    ...

class BaseOrdering(ObjectModel):
    orders: List[Order] = ApiField(alias='orders', default_factory=list)

class Bucket(ObjectModel):
    first: str = ApiField(alias='first')
    second: List[NestedFacet] = ApiField(alias='second', default_factory=list)

class CSRAttributesInformation(ObjectModel):
    commonName: str = ApiField(alias='commonName')
    country: str = ApiField(alias='country')
    keyTypeParameters: KeyTypeParameters = ApiField(alias='keyTypeParameters')
    locality: str = ApiField(alias='locality')
    organization: str = ApiField(alias='organization')
    organizationalUnits: List[str] = ApiField(alias='organizationalUnits', default_factory=list)
    state: str = ApiField(alias='state')
    subjectAlternativeNamesByType: SubjectAlternativeNamesByType = ApiField(alias='subjectAlternativeNamesByType')

class CertificateAggregatesRangeResponse(ObjectModel):
    certificateAggregatesMap: Dict[str, int] = ApiField(alias='certificateAggregatesMap', default_factory=dict)
    companyId: UUID = ApiField(alias='companyId')

class CertificateAggregatesResponse(ObjectModel):
    certificateAggregatesMap: Dict[str, CertificateCategoryInformation] = ApiField(
        alias='certificateAggregatesMap',
        default_factory=dict
    )
    companyId: UUID = ApiField(alias='companyId')

class CertificateAggregationsRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    facet: Facet = ApiField(alias='facet')
    includeRetired: bool = ApiField(alias='includeRetired')

class CertificateAuthorityProductInformation(ObjectModel):
    certificateType: Literal['DOMAIN_VALIDATED_SSL', 'OTHER'] = ApiField(alias='certificateType')
    hashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='hashAlgorithm')
    productName: str = ApiField(alias='productName')
    productTypes: List[Literal['CODESIGN', 'SSL']] = ApiField(alias='productTypes', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateCategoryInformation(ObjectModel):
    certificateCategoryAggregatesMap: Dict[str, int] = ApiField(
        alias='certificateCategoryAggregatesMap',
        default_factory=dict
    )
    certificatesCount: int = ApiField(alias='certificatesCount')

class CertificateDeletionRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)

class CertificateImportInfo(ObjectModel):
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificate: str = ApiField(alias='certificate')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(
        alias='certificateUsageMetadata',
        default_factory=list
    )
    issuerCertificates: List[str] = ApiField(alias='issuerCertificates', default_factory=list)

class CertificateImportRequest(ObjectModel):
    certificates: List[CertificateImportInfo] = ApiField(alias='certificates', default_factory=list)
    overrideBlocklist: bool = ApiField(alias='overrideBlocklist')

class CertificateImportResponse(ObjectModel):
    certificateInformations: List[ImportedCertificateInformation] = ApiField(
        alias='certificateInformations',
        default_factory=list
    )
    statistics: Dict[str, int] = ApiField(alias='statistics', default_factory=dict)

class CertificateInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    archivedDate: datetime = ApiField(alias='archivedDate')
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateName: str = ApiField(alias='certificateName')
    certificateRequestId: UUID = ApiField(alias='certificateRequestId')
    certificateStatus: Literal['ACTIVE', 'DELETED', 'RETIRED'] = ApiField(alias='certificateStatus')
    companyId: UUID = ApiField(alias='companyId')
    dekHash: str = ApiField(alias='dekHash')
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(
        alias='encryptionType'
    )
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    inhibitAnyPolicy: int = ApiField(alias='inhibitAnyPolicy')
    inhibitPolicyMapping: int = ApiField(alias='inhibitPolicyMapping')
    instances: List[CertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)
    issuerAlternativeNameDns: List[str] = ApiField(alias='issuerAlternativeNameDns', default_factory=list)
    issuerAlternativeNameNonDns: List[str] = ApiField(alias='issuerAlternativeNameNonDns', default_factory=list)
    issuerC: str = ApiField(alias='issuerC')
    issuerCN: List[str] = ApiField(alias='issuerCN', default_factory=list)
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerL: str = ApiField(alias='issuerL')
    issuerOU: List[str] = ApiField(alias='issuerOU', default_factory=list)
    issuerST: str = ApiField(alias='issuerST')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyStrength: int = ApiField(alias='keyStrength')
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    lastNotification: int = ApiField(alias='lastNotification')
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    ocspNoCheck: bool = ApiField(alias='ocspNoCheck')
    ownership: CertificateOwnership = ApiField(alias='ownership')
    pathLength: int = ApiField(alias='pathLength')
    requireExplicitPolicy: int = ApiField(alias='requireExplicitPolicy')
    selfSigned: bool = ApiField(alias='selfSigned')
    serialNumber: str = ApiField(alias='serialNumber')
    signatureAlgorithm: Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(
        alias='signatureAlgorithm'
    )
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    statusModificationDate: datetime = ApiField(alias='statusModificationDate')
    statusModificationUserId: UUID = ApiField(alias='statusModificationUserId')
    subjectAlternativeNameDns: List[str] = ApiField(alias='subjectAlternativeNameDns', default_factory=list)
    subjectAlternativeNameNonDns: List[str] = ApiField(alias='subjectAlternativeNameNonDns', default_factory=list)
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectC: str = ApiField(alias='subjectC')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    subjectL: str = ApiField(alias='subjectL')
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: List[str] = ApiField(alias='subjectOU', default_factory=list)
    subjectST: str = ApiField(alias='subjectST')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    totalActiveInstanceCount: int = ApiField(alias='totalActiveInstanceCount')
    totalInstanceCount: int = ApiField(alias='totalInstanceCount')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')
    versionType: Literal['CURRENT', 'OLD'] = ApiField(alias='versionType')

class CertificateInstallationsUsageResponse(ObjectModel):
    count: int = ApiField(alias='count')

class CertificateInstanceInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificateId: UUID = ApiField(alias='certificateId')
    certificateInstanceId: UUID = ApiField(alias='certificateInstanceId')
    certificateSource: Literal[
        'AWS_DISCOVERY', 'AZURE_DISCOVERY', 'DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'GCP_DISCOVERY', 'KUBERNETES_DISCOVERY', 'MACHINE_DISCOVERY', 'ON_PREM_CA_IMPORT',
        'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL', 'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(
        alias='certificateSource'
    )
    deploymentStatus: Literal['IN_USE', 'SUPERSEDED', 'UNKNOWN'] = ApiField(alias='deploymentStatus')
    hostname: str = ApiField(alias='hostname')
    instanceChainValidationStatus: List[
        Literal['CHAIN_BUILDING_FAILED', 'CHAIN_EXPIRE_BEFORE_EE', 'DISTRUSTED', 'INCOMPLETE_CHAIN',
        'OK', 'SELF_SIGNED', 'UNKNOWN_ERROR']] = ApiField(alias='instanceChainValidationStatus', default_factory=list)
    ipAddress: str = ApiField(alias='ipAddress')
    lastScanDate: datetime = ApiField(alias='lastScanDate')
    lastValidatedAttempt: datetime = ApiField(alias='lastValidatedAttempt')
    modificationDate: datetime = ApiField(alias='modificationDate')
    port: int = ApiField(alias='port')
    serviceIds: List[UUID] = ApiField(alias='serviceIds', default_factory=list)
    sslProtocols: List[str] = ApiField(alias='sslProtocols', default_factory=list)
    sslValidationErrorArguments: List[str] = ApiField(alias='sslValidationErrorArguments', default_factory=list)
    sslValidationStatus: Literal[
        'HOSTNAME_NOT_RESOLVABLE', 'INVALID_CERTIFICATE_FOUND', 'NO_CERTIFICATE_PRESENTED', 'OK',
        'OLD_VERSION_CERTIFICATE_FOUND', 'TARGET_UNREACHABLE', 'UNEXPECTED_CERTIFICATE_FOUND', 'UNKNOWN_ERROR'] = ApiField(
        alias='sslValidationStatus'
    )
    sslValidationStatusMessage: str = ApiField(alias='sslValidationStatusMessage')

class CertificateInstanceSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')

class CertificateInstanceValidationRequest(ObjectModel):
    instanceIds: List[UUID] = ApiField(alias='instanceIds', default_factory=list)

class CertificateIssuingTemplateInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    id: UUID = ApiField(alias='id')
    keyGeneratedByVenafiAllowed: bool = ApiField(alias='keyGeneratedByVenafiAllowed')
    keyReuse: bool = ApiField(alias='keyReuse')
    keyTypes: List[KeyTypeInformation] = ApiField(alias='keyTypes', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    priority: int = ApiField(alias='priority')
    product: CertificateAuthorityProductInformation = ApiField(alias='product')
    productEntitlement: Literal['ANY', 'CODESIGN', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(
        alias='productEntitlement'
    )
    productEntitlements: Literal['ANY', 'CODESIGN', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(
        alias='productEntitlements'
    )
    reason: str = ApiField(alias='reason')
    recommendedSettings: RecommendedSettingsInformation = ApiField(alias='recommendedSettings')
    resourceConsumerTeamIds: List[UUID] = ApiField(alias='resourceConsumerTeamIds', default_factory=list)
    resourceConsumerUserIds: List[UUID] = ApiField(alias='resourceConsumerUserIds', default_factory=list)
    sanDnsNameRegexes: List[str] = ApiField(alias='sanDnsNameRegexes', default_factory=list)
    sanIpAddressRegexes: List[str] = ApiField(alias='sanIpAddressRegexes', default_factory=list)
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    sanRfc822NameRegexes: List[str] = ApiField(alias='sanRfc822NameRegexes', default_factory=list)
    sanUniformResourceIdentifierRegexes: List[str] = ApiField(
        alias='sanUniformResourceIdentifierRegexes',
        default_factory=list
    )
    status: Literal['AVAILABLE', 'UNAVAILABLE'] = ApiField(alias='status')
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValues: List[str] = ApiField(alias='subjectCValues', default_factory=list)
    subjectLRegexes: List[str] = ApiField(alias='subjectLRegexes', default_factory=list)
    subjectORegexes: List[str] = ApiField(alias='subjectORegexes', default_factory=list)
    subjectOURegexes: List[str] = ApiField(alias='subjectOURegexes', default_factory=list)
    subjectSTRegexes: List[str] = ApiField(alias='subjectSTRegexes', default_factory=list)
    systemGenerated: bool = ApiField(alias='systemGenerated')
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateKeystoreRequest(ObjectModel):
    certificateLabel: str = ApiField(alias='certificateLabel')
    encryptedKeystorePassphrase: str = ApiField(alias='encryptedKeystorePassphrase')
    encryptedPrivateKeyPassphrase: str = ApiField(alias='encryptedPrivateKeyPassphrase')
    exportFormat: Literal['JKS', 'PEM', 'PKCS12'] = ApiField(alias='exportFormat')

class CertificateOwnership(ObjectModel):
    owningContainers: List[ExtendedApplicationOwnership] = ApiField(alias='owningContainers', default_factory=list)

class CertificateRecoveryRequest(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)

class CertificateRequestDocumentInformation(ObjectModel):
    applicationId: UUID = ApiField(alias='applicationId')
    approvedIds: List[UUID] = ApiField(alias='approvedIds', default_factory=list)
    approverTeamIds: List[UUID] = ApiField(alias='approverTeamIds', default_factory=list)
    approverUserIds: List[UUID] = ApiField(alias='approverUserIds', default_factory=list)
    caOrderId: str = ApiField(alias='caOrderId')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    customAttributes: CustomAttributes = ApiField(alias='customAttributes')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    finalApproverId: UUID = ApiField(alias='finalApproverId')
    id: UUID = ApiField(alias='id')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['CANCELLED', 'DELETED', 'FAILED', 'ISSUED', 'NEW', 'PENDING', 'PENDING_APPROVAL',
    'PENDING_FINAL_APPROVAL', 'REJECTED', 'REJECTED_APPROVAL', 'REQUESTED', 'REVOKED'] = ApiField(alias='status')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectCN: str = ApiField(alias='subjectCN')
    subjectDN: str = ApiField(alias='subjectDN')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateRequestDocumentResponse(ObjectModel):
    certificateRequests: List[CertificateRequestDocumentInformation] = ApiField(
        alias='certificateRequests',
        default_factory=list
    )
    numFound: int = ApiField(alias='numFound')

class CertificateRequestInformation(ObjectModel):
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    applicationId: UUID = ApiField(alias='applicationId')
    approvedIds: List[UUID] = ApiField(alias='approvedIds', default_factory=list)
    approverTeamIds: List[UUID] = ApiField(alias='approverTeamIds', default_factory=list)
    approverUserIds: List[UUID] = ApiField(alias='approverUserIds', default_factory=list)
    caOrderId: str = ApiField(alias='caOrderId')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateSigningRequest: str = ApiField(alias='certificateSigningRequest')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(
        alias='certificateUsageMetadata',
        default_factory=list
    )
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    customAttributesInformation: CustomAttributesInformation = ApiField(alias='customAttributesInformation')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    finalApproverId: UUID = ApiField(alias='finalApproverId')
    id: UUID = ApiField(alias='id')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['CANCELLED', 'DELETED', 'FAILED', 'ISSUED', 'NEW', 'PENDING', 'PENDING_APPROVAL',
    'PENDING_FINAL_APPROVAL', 'REJECTED', 'REJECTED_APPROVAL', 'REQUESTED', 'REVOKED'] = ApiField(alias='status')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectDN: str = ApiField(alias='subjectDN')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateRequestRequest(ObjectModel):
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    applicationId: UUID = ApiField(alias='applicationId')
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateSigningRequest: str = ApiField(alias='certificateSigningRequest')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(
        alias='certificateUsageMetadata',
        default_factory=list
    )
    csrAttributes: CSRAttributesInformation = ApiField(alias='csrAttributes')
    customAttributes: CustomAttributesInformation = ApiField(alias='customAttributes')
    existingCertificateId: UUID = ApiField(alias='existingCertificateId')
    isVaaSGenerated: bool = ApiField(alias='isVaaSGenerated')
    reuseCSR: bool = ApiField(alias='reuseCSR')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateRequestResponse(ObjectModel):
    certificateRequests: List[CertificateRequestInformation] = ApiField(
        alias='certificateRequests',
        default_factory=list
    )

class CertificateRequestResubmissionRequest(ObjectModel):
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(
        alias='certificateUsageMetadata',
        default_factory=list
    )
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateRequestsSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')

class CertificateResponse(ObjectModel):
    certificates: List[CertificateInformation] = ApiField(alias='certificates', default_factory=list)
    count: int = ApiField(alias='count')

class CertificateRetirementRequest(ObjectModel):
    addToBlocklist: bool = ApiField(alias='addToBlocklist')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)

class CertificateSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')

class CertificateUsageMetadata(ObjectModel):
    appName: str = ApiField(alias='appName')
    automationMetadata: str = ApiField(alias='automationMetadata')
    nodeName: str = ApiField(alias='nodeName')

class CertificateValidationRequest(ObjectModel):
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)

class CertificateValidationResponse(ObjectModel):
    fingerprints: List[str] = ApiField(alias='fingerprints', default_factory=list)

class CertificationRequestInformation(ObjectModel):
    hashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='hashAlgorithm')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    publicKeyHash: str = ApiField(alias='publicKeyHash')
    signatureAlgorithm: Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(
        alias='signatureAlgorithm'
    )
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectDN: str = ApiField(alias='subjectDN')

class Condition(ObjectModel):
    field: str = ApiField(alias='field')
    operator: Literal['EQ', 'FIND', 'GT', 'GTE', 'IN', 'LT', 'LTE', 'MATCH'] = ApiField(alias='operator')
    value: str = ApiField(alias='value')
    values: List[str] = ApiField(alias='values', default_factory=list)

class CustomAttributes(ObjectModel):
    dnsNames: List[str] = ApiField(alias='dnsNames', default_factory=list)
    overwriteSans: bool = ApiField(alias='overwriteSans')

class CustomAttributesInformation(ObjectModel):
    dnsNames: List[str] = ApiField(alias='dnsNames', default_factory=list)
    overwriteSans: bool = ApiField(alias='overwriteSans')

class EntityTag(ObjectModel):
    value: str = ApiField(alias='value')
    weak: bool = ApiField(alias='weak')

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class Expression(ObjectModel):
    ...

class ExtendedApplicationOwnership(ObjectModel):
    id: UUID = ApiField(alias='id')
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    type: str = ApiField(alias='type')

class ExtendedCertificateInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    archivedDate: datetime = ApiField(alias='archivedDate')
    authorityKeyIdentifierHash: str = ApiField(alias='authorityKeyIdentifierHash')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateName: str = ApiField(alias='certificateName')
    certificateRequestId: UUID = ApiField(alias='certificateRequestId')
    certificateStatus: Literal['ACTIVE', 'DELETED', 'RETIRED'] = ApiField(alias='certificateStatus')
    companyId: UUID = ApiField(alias='companyId')
    dekHash: str = ApiField(alias='dekHash')
    encryptionType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(
        alias='encryptionType'
    )
    extendedKeyUsage: List[str] = ApiField(alias='extendedKeyUsage', default_factory=list)
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    inhibitAnyPolicy: int = ApiField(alias='inhibitAnyPolicy')
    inhibitPolicyMapping: int = ApiField(alias='inhibitPolicyMapping')
    instances: List[CertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)
    issuerAlternativeNameDns: List[str] = ApiField(alias='issuerAlternativeNameDns', default_factory=list)
    issuerAlternativeNameNonDns: List[str] = ApiField(alias='issuerAlternativeNameNonDns', default_factory=list)
    issuerC: str = ApiField(alias='issuerC')
    issuerCN: List[str] = ApiField(alias='issuerCN', default_factory=list)
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    issuerCertificates: List[CertificateInformation] = ApiField(alias='issuerCertificates', default_factory=list)
    issuerDN: str = ApiField(alias='issuerDN')
    issuerL: str = ApiField(alias='issuerL')
    issuerOU: List[str] = ApiField(alias='issuerOU', default_factory=list)
    issuerST: str = ApiField(alias='issuerST')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyStrength: int = ApiField(alias='keyStrength')
    keyUsage: List[str] = ApiField(alias='keyUsage', default_factory=list)
    lastNotification: int = ApiField(alias='lastNotification')
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    ocspNoCheck: bool = ApiField(alias='ocspNoCheck')
    ownership: CertificateOwnership = ApiField(alias='ownership')
    pathLength: int = ApiField(alias='pathLength')
    requireExplicitPolicy: int = ApiField(alias='requireExplicitPolicy')
    selfSigned: bool = ApiField(alias='selfSigned')
    serialNumber: str = ApiField(alias='serialNumber')
    signatureAlgorithm: Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(
        alias='signatureAlgorithm'
    )
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    statusModificationDate: datetime = ApiField(alias='statusModificationDate')
    statusModificationUserId: UUID = ApiField(alias='statusModificationUserId')
    subjectAlternativeNameDns: List[str] = ApiField(alias='subjectAlternativeNameDns', default_factory=list)
    subjectAlternativeNameNonDns: List[str] = ApiField(alias='subjectAlternativeNameNonDns', default_factory=list)
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectC: str = ApiField(alias='subjectC')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectKeyIdentifierHash: str = ApiField(alias='subjectKeyIdentifierHash')
    subjectL: str = ApiField(alias='subjectL')
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: List[str] = ApiField(alias='subjectOU', default_factory=list)
    subjectST: str = ApiField(alias='subjectST')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    totalActiveInstanceCount: int = ApiField(alias='totalActiveInstanceCount')
    totalInstanceCount: int = ApiField(alias='totalInstanceCount')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')
    versionType: Literal['CURRENT', 'OLD'] = ApiField(alias='versionType')

class ExtendedCertificateInstanceInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificate: CertificateInformation = ApiField(alias='certificate')
    certificateId: UUID = ApiField(alias='certificateId')
    certificateInstanceId: UUID = ApiField(alias='certificateInstanceId')
    certificateSource: Literal[
        'AWS_DISCOVERY', 'AZURE_DISCOVERY', 'DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'GCP_DISCOVERY', 'KUBERNETES_DISCOVERY', 'MACHINE_DISCOVERY', 'ON_PREM_CA_IMPORT',
        'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL', 'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(
        alias='certificateSource'
    )
    deploymentStatus: Literal['IN_USE', 'SUPERSEDED', 'UNKNOWN'] = ApiField(alias='deploymentStatus')
    hostname: str = ApiField(alias='hostname')
    instanceChainValidationStatus: List[
        Literal['CHAIN_BUILDING_FAILED', 'CHAIN_EXPIRE_BEFORE_EE', 'DISTRUSTED', 'INCOMPLETE_CHAIN',
        'OK', 'SELF_SIGNED', 'UNKNOWN_ERROR']] = ApiField(alias='instanceChainValidationStatus', default_factory=list)
    ipAddress: str = ApiField(alias='ipAddress')
    lastScanDate: datetime = ApiField(alias='lastScanDate')
    lastValidatedAttempt: datetime = ApiField(alias='lastValidatedAttempt')
    modificationDate: datetime = ApiField(alias='modificationDate')
    port: int = ApiField(alias='port')
    serviceIds: List[UUID] = ApiField(alias='serviceIds', default_factory=list)
    sslProtocols: List[str] = ApiField(alias='sslProtocols', default_factory=list)
    sslValidationErrorArguments: List[str] = ApiField(alias='sslValidationErrorArguments', default_factory=list)
    sslValidationStatus: Literal[
        'HOSTNAME_NOT_RESOLVABLE', 'INVALID_CERTIFICATE_FOUND', 'NO_CERTIFICATE_PRESENTED', 'OK',
        'OLD_VERSION_CERTIFICATE_FOUND', 'TARGET_UNREACHABLE', 'UNEXPECTED_CERTIFICATE_FOUND', 'UNKNOWN_ERROR'] = ApiField(
        alias='sslValidationStatus'
    )
    sslValidationStatusMessage: str = ApiField(alias='sslValidationStatusMessage')

class ExtendedCertificateInstanceResponse(ObjectModel):
    count: int = ApiField(alias='count')
    instances: List[ExtendedCertificateInstanceInformation] = ApiField(alias='instances', default_factory=list)

class Facet(ObjectModel):
    domain: Dict[str, AnyValue] = ApiField(alias='domain', default_factory=dict)
    facets: List[Facet] = ApiField(alias='facets', default_factory=list)
    name: str = ApiField(alias='name')

class FacetResponse(ObjectModel):
    aggregates: Dict[str, str] = ApiField(alias='aggregates', default_factory=dict)
    buckets: List[Bucket] = ApiField(alias='buckets', default_factory=list)

class Filter(ObjectModel):
    expression: BaseFilter = ApiField(alias='expression')
    ordering: BaseOrdering = ApiField(alias='ordering')
    paging: Page = ApiField(alias='paging')

class FilterOperand(ObjectModel):
    operand: Condition = ApiField(alias='operand')
    operator: Literal['NOT'] = ApiField(alias='operator')

class FilterOperands(ObjectModel):
    operands: List[BaseFilter] = ApiField(alias='operands', default_factory=list)
    operator: Literal['AND', 'OR'] = ApiField(alias='operator')

class FlattenedCertificateSavedSearch(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')

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

class ImportedCertificateInformation(ObjectModel):
    apiClientInformation: ApiClientInformation = ApiField(alias='apiClientInformation')
    base64Certificate: str = ApiField(alias='base64Certificate')
    certificateSource: Literal[
        'AWS_DISCOVERY', 'AZURE_DISCOVERY', 'DOMAIN_SCAN', 'EXTERNAL_CA_IMPORT', 'EXTERNAL_SCAN', 'FILE_IMPORT', 'GCP_DISCOVERY', 'KUBERNETES_DISCOVERY', 'MACHINE_DISCOVERY', 'ON_PREM_CA_IMPORT',
        'SMART_SCAN_EXTERNAL', 'SMART_SCAN_INTERNAL', 'SMART_VALIDATION_EXTERNAL', 'SMART_VALIDATION_INTERNAL', 'TRUSTNET_SCAN', 'UNKNOWN', 'USER_IMPORTED', 'USER_PROVIDED', 'USER_SCAN'] = ApiField(
        alias='certificateSource'
    )
    certificateUsageMetadata: List[CertificateUsageMetadata] = ApiField(
        alias='certificateUsageMetadata',
        default_factory=list
    )
    companyId: UUID = ApiField(alias='companyId')
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    issuerCertificateIds: List[UUID] = ApiField(alias='issuerCertificateIds', default_factory=list)
    managedCertificateId: UUID = ApiField(alias='managedCertificateId')

class InventoryMonitoringConfig(ObjectModel):
    inventoryMonitoringConfigurationType: str = ApiField(alias='inventoryMonitoringConfigurationType')

class InventoryMonitoringConfigRequest(ObjectModel):
    inventoryMonitoringConfiguration: Union[CertificateExpirationInventoryMonitoringConfig] = ApiField(
        alias='inventoryMonitoringConfiguration'
    )

class InventoryMonitoringConfiguration(ObjectModel):
    inventoryMonitoringConfigurationType: str = ApiField(alias='inventoryMonitoringConfigurationType')

class InventoryMonitoringConfigurationRequest(ObjectModel):
    inventoryMonitoringConfiguration: InventoryMonitoringConfiguration = ApiField(
        alias='inventoryMonitoringConfiguration'
    )

class InventoryMonitoringConfigurationResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    configuration: InventoryMonitoringConfiguration = ApiField(alias='configuration')
    id: UUID = ApiField(alias='id')

class InventoryMonitoringSchedulerInformation(ObjectModel):
    name: str = ApiField(alias='name')
    status: Literal['DONE', 'FAILED', 'PENDING', 'RUNNING'] = ApiField(alias='status')

class InvitationInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN', 'PKI_ADMIN',
    'PLATFORM_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    properties: Dict[str, str] = ApiField(alias='properties', default_factory=dict)
    userId: UUID = ApiField(alias='userId')

class InvitationRequest(ObjectModel):
    role: Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN', 'PKI_ADMIN',
    'PLATFORM_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN'] = ApiField(alias='role')

class InvitationResponse(ObjectModel):
    invitations: List[InvitationInformation] = ApiField(alias='invitations', default_factory=list)

class KeyTypeInformation(ObjectModel):
    keyType: str = ApiField(alias='keyType')

class KeyTypeParameters(ObjectModel):
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['EC', 'RSA'] = ApiField(alias='keyType')

class Link(ObjectModel):
    params: Dict[str, str] = ApiField(alias='params', default_factory=dict)
    rel: str = ApiField(alias='rel')
    rels: List[str] = ApiField(alias='rels', default_factory=list)
    title: str = ApiField(alias='title')
    type: str = ApiField(alias='type')
    uri: str = ApiField(alias='uri')
    uriBuilder: UriBuilder = ApiField(alias='uriBuilder')

class MediaType(ObjectModel):
    parameters: Dict[str, str] = ApiField(alias='parameters', default_factory=dict)
    subtype: str = ApiField(alias='subtype')
    type: str = ApiField(alias='type')
    wildcardSubtype: bool = ApiField(alias='wildcardSubtype')
    wildcardType: bool = ApiField(alias='wildcardType')

class MetadataInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    productEntitlement: Literal['ANY', 'CODESIGN', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(
        alias='productEntitlement'
    )

class MultivaluedMapStringObject(ObjectModel):
    empty: bool = ApiField(alias='empty')

class MultivaluedMapStringString(ObjectModel):
    empty: bool = ApiField(alias='empty')

class NestedBucket(ObjectModel):
    first: str = ApiField(alias='first')
    second: List[AnyValue] = ApiField(alias='second', default_factory=list)

class NestedFacet(ObjectModel):
    aggregates: Dict[str, str] = ApiField(alias='aggregates', default_factory=dict)
    buckets: List[NestedBucket] = ApiField(alias='buckets', default_factory=list)

class NewCookie(ObjectModel):
    comment: str = ApiField(alias='comment')
    domain: str = ApiField(alias='domain')
    expiry: datetime = ApiField(alias='expiry')
    httpOnly: bool = ApiField(alias='httpOnly')
    maxAge: int = ApiField(alias='maxAge')
    name: str = ApiField(alias='name')
    path: str = ApiField(alias='path')
    sameSite: Literal['LAX', 'NONE', 'STRICT'] = ApiField(alias='sameSite')
    secure: bool = ApiField(alias='secure')
    value: str = ApiField(alias='value')
    version: int = ApiField(alias='version')

class Order(ObjectModel):
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')
    field: str = ApiField(alias='field')

class OrderObject(ObjectModel):
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')
    field: str = ApiField(alias='field')

class Ordering(ObjectModel):
    orders: List[OrderObject] = ApiField(alias='orders', default_factory=list)

class OwnerIdAndType(ObjectModel):
    ownerId: UUID = ApiField(alias='ownerId')
    ownerType: Literal['SERVICE_ACCOUNT', 'TEAM', 'USER'] = ApiField(alias='ownerType')

class Page(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')

class Paging(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')

class ProviderConfigInformation(ObjectModel):
    api_key: str = ApiField(alias='api_key')
    endpoint: str = ApiField(alias='endpoint')

class ProviderInformation(ObjectModel):
    config: ProviderConfigInformation = ApiField(alias='config')
    inputs: List[ProviderInputInformation] = ApiField(alias='inputs', default_factory=list)
    type: str = ApiField(alias='type')

class ProviderInputInformation(ObjectModel):
    hosts: List[str] = ApiField(alias='hosts', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    subnet: str = ApiField(alias='subnet')
    type: str = ApiField(alias='type')

class RSAKeyTypeInformation(KeyTypeInformation):
    keyLengths: List[int] = ApiField(alias='keyLengths', default_factory=list)

class RecommendedSettingsInformation(ObjectModel):
    key: RecommendedSettingsKeyTypeInformation = ApiField(alias='key')
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValue: str = ApiField(alias='subjectCValue')
    subjectLValue: str = ApiField(alias='subjectLValue')
    subjectOUValue: str = ApiField(alias='subjectOUValue')
    subjectOValue: str = ApiField(alias='subjectOValue')
    subjectSTValue: str = ApiField(alias='subjectSTValue')

class RecommendedSettingsKeyTypeInformation(ObjectModel):
    curve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='curve')
    length: int = ApiField(alias='length')
    type: Literal['EC', 'RSA'] = ApiField(alias='type')

class Response(ObjectModel):
    allowedMethods: List[str] = ApiField(alias='allowedMethods', default_factory=list)
    closed: bool = ApiField(alias='closed')
    cookies: Dict[str, NewCookie] = ApiField(alias='cookies', default_factory=dict)
    date: datetime = ApiField(alias='date')
    entity: AnyValue = ApiField(alias='entity')
    entityTag: EntityTag = ApiField(alias='entityTag')
    headers: Dict[str, Any] = ApiField(alias='headers', default_factory=dict)
    language: Dict[str, Any] = ApiField(alias='language', default_factory=dict)
    lastModified: datetime = ApiField(alias='lastModified')
    length: int = ApiField(alias='length')
    links: List[Link] = ApiField(alias='links', default_factory=list)
    location: str = ApiField(alias='location')
    mediaType: MediaType = ApiField(alias='mediaType')
    metadata: Dict[str, Any] = ApiField(alias='metadata', default_factory=dict)
    status: int = ApiField(alias='status')
    statusInfo: StatusType = ApiField(alias='statusInfo')
    stringHeaders: Dict[str, Any] = ApiField(alias='stringHeaders', default_factory=dict)

class SavedSearchInfo(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    isDefault: bool = ApiField(alias='isDefault')
    name: str = ApiField(alias='name')
    searchDetails: FlattenedCertificateSavedSearch = ApiField(alias='searchDetails')
    type: Literal['FULL_TEXT', 'PREDEFINED_FILTER'] = ApiField(alias='type')
    userId: UUID = ApiField(alias='userId')

class SavedSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    isDefault: bool = ApiField(alias='isDefault')
    name: str = ApiField(alias='name')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')
    type: Literal['FULL_TEXT', 'PREDEFINED_FILTER'] = ApiField(alias='type')

class SavedSearchResponse(ObjectModel):
    savedSearchInfo: List[SavedSearchInfo] = ApiField(alias='savedSearchInfo', default_factory=list)

class ScanafiConfigResponseV1(ObjectModel):
    id: str = ApiField(alias='id')
    metadata: MetadataInformation = ApiField(alias='metadata')
    provider: ProviderInformation = ApiField(alias='provider')

class ServiceAccountInformation(ObjectModel):
    applications: List[UUID] = ApiField(alias='applications', default_factory=list)
    applicationsAdded: List[UUID] = ApiField(alias='applicationsAdded', default_factory=list)
    applicationsRemoved: List[UUID] = ApiField(alias='applicationsRemoved', default_factory=list)
    authType: str = ApiField(alias='authType')
    authenticationType: str = ApiField(alias='authenticationType')
    companyId: UUID = ApiField(alias='companyId')
    enabled: bool = ApiField(alias='enabled')
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    owner: UUID = ApiField(alias='owner')
    ownership: Dict[str, List[UUID]] = ApiField(alias='ownership', default_factory=dict)
    roles: List[str] = ApiField(alias='roles', default_factory=list)
    scopes: List[str] = ApiField(alias='scopes', default_factory=list)
    tenantId: UUID = ApiField(alias='tenantId')

class StatusType(ObjectModel):
    family: Literal['CLIENT_ERROR', 'INFORMATIONAL', 'OTHER', 'REDIRECTION', 'SERVER_ERROR', 'SUCCESSFUL'] = ApiField(
        alias='family'
    )
    reasonPhrase: str = ApiField(alias='reasonPhrase')
    statusCode: int = ApiField(alias='statusCode')

class SubjectAlternativeNamesByType(ObjectModel):
    dnsNames: List[str] = ApiField(alias='dnsNames', default_factory=list)
    ipAddresses: List[str] = ApiField(alias='ipAddresses', default_factory=list)
    rfc822Names: List[str] = ApiField(alias='rfc822Names', default_factory=list)
    uniformResourceIdentifiers: List[str] = ApiField(alias='uniformResourceIdentifiers', default_factory=list)

class TeamInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    members: List[UUID] = ApiField(alias='members', default_factory=list)
    name: str = ApiField(alias='name')
    owners: List[UUID] = ApiField(alias='owners', default_factory=list)
    ownership: Dict[str, List[UUID]] = ApiField(alias='ownership', default_factory=dict)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN', 'PKI_ADMIN',
    'PLATFORM_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)

class UnassignedCertificateAggregatesResponse(ObjectModel):
    certificateAggregatesMap: Dict[str, int] = ApiField(alias='certificateAggregatesMap', default_factory=dict)
    companyId: UUID = ApiField(alias='companyId')

class UriBuilder(ObjectModel):
    ...

class UserInformation(ObjectModel):
    admin: bool = ApiField(alias='admin')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    firstname: str = ApiField(alias='firstname')
    id: UUID = ApiField(alias='id')
    lastname: str = ApiField(alias='lastname')
    memberedTeams: List[UUID] = ApiField(alias='memberedTeams', default_factory=list)
    ownedTeams: List[UUID] = ApiField(alias='ownedTeams', default_factory=list)
    productRoles: Dict[str, List[Literal['DEVOPS_LEAD', 'DEVOPS_USER', 'GUEST', 'OUTAGEDETECTION_ADMIN', 'PKI_ADMIN',
    'PLATFORM_ADMIN', 'RESOURCE_OWNER', 'SECURITY_ADMIN']]] = ApiField(alias='productRoles', default_factory=dict)
    resourceOwner: bool = ApiField(alias='resourceOwner')
    serviceAccount: bool = ApiField(alias='serviceAccount')
    systemRoles: List[Literal['CONDOR_METRICS', 'SYSTEM_ADMIN']] = ApiField(alias='systemRoles', default_factory=list)
    teamsIds: List[UUID] = ApiField(alias='teamsIds', default_factory=list)
    userAccountType: str = ApiField(alias='userAccountType')
    userStatus: str = ApiField(alias='userStatus')
    userType: str = ApiField(alias='userType')
    username: str = ApiField(alias='username')

class CertificateExpirationInventoryMonitoringConfig(InventoryMonitoringConfig):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    enabled: bool = ApiField(alias='enabled')
    includeUnassignedCertificates: bool = ApiField(alias='includeUnassignedCertificates')
    thresholds: List[int] = ApiField(alias='thresholds', default_factory=list)

class CertificateExpirationInventoryMonitoringConfiguration(InventoryMonitoringConfiguration):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    enabled: bool = ApiField(alias='enabled')
    includeUnassignedCertificates: bool = ApiField(alias='includeUnassignedCertificates')
    thresholds: List[int] = ApiField(alias='thresholds', default_factory=list)

class ECKeyTypeInformation(KeyTypeInformation):
    keyCurves: List[Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN']] = ApiField(
        alias='keyCurves',
        default_factory=list
    )

ApiClientInformation.update_forward_refs()
ApplicationInformation.update_forward_refs()
ApplicationOwnership.update_forward_refs()
ApplicationRequest.update_forward_refs()
ApplicationResponse.update_forward_refs()
ApplicationsAssignRequest.update_forward_refs()
ApplicationsAssignResponse.update_forward_refs()
BaseFilter.update_forward_refs()
BaseOrdering.update_forward_refs()
Bucket.update_forward_refs()
CSRAttributesInformation.update_forward_refs()
CertificateAggregatesRangeResponse.update_forward_refs()
CertificateAggregatesResponse.update_forward_refs()
CertificateAggregationsRequest.update_forward_refs()
CertificateAuthorityProductInformation.update_forward_refs()
CertificateCategoryInformation.update_forward_refs()
CertificateDeletionRequest.update_forward_refs()
CertificateExpirationInventoryMonitoringConfig.update_forward_refs()
CertificateExpirationInventoryMonitoringConfiguration.update_forward_refs()
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
CertificateOwnership.update_forward_refs()
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
CertificateValidationResponse.update_forward_refs()
CertificationRequestInformation.update_forward_refs()
Condition.update_forward_refs()
CustomAttributes.update_forward_refs()
CustomAttributesInformation.update_forward_refs()
ECKeyTypeInformation.update_forward_refs()
EntityTag.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Expression.update_forward_refs()
ExtendedApplicationOwnership.update_forward_refs()
ExtendedCertificateInformation.update_forward_refs()
ExtendedCertificateInstanceInformation.update_forward_refs()
ExtendedCertificateInstanceResponse.update_forward_refs()
Facet.update_forward_refs()
FacetResponse.update_forward_refs()
Filter.update_forward_refs()
FilterOperand.update_forward_refs()
FilterOperands.update_forward_refs()
FlattenedCertificateSavedSearch.update_forward_refs()
GeneralNamesData.update_forward_refs()
ImportedCertificateInformation.update_forward_refs()
InventoryMonitoringConfig.update_forward_refs()
InventoryMonitoringConfigRequest.update_forward_refs()
InventoryMonitoringConfiguration.update_forward_refs()
InventoryMonitoringConfigurationRequest.update_forward_refs()
InventoryMonitoringConfigurationResponse.update_forward_refs()
InventoryMonitoringSchedulerInformation.update_forward_refs()
InvitationInformation.update_forward_refs()
InvitationRequest.update_forward_refs()
InvitationResponse.update_forward_refs()
KeyTypeInformation.update_forward_refs()
KeyTypeParameters.update_forward_refs()
Link.update_forward_refs()
MediaType.update_forward_refs()
MetadataInformation.update_forward_refs()
MultivaluedMapStringObject.update_forward_refs()
MultivaluedMapStringString.update_forward_refs()
NestedBucket.update_forward_refs()
NestedFacet.update_forward_refs()
NewCookie.update_forward_refs()
Order.update_forward_refs()
OrderObject.update_forward_refs()
Ordering.update_forward_refs()
OwnerIdAndType.update_forward_refs()
Page.update_forward_refs()
Paging.update_forward_refs()
ProviderConfigInformation.update_forward_refs()
ProviderInformation.update_forward_refs()
ProviderInputInformation.update_forward_refs()
RSAKeyTypeInformation.update_forward_refs()
RecommendedSettingsInformation.update_forward_refs()
RecommendedSettingsKeyTypeInformation.update_forward_refs()
Response.update_forward_refs()
SavedSearchInfo.update_forward_refs()
SavedSearchRequest.update_forward_refs()
SavedSearchResponse.update_forward_refs()
ScanafiConfigResponseV1.update_forward_refs()
ServiceAccountInformation.update_forward_refs()
StatusType.update_forward_refs()
SubjectAlternativeNamesByType.update_forward_refs()
TeamInformation.update_forward_refs()
UnassignedCertificateAggregatesResponse.update_forward_refs()
UriBuilder.update_forward_refs()
UserInformation.update_forward_refs()
