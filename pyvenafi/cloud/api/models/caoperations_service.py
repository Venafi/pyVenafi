from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class CAAccountConfigurationInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class CAAccountImportConfigurationInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class CaOperationRequest(ObjectModel):
    operation: str = ApiField(alias='operation')


class CancelCaEditOperationRequest(CaOperationRequest):
    pass


class CertificateAuthorityAccountConfigurationRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')


class CertificateAuthorityAccountDeleteResponse(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    id: UUID = ApiField(alias='id')
    key: str = ApiField(alias='key')


class CertificateAuthorityAccountDetails(ObjectModel):
    domainsDetails: List[CertificateAuthorityDomainDetails] = ApiField(alias='domainsDetails', default_factory=list)


class CertificateAuthorityAccountDomainInformation(ObjectModel):
    pass


class CertificateAuthorityAccountDomainRequest(ObjectModel):
    domain: str = ApiField(alias='domain')
    domainAction: Literal['ASSERT_DOMAIN_OVER_DNS', 'DELETE', 'SUBMIT'] = ApiField(alias='domainAction')
    identifier: str = ApiField(alias='identifier')


class CertificateAuthorityAccountImportOptionRequest(ObjectModel):
    importDetails: CertificateAuthorityImportDetailsInformation = ApiField(alias='importDetails')


class CertificateAuthorityAccountImportOptionResponse(ObjectModel):
    certificateAuthorityImportOptions: List[CertificateAuthorityImportOptionInformation] = ApiField(
        alias='certificateAuthorityImportOptions', default_factory=list)


class CertificateAuthorityAccountInformation(ObjectModel):
    accountDetails: CertificateAuthorityAccountDetails = ApiField(alias='accountDetails')
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    companyId: UUID = ApiField(alias='companyId')
    connectionStatus: Literal['FAILED', 'OK'] = ApiField(alias='connectionStatus')
    creationDate: datetime = ApiField(alias='creationDate')
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    id: UUID = ApiField(alias='id')
    importConfiguration: ImportConfigurationDetails = ApiField(alias='importConfiguration')
    importSchedulerEnabled: bool = ApiField(alias='importSchedulerEnabled')
    importSchedulerPattern: SchedulerPatternInformation = ApiField(alias='importSchedulerPattern')
    importStatus: Literal['ABORTED', 'COMPLETE', 'FAILED', 'PENDING', 'RUNNING'] = ApiField(alias='importStatus')
    key: str = ApiField(alias='key')
    lastImportEndDate: datetime = ApiField(alias='lastImportEndDate')
    lastImportRunId: UUID = ApiField(alias='lastImportRunId')
    lastImportStartDate: datetime = ApiField(alias='lastImportStartDate')
    lastTestDate: datetime = ApiField(alias='lastTestDate')
    lastTestError: str = ApiField(alias='lastTestError')
    lastTestSuccessDate: datetime = ApiField(alias='lastTestSuccessDate')
    modificationDate: datetime = ApiField(alias='modificationDate')


class CertificateAuthorityAccountRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    caAccountImportOptions: List[CertificateAuthorityImportDetailsInformation] = ApiField(alias='caAccountImportOptions', default_factory=list)
    caAccountProductOptions: List[CertificateAuthorityProductDetailsInformation] = ApiField(
        alias='caAccountProductOptions', default_factory=list)
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    importConfiguration: CAAccountImportConfigurationInformation = ApiField(alias='importConfiguration')
    importSchedulerEnabled: bool = ApiField(alias='importSchedulerEnabled')
    importSchedulerPattern: SchedulerPatternInformation = ApiField(alias='importSchedulerPattern')
    key: str = ApiField(alias='key')


class CertificateAuthorityAccountResponse(ObjectModel):
    accounts: List[ExtendedCertificateAuthorityAccountInformation] = ApiField(alias='accounts', default_factory=list)


class CertificateAuthorityAccountUpdateRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    caAccountImportOptions: List[CertificateAuthorityImportDetailsInformation] = ApiField(alias='caAccountImportOptions', default_factory=list)
    caAccountProductOptions: List[CertificateAuthorityProductDetailsInformation] = ApiField(
        alias='caAccountProductOptions', default_factory=list)
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    importConfiguration: CAAccountImportConfigurationInformation = ApiField(alias='importConfiguration')
    importSchedulerEnabled: bool = ApiField(alias='importSchedulerEnabled')
    importSchedulerPattern: SchedulerPatternInformation = ApiField(alias='importSchedulerPattern')
    key: str = ApiField(alias='key')


class CertificateAuthorityApiInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityApi: Literal['ACME', 'BUILTIN_CA', 'DIGICERT_TEST', 'ENTRUST', 'GLOBALSIGN_HVCA_V2',
                                     'GLOBALSIGN_MSSL', 'MICROSOFT', 'MOCKCA_TEST', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthorityApi')
    credentialsTemplate: CertificateAuthorityCredentials = ApiField(alias='credentialsTemplate')
    urlTemplate: str = ApiField(alias='urlTemplate')


class CertificateAuthorityCredentials(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class CertificateAuthorityCredentialsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class CertificateAuthorityCredentialsRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')


class CertificateAuthorityDomainDetails(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    domain: str = ApiField(alias='domain')
    identifier: str = ApiField(alias='identifier')
    status: Literal['INVALID', 'PENDING', 'REQUESTED', 'VALID'] = ApiField(alias='status')


class CertificateAuthorityImportDetailsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class CertificateAuthorityImportOptionInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    id: UUID = ApiField(alias='id')
    importDetails: CertificateAuthorityImportDetailsInformation = ApiField(alias='importDetails')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['ABORTED', 'COMPLETE', 'FAILED', 'PENDING', 'RUNNING'] = ApiField(alias='status')


class CertificateAuthorityInformation(ObjectModel):
    apis: List[CertificateAuthorityApiInformation] = ApiField(alias='apis', default_factory=list)
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')


class CertificateAuthorityProductDetailsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    certificateType: Literal['DOMAIN_VALIDATED_SSL', 'OTHER'] = ApiField(alias='certificateType')
    hashAlgorithms: List[Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224', 'SHA256',
                                 'SHA384', 'SHA512', 'UNKNOWN']] = ApiField(alias='hashAlgorithms', default_factory=list)
    productName: str = ApiField(alias='productName')
    productTemplate: CertificateAuthorityProductInformation = ApiField(alias='productTemplate')


class CertificateAuthorityProductInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    certificateType: Literal['DOMAIN_VALIDATED_SSL', 'OTHER'] = ApiField(alias='certificateType')
    hashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                           'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='hashAlgorithm')
    productName: str = ApiField(alias='productName')
    validityPeriod: str = ApiField(alias='validityPeriod')


class CertificateAuthorityProductOptionInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    modificationDate: datetime = ApiField(alias='modificationDate')
    productDetails: CertificateAuthorityProductDetailsInformation = ApiField(alias='productDetails')
    productName: str = ApiField(alias='productName')


class CertificateAuthorityProductOptionRequest(ObjectModel):
    caProduct: CertificateAuthorityProductDetailsInformation = ApiField(alias='caProduct')


class CertificateAuthorityProductOptionResponse(ObjectModel):
    productOptions: List[CertificateAuthorityProductOptionInformation] = ApiField(alias='productOptions', default_factory=list)


class CertificateAuthorityProductOptionsTestIssuanceRequest(ObjectModel):
    productOptions: List[ProductOptionTestIssuanceInformation] = ApiField(alias='productOptions', default_factory=list)


class CertificateAuthorityProductOptionsTestIssuanceResultsResponse(ObjectModel):
    productOptionsResults: List[ProductOptionTestIssuanceInformation] = ApiField(alias='productOptionsResults', default_factory=list)


class CertificateAuthorityResponse(ObjectModel):
    certificateAuthorities: List[CertificateAuthorityInformation] = ApiField(alias='certificateAuthorities', default_factory=list)


class CertificateAuthorityTestConnectionRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')


class CertificateImportRequest(ObjectModel):
    certificateImportAction: Literal['ABORT', 'START'] = ApiField(alias='certificateImportAction')


class CertificateInformation(ObjectModel):
    keySize: int = ApiField(alias='keySize')
    keyType: Literal['EC', 'RSA'] = ApiField(alias='keyType')
    subjectC: str = ApiField(alias='subjectC')
    subjectCN: str = ApiField(alias='subjectCN')
    subjectL: str = ApiField(alias='subjectL')
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: str = ApiField(alias='subjectOU')
    subjectST: str = ApiField(alias='subjectST')


class CertificateIssuingTemplateDeleteResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')


class CertificateIssuingTemplateInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    extendedKeyUsageValues: List[Literal['CLIENT', 'SERVER']] = ApiField(alias='extendedKeyUsageValues', default_factory=list)
    id: UUID = ApiField(alias='id')
    keyGeneratedByVenafiAllowed: bool = ApiField(alias='keyGeneratedByVenafiAllowed')
    keyReuse: bool = ApiField(alias='keyReuse')
    keyTypes: List[KeyTypeInformation] = ApiField(alias='keyTypes', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    priority: int = ApiField(alias='priority')
    product: CertificateAuthorityProductInformation = ApiField(alias='product')
    reason: str = ApiField(alias='reason')
    recommendedSettings: RecommendedSettingsInformation = ApiField(alias='recommendedSettings')
    referencingApplicationIds: List[UUID] = ApiField(alias='referencingApplicationIds', default_factory=list)
    resourceConsumerTeamIds: List[UUID] = ApiField(alias='resourceConsumerTeamIds', default_factory=list)
    resourceConsumerUserIds: List[UUID] = ApiField(alias='resourceConsumerUserIds', default_factory=list)
    sanDnsNameRegexes: List[str] = ApiField(alias='sanDnsNameRegexes', default_factory=list)
    sanIpAddressRegexes: List[str] = ApiField(alias='sanIpAddressRegexes', default_factory=list)
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    sanRfc822NameRegexes: List[str] = ApiField(alias='sanRfc822NameRegexes', default_factory=list)
    sanUniformResourceIdentifierRegexes: List[str] = ApiField(alias='sanUniformResourceIdentifierRegexes', default_factory=list)
    status: Literal['AVAILABLE', 'UNAVAILABLE'] = ApiField(alias='status')
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValues: List[str] = ApiField(alias='subjectCValues', default_factory=list)
    subjectLRegexes: List[str] = ApiField(alias='subjectLRegexes', default_factory=list)
    subjectORegexes: List[str] = ApiField(alias='subjectORegexes', default_factory=list)
    subjectOURegexes: List[str] = ApiField(alias='subjectOURegexes', default_factory=list)
    subjectSTRegexes: List[str] = ApiField(alias='subjectSTRegexes', default_factory=list)
    systemGenerated: bool = ApiField(alias='systemGenerated')
    trackingData: TrackingDataInformation = ApiField(alias='trackingData')


class CertificateIssuingTemplateRequest(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
                                  'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    extendedKeyUsageValues: List[Literal['CLIENT', 'SERVER']] = ApiField(alias='extendedKeyUsageValues', default_factory=list)
    keyGeneratedByVenafiAllowed: bool = ApiField(alias='keyGeneratedByVenafiAllowed')
    keyReuse: bool = ApiField(alias='keyReuse')
    keyTypes: List[KeyTypeParameters] = ApiField(alias='keyTypes', default_factory=list)
    name: str = ApiField(alias='name')
    priority: int = ApiField(alias='priority')
    product: CertificateAuthorityProductInformation = ApiField(alias='product')
    recommendedSettings: RecommendedSettingsRequest = ApiField(alias='recommendedSettings')
    resourceConsumerTeamIds: List[UUID] = ApiField(alias='resourceConsumerTeamIds', default_factory=list)
    resourceConsumerUserIds: List[UUID] = ApiField(alias='resourceConsumerUserIds', default_factory=list)
    sanIpAddressRegexes: List[str] = ApiField(alias='sanIpAddressRegexes', default_factory=list)
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    sanRfc822NameRegexes: List[str] = ApiField(alias='sanRfc822NameRegexes', default_factory=list)
    sanUniformResourceIdentifierRegexes: List[str] = ApiField(alias='sanUniformResourceIdentifierRegexes', default_factory=list)
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValues: List[str] = ApiField(alias='subjectCValues', default_factory=list)
    subjectLRegexes: List[str] = ApiField(alias='subjectLRegexes', default_factory=list)
    subjectORegexes: List[str] = ApiField(alias='subjectORegexes', default_factory=list)
    subjectOURegexes: List[str] = ApiField(alias='subjectOURegexes', default_factory=list)
    subjectSTRegexes: List[str] = ApiField(alias='subjectSTRegexes', default_factory=list)
    trackingData: TrackingDataInformation = ApiField(alias='trackingData')


class CertificateIssuingTemplateResponse(ObjectModel):
    certificateIssuingTemplates: List[CertificateIssuingTemplateInformation] = ApiField(
        alias='certificateIssuingTemplates', default_factory=list)


class CertificateIssuingTemplateRulesInformation(ObjectModel):
    commonName: StringList = ApiField(alias='commonName')
    country: StringField = ApiField(alias='country')
    keySizes: List[int] = ApiField(alias='keySizes', default_factory=list)
    keyType: str = ApiField(alias='keyType')
    locality: StringField = ApiField(alias='locality')
    organization: StringField = ApiField(alias='organization')
    organizationalUnit: StringList = ApiField(alias='organizationalUnit')
    state: StringField = ApiField(alias='state')
    subjectAlternativeNames: List[str] = ApiField(alias='subjectAlternativeNames', default_factory=list)


class ClientCredentials(ObjectModel):
    apiKey: str = ApiField(alias='apiKey')
    secret: str = ApiField(alias='secret')


class DigicertCredentials(CertificateAuthorityCredentials):
    apiKey: str = ApiField(alias='apiKey')


class DigicertCredentialsInformation(CertificateAuthorityCredentialsInformation):
    apiKey: str = ApiField(alias='apiKey')


class DigicertProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    allowAutoRenew: bool = ApiField(alias='allowAutoRenew')
    defaultHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
                                  'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='defaultHashAlgorithm')
    organizationIds: List[int] = ApiField(alias='organizationIds', default_factory=list)
    productFriendlyName: str = ApiField(alias='productFriendlyName')


class DigicertProductInformation(CertificateAuthorityProductInformation):
    autoRenew: bool = ApiField(alias='autoRenew')
    organizationId: int = ApiField(alias='organizationId')


class DnComponentInformation(ObjectModel):
    label: str = ApiField(alias='label')
    modifiable: bool = ApiField(alias='modifiable')
    required: bool = ApiField(alias='required')
    tag: str = ApiField(alias='tag')


class DnsMethod(ObjectModel):
    recordDomain: str = ApiField(alias='recordDomain')
    recordType: str = ApiField(alias='recordType')
    recordValue: str = ApiField(alias='recordValue')


class DnsProviderInformation(ObjectModel):
    dekId: str = ApiField(alias='dekId')
    dnsProviderType: str = ApiField(alias='dnsProviderType')


class DurationFieldType(ObjectModel):
    name: str = ApiField(alias='name')


class EntrustCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    clientId: int = ApiField(alias='clientId')


class EntrustCredentials(CertificateAuthorityCredentials):
    key: str = ApiField(alias='key')
    keyPassword: str = ApiField(alias='keyPassword')
    keyStoreBase64: str = ApiField(alias='keyStoreBase64')
    keyStorePassword: str = ApiField(alias='keyStorePassword')
    username: str = ApiField(alias='username')


class EntrustCredentialsInformation(CertificateAuthorityCredentialsInformation):
    key: str = ApiField(alias='key')
    keyPassword: str = ApiField(alias='keyPassword')
    keyStoreBase64: str = ApiField(alias='keyStoreBase64')
    keyStorePassword: str = ApiField(alias='keyStorePassword')
    username: str = ApiField(alias='username')


class EntrustDomainDetails(CertificateAuthorityDomainDetails):
    clientId: int = ApiField(alias='clientId')
    dnsMethod: DnsMethod = ApiField(alias='dnsMethod')
    emailMethod: List[str] = ApiField(alias='emailMethod', default_factory=list)
    evEligible: bool = ApiField(alias='evEligible')
    evExpiryDate: datetime = ApiField(alias='evExpiryDate')
    ovEligible: bool = ApiField(alias='ovEligible')
    ovExpiryDate: datetime = ApiField(alias='ovExpiryDate')
    validationMethod: str = ApiField(alias='validationMethod')
    webServerMethod: WebServerMethod = ApiField(alias='webServerMethod')


class EntrustProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    pass


class EntrustProductInformation(CertificateAuthorityProductInformation):
    pass


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class ExtendedCertificateAuthorityAccountInformation(ObjectModel):
    account: CertificateAuthorityAccountInformation = ApiField(alias='account')
    importOptions: List[CertificateAuthorityImportOptionInformation] = ApiField(alias='importOptions', default_factory=list)
    productOptions: List[CertificateAuthorityProductOptionInformation] = ApiField(alias='productOptions', default_factory=list)


class GenerateCaCSROperationRequest(CaOperationRequest):
    intermediateProps: CertificateInformation = ApiField(alias='intermediateProps')


class GlobalSignCredentials(CertificateAuthorityCredentials):
    clientCredentials: ClientCredentials = ApiField(alias='clientCredentials')
    credentials: str = ApiField(alias='credentials')


class GlobalSignCredentialsInformation(CertificateAuthorityCredentialsInformation):
    credentials: str = ApiField(alias='credentials')


class GlobalSignDomainDetails(CertificateAuthorityDomainDetails):
    assertBy: datetime = ApiField(alias='assertBy')
    claimId: str = ApiField(alias='claimId')
    createdAt: datetime = ApiField(alias='createdAt')
    expiresAt: datetime = ApiField(alias='expiresAt')
    log: List[GlobalSignLogEntry] = ApiField(alias='log', default_factory=list)
    validationToken: str = ApiField(alias='validationToken')


class GlobalSignLogEntry(ObjectModel):
    description: str = ApiField(alias='description')
    status: Literal['ERROR', 'SUCCESS'] = ApiField(alias='status')
    timestamp: datetime = ApiField(alias='timestamp')


class GlobalSignMSSLCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    connectTestServer: bool = ApiField(alias='connectTestServer')
    profileId: str = ApiField(alias='profileId')


class GlobalSignMSSLCredentials(CertificateAuthorityCredentials):
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')


class GlobalSignMSSLCredentialsInformation(CertificateAuthorityCredentialsInformation):
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')


class GlobalSignMSSLDomainDetails(CertificateAuthorityDomainDetails):
    domainId: str = ApiField(alias='domainId')


class GlobalSignMSSLProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    productFriendlyName: str = ApiField(alias='productFriendlyName')


class GlobalSignMSSLProductInformation(CertificateAuthorityProductInformation):
    pass


class GlobalSignProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    pass


class GlobalSignProductInformation(CertificateAuthorityProductInformation):
    pass


class GoogleCloudDnsProviderInformation(DnsProviderInformation):
    clientEmail: str = ApiField(alias='clientEmail')
    privateKey: str = ApiField(alias='privateKey')
    privateKeyId: str = ApiField(alias='privateKeyId')
    projectId: str = ApiField(alias='projectId')
    tokenUri: str = ApiField(alias='tokenUri')


class ImportConfigurationDetails(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    includeExpiredCertificates: bool = ApiField(alias='includeExpiredCertificates')
    includeRevokedCertificates: bool = ApiField(alias='includeRevokedCertificates')


class KeyTypeInformation(ObjectModel):
    keyType: str = ApiField(alias='keyType')


class KeyTypeParameters(ObjectModel):
    keyCurves: List[Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN']] = ApiField(alias='keyCurves', default_factory=list)
    keyLengths: List[int] = ApiField(alias='keyLengths', default_factory=list)
    keyType: Literal['EC', 'RSA'] = ApiField(alias='keyType')


class MicrosoftCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    address: str = ApiField(alias='address')
    serviceName: str = ApiField(alias='serviceName')
    workerId: UUID = ApiField(alias='workerId')


class MicrosoftCAAccountImportConfigurationInformation(CAAccountImportConfigurationInformation):
    includeExpiredCertificates: bool = ApiField(alias='includeExpiredCertificates')
    includeRevokedCertificates: bool = ApiField(alias='includeRevokedCertificates')


class MicrosoftCAImportDetailsInformation(CertificateAuthorityImportDetailsInformation):
    name: str = ApiField(alias='name')
    oid: str = ApiField(alias='oid')


class MicrosoftCredentials(CertificateAuthorityCredentials):
    dekId: str = ApiField(alias='dekId')
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')


class MicrosoftCredentialsInformation(CertificateAuthorityCredentialsInformation):
    dekId: str = ApiField(alias='dekId')
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')


class MicrosoftImportConfigurationDetails(ImportConfigurationDetails):
    pass


class MicrosoftProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    oid: str = ApiField(alias='oid')
    status: Literal['FAILED', 'IN_PROGRESS', 'OK', 'PENDING'] = ApiField(alias='status')


class MicrosoftProductInformation(CertificateAuthorityProductInformation):
    templateOid: str = ApiField(alias='templateOid')


class MockCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    someId: int = ApiField(alias='someId')
    someName: str = ApiField(alias='someName')


class MockCACredentials(CertificateAuthorityCredentials):
    apiKey: str = ApiField(alias='apiKey')


class MockCACredentialsInformation(CertificateAuthorityCredentialsInformation):
    apiKey: str = ApiField(alias='apiKey')


class MockCADomainDetails(CertificateAuthorityDomainDetails):
    pass


class MockCAImportConfiguration(ImportConfigurationDetails):
    pass


class MockCAProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    signatureAlgorithms: List[Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                      'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1']] = ApiField(alias='signatureAlgorithms', default_factory=list)


class MockCAProductInformation(CertificateAuthorityProductInformation):
    signatureAlgorithm: Literal['EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
                                'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(alias='signatureAlgorithm')


class NewCaCertificatesOperationRequest(CaOperationRequest):
    intermediateProps: CertificateInformation = ApiField(alias='intermediateProps')
    rootProps: CertificateInformation = ApiField(alias='rootProps')


class Period(ObjectModel):
    days: int = ApiField(alias='days')
    fieldTypes: List[DurationFieldType] = ApiField(alias='fieldTypes', default_factory=list)
    hours: int = ApiField(alias='hours')
    millis: int = ApiField(alias='millis')
    minutes: int = ApiField(alias='minutes')
    months: int = ApiField(alias='months')
    period: ReadablePeriod = ApiField(alias='period')
    periodInternal: ReadablePeriod = ApiField(alias='periodInternal')
    periodType: PeriodType = ApiField(alias='periodType')
    seconds: int = ApiField(alias='seconds')
    values: List[int] = ApiField(alias='values', default_factory=list)
    weeks: int = ApiField(alias='weeks')
    years: int = ApiField(alias='years')


class PeriodType(ObjectModel):
    name: str = ApiField(alias='name')


class ProductOptionTestIssuanceInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    status: Literal['FAILED', 'IN_PROGRESS', 'OK', 'PENDING'] = ApiField(alias='status')


class RSAKeyTypeInformation(KeyTypeInformation):
    keyLengths: List[int] = ApiField(alias='keyLengths', default_factory=list)


class ReadablePeriod(ObjectModel):
    periodType: PeriodType = ApiField(alias='periodType')


class RecommendedSettingsInformation(ObjectModel):
    key: RecommendedSettingsKeyTypeInformation = ApiField(alias='key')
    keyGeneratedBy: str = ApiField(alias='keyGeneratedBy')
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


class RecommendedSettingsKeyTypeParameter(ObjectModel):
    curve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='curve')
    length: int = ApiField(alias='length')
    type: Literal['EC', 'RSA'] = ApiField(alias='type')


class RecommendedSettingsRequest(ObjectModel):
    key: RecommendedSettingsKeyTypeParameter = ApiField(alias='key')
    keyGeneratedBy: str = ApiField(alias='keyGeneratedBy')
    sanRegexes: List[str] = ApiField(alias='sanRegexes', default_factory=list)
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValue: str = ApiField(alias='subjectCValue')
    subjectLValue: str = ApiField(alias='subjectLValue')
    subjectOUValue: str = ApiField(alias='subjectOUValue')
    subjectOValue: str = ApiField(alias='subjectOValue')
    subjectSTValue: str = ApiField(alias='subjectSTValue')


class SchedulerPatternInformation(ObjectModel):
    recurrenceType: str = ApiField(alias='recurrenceType')


class StringField(ObjectModel):
    format: str = ApiField(alias='format')
    presence: str = ApiField(alias='presence')


class StringList(ObjectModel):
    format: List[str] = ApiField(alias='format', default_factory=list)
    presence: str = ApiField(alias='presence')


class SubjectAltNamesInformation(ObjectModel):
    label: str = ApiField(alias='label')
    modifiable: bool = ApiField(alias='modifiable')
    required: bool = ApiField(alias='required')
    tag: str = ApiField(alias='tag')


class TppCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    clientId: str = ApiField(alias='clientId')
    hostnameOrAddress: str = ApiField(alias='hostnameOrAddress')
    pluginId: UUID = ApiField(alias='pluginId')


class TppCredentials(CertificateAuthorityCredentials):
    accessToken: str = ApiField(alias='accessToken')
    dekId: str = ApiField(alias='dekId')
    expires: datetime = ApiField(alias='expires')
    refreshToken: str = ApiField(alias='refreshToken')
    refreshUntil: datetime = ApiField(alias='refreshUntil')


class TppCredentialsInformation(CertificateAuthorityCredentialsInformation):
    dekId: str = ApiField(alias='dekId')
    expires: datetime = ApiField(alias='expires')
    refreshToken: str = ApiField(alias='refreshToken')
    refreshUntil: datetime = ApiField(alias='refreshUntil')


class TppProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    pass


class TppProductInformation(CertificateAuthorityProductInformation):
    pass


class TrackingDataInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')


class UploadCaCertificateOperationRequest(CaOperationRequest):
    pemCertificates: str = ApiField(alias='pemCertificates')


class ValidityInformation(ObjectModel):
    defaultValue: Period = ApiField(alias='defaultValue')
    maxValue: Period = ApiField(alias='maxValue')


class WebServerMethod(ObjectModel):
    fileContents: str = ApiField(alias='fileContents')
    fileLocation: str = ApiField(alias='fileLocation')


class WeeklyPatternInformation(SchedulerPatternInformation):
    daysOfWeek: List[Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY',
                             'TUESDAY', 'WEDNESDAY']] = ApiField(alias='daysOfWeek', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')


class ZtpkiCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    serverUrl: str = ApiField(alias='serverUrl')


class ZtpkiCredentials(CertificateAuthorityCredentials):
    keyId: str = ApiField(alias='keyId')
    macKey: str = ApiField(alias='macKey')


class ZtpkiCredentialsInformation(CertificateAuthorityCredentialsInformation):
    keyId: str = ApiField(alias='keyId')
    macKey: str = ApiField(alias='macKey')


class ZtpkiProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    approvalRequired: bool = ApiField(alias='approvalRequired')
    certificateAuthorityId: str = ApiField(alias='certificateAuthorityId')
    dnComponents: List[DnComponentInformation] = ApiField(alias='dnComponents', default_factory=list)
    id: str = ApiField(alias='id')
    organizationId: str = ApiField(alias='organizationId')
    sans: List[SubjectAltNamesInformation] = ApiField(alias='sans', default_factory=list)
    validity: ValidityInformation = ApiField(alias='validity')


class ZtpkiProductInformation(CertificateAuthorityProductInformation):
    days: List[str] = ApiField(alias='days', default_factory=list)
    maxValidityPeriod: Period = ApiField(alias='maxValidityPeriod')
    months: List[str] = ApiField(alias='months', default_factory=list)
    policyId: str = ApiField(alias='policyId')
    years: List[str] = ApiField(alias='years', default_factory=list)


class AcmeCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    caType: Literal['CUSTOM', 'GO_DADDY', 'LETS_ENCRYPT', 'SECTIGO', 'ZERO_TOUCH_PKI'] = ApiField(alias='caType')
    directoryUrl: str = ApiField(alias='directoryUrl')
    dnsProvider: DnsProviderInformation = ApiField(alias='dnsProvider')
    logo: str = ApiField(alias='logo')
    termsOfServiceAgreed: bool = ApiField(alias='termsOfServiceAgreed')
    useDnsProvider: bool = ApiField(alias='useDnsProvider')


class AcmeCredentials(CertificateAuthorityCredentials):
    dekId: str = ApiField(alias='dekId')
    emailAddresses: List[str] = ApiField(alias='emailAddresses', default_factory=list)
    keyId: str = ApiField(alias='keyId')
    macKey: str = ApiField(alias='macKey')
    privateKey: Dict[str, Any] = ApiField(alias='privateKey', default_factory=dict)


class AcmeCredentialsInformation(CertificateAuthorityCredentialsInformation):
    dekId: str = ApiField(alias='dekId')
    emailAddresses: List[str] = ApiField(alias='emailAddresses', default_factory=list)
    keyId: str = ApiField(alias='keyId')
    macKey: str = ApiField(alias='macKey')


class AcmeProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    pass


class AcmeProductInformation(CertificateAuthorityProductInformation):
    pass


class AkamaiDnsProviderInformation(DnsProviderInformation):
    accessToken: str = ApiField(alias='accessToken')
    clientSecret: str = ApiField(alias='clientSecret')
    clientToken: str = ApiField(alias='clientToken')
    host: str = ApiField(alias='host')


class AwsRoute53DnsProviderInformation(DnsProviderInformation):
    accessKeyId: str = ApiField(alias='accessKeyId')
    hostedZoneId: str = ApiField(alias='hostedZoneId')
    secretAccessKey: str = ApiField(alias='secretAccessKey')


class AzureDnsProviderInformation(DnsProviderInformation):
    clientId: str = ApiField(alias='clientId')
    clientSecret: str = ApiField(alias='clientSecret')
    resourceGroup: str = ApiField(alias='resourceGroup')
    subscriptionId: str = ApiField(alias='subscriptionId')
    tenantId: str = ApiField(alias='tenantId')


class BuiltInCAProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    pass


class BuiltInCAProductInformation(CertificateAuthorityProductInformation):
    pass


class CloudFlareDnsProviderInformation(DnsProviderInformation):
    apiKey: str = ApiField(alias='apiKey')
    dnsApiToken: str = ApiField(alias='dnsApiToken')
    email: str = ApiField(alias='email')
    zoneApiToken: str = ApiField(alias='zoneApiToken')


class CronPatternInformation(SchedulerPatternInformation):
    cronExpression: str = ApiField(alias='cronExpression')


class DigitalOceanDnsProviderInformation(DnsProviderInformation):
    authenticationToken: str = ApiField(alias='authenticationToken')


class ECKeyTypeInformation(KeyTypeInformation):
    keyCurves: List[Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN']] = ApiField(alias='keyCurves', default_factory=list)


class EntrustTrackingDataInformation(TrackingDataInformation):
    requesterEmail: str = ApiField(alias='requesterEmail')
    requesterName: str = ApiField(alias='requesterName')
    requesterPhone: str = ApiField(alias='requesterPhone')


class GlobalSignMSSLTrackingDataInformation(TrackingDataInformation):
    requesterEmail: str = ApiField(alias='requesterEmail')
    requesterFirstName: str = ApiField(alias='requesterFirstName')
    requesterLastName: str = ApiField(alias='requesterLastName')
    requesterPhone: str = ApiField(alias='requesterPhone')


class MicrosoftProductOptionTestIssuanceInformation(ProductOptionTestIssuanceInformation):
    name: str = ApiField(alias='name')
    oid: str = ApiField(alias='oid')


class MockCAProductOptionTestIssuanceInformation(ProductOptionTestIssuanceInformation):
    pass


class MockCATrackingDataInformation(TrackingDataInformation):
    requesterName: str = ApiField(alias='requesterName')


class MonthlyPatternInformation(SchedulerPatternInformation):
    daysOfMonth: List[Literal['D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25',
                              'D26', 'D27', 'D28', 'D29', 'D3', 'D30', 'D31', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'L', 'LW']] = ApiField(alias='daysOfMonth', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')


AcmeCAAccountConfigurationInformation.update_forward_refs()
AcmeCredentials.update_forward_refs()
AcmeCredentialsInformation.update_forward_refs()
AcmeProductDetailsInformation.update_forward_refs()
AcmeProductInformation.update_forward_refs()
AkamaiDnsProviderInformation.update_forward_refs()
AwsRoute53DnsProviderInformation.update_forward_refs()
AzureDnsProviderInformation.update_forward_refs()
BuiltInCAProductDetailsInformation.update_forward_refs()
BuiltInCAProductInformation.update_forward_refs()
CAAccountConfigurationInformation.update_forward_refs()
CAAccountImportConfigurationInformation.update_forward_refs()
CaOperationRequest.update_forward_refs()
CancelCaEditOperationRequest.update_forward_refs()
CertificateAuthorityAccountConfigurationRequest.update_forward_refs()
CertificateAuthorityAccountDeleteResponse.update_forward_refs()
CertificateAuthorityAccountDetails.update_forward_refs()
CertificateAuthorityAccountDomainInformation.update_forward_refs()
CertificateAuthorityAccountDomainRequest.update_forward_refs()
CertificateAuthorityAccountImportOptionRequest.update_forward_refs()
CertificateAuthorityAccountImportOptionResponse.update_forward_refs()
CertificateAuthorityAccountInformation.update_forward_refs()
CertificateAuthorityAccountRequest.update_forward_refs()
CertificateAuthorityAccountResponse.update_forward_refs()
CertificateAuthorityAccountUpdateRequest.update_forward_refs()
CertificateAuthorityApiInformation.update_forward_refs()
CertificateAuthorityCredentials.update_forward_refs()
CertificateAuthorityCredentialsInformation.update_forward_refs()
CertificateAuthorityCredentialsRequest.update_forward_refs()
CertificateAuthorityDomainDetails.update_forward_refs()
CertificateAuthorityImportDetailsInformation.update_forward_refs()
CertificateAuthorityImportOptionInformation.update_forward_refs()
CertificateAuthorityInformation.update_forward_refs()
CertificateAuthorityProductDetailsInformation.update_forward_refs()
CertificateAuthorityProductInformation.update_forward_refs()
CertificateAuthorityProductOptionInformation.update_forward_refs()
CertificateAuthorityProductOptionRequest.update_forward_refs()
CertificateAuthorityProductOptionResponse.update_forward_refs()
CertificateAuthorityProductOptionsTestIssuanceRequest.update_forward_refs()
CertificateAuthorityProductOptionsTestIssuanceResultsResponse.update_forward_refs()
CertificateAuthorityResponse.update_forward_refs()
CertificateAuthorityTestConnectionRequest.update_forward_refs()
CertificateImportRequest.update_forward_refs()
CertificateInformation.update_forward_refs()
CertificateIssuingTemplateDeleteResponse.update_forward_refs()
CertificateIssuingTemplateInformation.update_forward_refs()
CertificateIssuingTemplateRequest.update_forward_refs()
CertificateIssuingTemplateResponse.update_forward_refs()
CertificateIssuingTemplateRulesInformation.update_forward_refs()
ClientCredentials.update_forward_refs()
CloudFlareDnsProviderInformation.update_forward_refs()
CronPatternInformation.update_forward_refs()
DigicertCredentials.update_forward_refs()
DigicertCredentialsInformation.update_forward_refs()
DigicertProductDetailsInformation.update_forward_refs()
DigicertProductInformation.update_forward_refs()
DigitalOceanDnsProviderInformation.update_forward_refs()
DnComponentInformation.update_forward_refs()
DnsMethod.update_forward_refs()
DnsProviderInformation.update_forward_refs()
DurationFieldType.update_forward_refs()
ECKeyTypeInformation.update_forward_refs()
EntrustCAAccountConfigurationInformation.update_forward_refs()
EntrustCredentials.update_forward_refs()
EntrustCredentialsInformation.update_forward_refs()
EntrustDomainDetails.update_forward_refs()
EntrustProductDetailsInformation.update_forward_refs()
EntrustProductInformation.update_forward_refs()
EntrustTrackingDataInformation.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExtendedCertificateAuthorityAccountInformation.update_forward_refs()
GenerateCaCSROperationRequest.update_forward_refs()
GlobalSignCredentials.update_forward_refs()
GlobalSignCredentialsInformation.update_forward_refs()
GlobalSignDomainDetails.update_forward_refs()
GlobalSignLogEntry.update_forward_refs()
GlobalSignMSSLCAAccountConfigurationInformation.update_forward_refs()
GlobalSignMSSLCredentials.update_forward_refs()
GlobalSignMSSLCredentialsInformation.update_forward_refs()
GlobalSignMSSLDomainDetails.update_forward_refs()
GlobalSignMSSLProductDetailsInformation.update_forward_refs()
GlobalSignMSSLProductInformation.update_forward_refs()
GlobalSignMSSLTrackingDataInformation.update_forward_refs()
GlobalSignProductDetailsInformation.update_forward_refs()
GlobalSignProductInformation.update_forward_refs()
GoogleCloudDnsProviderInformation.update_forward_refs()
ImportConfigurationDetails.update_forward_refs()
KeyTypeInformation.update_forward_refs()
KeyTypeParameters.update_forward_refs()
MicrosoftCAAccountConfigurationInformation.update_forward_refs()
MicrosoftCAAccountImportConfigurationInformation.update_forward_refs()
MicrosoftCAImportDetailsInformation.update_forward_refs()
MicrosoftCredentials.update_forward_refs()
MicrosoftCredentialsInformation.update_forward_refs()
MicrosoftImportConfigurationDetails.update_forward_refs()
MicrosoftProductDetailsInformation.update_forward_refs()
MicrosoftProductInformation.update_forward_refs()
MicrosoftProductOptionTestIssuanceInformation.update_forward_refs()
MockCAAccountConfigurationInformation.update_forward_refs()
MockCACredentials.update_forward_refs()
MockCACredentialsInformation.update_forward_refs()
MockCADomainDetails.update_forward_refs()
MockCAImportConfiguration.update_forward_refs()
MockCAProductDetailsInformation.update_forward_refs()
MockCAProductInformation.update_forward_refs()
MockCAProductOptionTestIssuanceInformation.update_forward_refs()
MockCATrackingDataInformation.update_forward_refs()
MonthlyPatternInformation.update_forward_refs()
NewCaCertificatesOperationRequest.update_forward_refs()
Period.update_forward_refs()
PeriodType.update_forward_refs()
ProductOptionTestIssuanceInformation.update_forward_refs()
RSAKeyTypeInformation.update_forward_refs()
ReadablePeriod.update_forward_refs()
RecommendedSettingsInformation.update_forward_refs()
RecommendedSettingsKeyTypeInformation.update_forward_refs()
RecommendedSettingsKeyTypeParameter.update_forward_refs()
RecommendedSettingsRequest.update_forward_refs()
SchedulerPatternInformation.update_forward_refs()
StringField.update_forward_refs()
StringList.update_forward_refs()
SubjectAltNamesInformation.update_forward_refs()
TppCAAccountConfigurationInformation.update_forward_refs()
TppCredentials.update_forward_refs()
TppCredentialsInformation.update_forward_refs()
TppProductDetailsInformation.update_forward_refs()
TppProductInformation.update_forward_refs()
TrackingDataInformation.update_forward_refs()
UploadCaCertificateOperationRequest.update_forward_refs()
ValidityInformation.update_forward_refs()
WebServerMethod.update_forward_refs()
WeeklyPatternInformation.update_forward_refs()
ZtpkiCAAccountConfigurationInformation.update_forward_refs()
ZtpkiCredentials.update_forward_refs()
ZtpkiCredentialsInformation.update_forward_refs()
ZtpkiProductDetailsInformation.update_forward_refs()
ZtpkiProductInformation.update_forward_refs()
