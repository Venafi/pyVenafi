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
)
from uuid import UUID

AnyValue = Any

class ApprovalDecisionRequest(ObjectModel):
    reason: str = ApiField(alias='reason')

class ApprovalRequestInformation(ObjectModel):
    approvalRule: CertificateRequestApprovalRuleOpenApi = ApiField(alias='approvalRule')
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    approversOutcome: List[ApproverOutcomeInformation] = ApiField(alias='approversOutcome', default_factory=list)
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    entityId: UUID = ApiField(alias='entityId')
    finalApprover: ApproverPropertyOpenApi = ApiField(alias='finalApprover')
    id: UUID = ApiField(alias='id')
    modificationDate: datetime = ApiField(alias='modificationDate')
    requestorId: UUID = ApiField(alias='requestorId')
    requiredApprovalsCount: int = ApiField(alias='requiredApprovalsCount')
    status: Literal['APPROVED', 'AUTO_APPROVED', 'EXPIRED', 'NOT_REQUIRED',
    'PENDING_APPROVAL', 'PENDING_FINAL_APPROVAL', 'REJECTED'] = ApiField(alias='status')

class ApproverOutcomeInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    reason: str = ApiField(alias='reason')
    status: Literal['APPROVED', 'REJECTED'] = ApiField(alias='status')
    userId: UUID = ApiField(alias='userId')

class ApproverProperty(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: Literal['TEAM', 'USER'] = ApiField(alias='type')

class ApproverPropertyOpenApi(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: str = ApiField(alias='type')

class BuiltInCARole(ObjectModel):
    country: str = ApiField(alias='country')
    defaultValidityDays: int = ApiField(alias='defaultValidityDays')
    keyType: str = ApiField(alias='keyType')
    maxValidityDays: int = ApiField(alias='maxValidityDays')
    name: str = ApiField(alias='name')
    organization: str = ApiField(alias='organization')
    ou: str = ApiField(alias='ou')

class BulkApprovalRequest(ObjectModel):
    ids: List[UUID] = ApiField(alias='ids', default_factory=list)
    reason: str = ApiField(alias='reason')
    wsClientId: str = ApiField(alias='wsClientId')

class BulkApprovalResponse(ObjectModel):
    operationId: str = ApiField(alias='operationId')

class BulkApprovalStatusResponse(ObjectModel):
    requestApprovalStatuses: List[CertificateRequestApprovalStatus] = ApiField(
        alias='requestApprovalStatuses',
        default_factory=list
    )

class CAAccountConfigurationInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class CAAccountImportConfigurationInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class CACertificateInformation(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    keyStrength: int = ApiField(alias='keyStrength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    publicKeyHash: str = ApiField(alias='publicKeyHash')
    signatureAlgorithm: Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(
        alias='signatureAlgorithm'
    )
    signatureHashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='signatureHashAlgorithm')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectC: str = ApiField(alias='subjectC')
    subjectCN: List[str] = ApiField(alias='subjectCN', default_factory=list)
    subjectDN: str = ApiField(alias='subjectDN')
    subjectL: str = ApiField(alias='subjectL')
    subjectO: str = ApiField(alias='subjectO')
    subjectOU: List[str] = ApiField(alias='subjectOU', default_factory=list)
    subjectST: str = ApiField(alias='subjectST')
    validityEnd: datetime = ApiField(alias='validityEnd')
    validityStart: datetime = ApiField(alias='validityStart')

class CaOperationRequest(ObjectModel):
    operation: str = ApiField(alias='operation')

class CancelCaEditOperationRequest(CaOperationRequest):
    ...

class CertificateAuthorityAccountConfigurationRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')

class CertificateAuthorityAccountDeleteResponse(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    id: UUID = ApiField(alias='id')
    key: str = ApiField(alias='key')

class CertificateAuthorityAccountDetailsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class CertificateAuthorityAccountDomainInformation(ObjectModel):
    ...

class CertificateAuthorityAccountDomainRequest(ObjectModel):
    domain: str = ApiField(alias='domain')
    domainAction: Literal['ASSERT_DOMAIN_OVER_DNS', 'DELETE', 'SUBMIT'] = ApiField(alias='domainAction')
    identifier: str = ApiField(alias='identifier')

class CertificateAuthorityAccountImportOptionRequest(ObjectModel):
    importDetails: CertificateAuthorityImportDetailsInformation = ApiField(alias='importDetails')

class CertificateAuthorityAccountImportOptionResponse(ObjectModel):
    certificateAuthorityImportOptions: List[CertificateAuthorityImportOptionInformation] = ApiField(
        alias='certificateAuthorityImportOptions', default_factory=list
    )

class CertificateAuthorityAccountInformation(ObjectModel):
    accountDetails: CertificateAuthorityAccountDetailsInformation = ApiField(alias='accountDetails')
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    companyId: UUID = ApiField(alias='companyId')
    connectionStatus: Literal['FAILED', 'OK'] = ApiField(alias='connectionStatus')
    creationDate: datetime = ApiField(alias='creationDate')
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    dekId: str = ApiField(alias='dekId')
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
    pluginId: UUID = ApiField(alias='pluginId')

class CertificateAuthorityAccountRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    caAccountImportOptions: List[CertificateAuthorityImportDetailsInformation] = ApiField(
        alias='caAccountImportOptions',
        default_factory=list
    )
    caAccountProductOptions: List[CertificateAuthorityProductDetailsInformation] = ApiField(
        alias='caAccountProductOptions', default_factory=list
    )
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    dekId: str = ApiField(alias='dekId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    importConfiguration: CAAccountImportConfigurationInformation = ApiField(alias='importConfiguration')
    importSchedulerEnabled: bool = ApiField(alias='importSchedulerEnabled')
    importSchedulerPattern: SchedulerPatternInformation = ApiField(alias='importSchedulerPattern')
    key: str = ApiField(alias='key')
    pluginId: UUID = ApiField(alias='pluginId')

class CertificateAuthorityAccountResponse(ObjectModel):
    accounts: List[ExtendedCertificateAuthorityAccountInformation] = ApiField(alias='accounts', default_factory=list)

class CertificateAuthorityAccountUpdateRequest(ObjectModel):
    caAccountConfiguration: CAAccountConfigurationInformation = ApiField(alias='caAccountConfiguration')
    caAccountImportOptions: List[CertificateAuthorityImportDetailsInformation] = ApiField(
        alias='caAccountImportOptions',
        default_factory=list
    )
    caAccountProductOptions: List[CertificateAuthorityProductDetailsInformation] = ApiField(
        alias='caAccountProductOptions', default_factory=list
    )
    credentials: CertificateAuthorityCredentialsInformation = ApiField(alias='credentials')
    dekId: str = ApiField(alias='dekId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    importConfiguration: CAAccountImportConfigurationInformation = ApiField(alias='importConfiguration')
    importSchedulerEnabled: bool = ApiField(alias='importSchedulerEnabled')
    importSchedulerPattern: SchedulerPatternInformation = ApiField(alias='importSchedulerPattern')
    key: str = ApiField(alias='key')
    pluginId: UUID = ApiField(alias='pluginId')

class CertificateAuthorityApiInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityApi: Literal[
        'ACME', 'BUILTIN_CA', 'CONNECTOR', 'DIGICERT_TEST', 'ENTRUST', 'GLOBALSIGN_HVCA_V2',
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
    dekId: str = ApiField(alias='dekId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    pluginId: UUID = ApiField(alias='pluginId')

class CertificateAuthorityImportDetailsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class CertificateAuthorityImportOptionInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
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
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')

class CertificateAuthorityProductDetailsInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    certificateType: Literal['DOMAIN_VALIDATED_SSL', 'OTHER'] = ApiField(alias='certificateType')
    hashAlgorithms: List[Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224', 'SHA256',
    'SHA384', 'SHA512', 'UNKNOWN']] = ApiField(alias='hashAlgorithms', default_factory=list)
    productName: str = ApiField(alias='productName')
    productTemplate: CertificateAuthorityProductInformation = ApiField(alias='productTemplate')
    productTypes: List[Literal['CODESIGN', 'SSL']] = ApiField(alias='productTypes', default_factory=list)

class CertificateAuthorityProductInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    certificateType: Literal['DOMAIN_VALIDATED_SSL', 'OTHER'] = ApiField(alias='certificateType')
    hashAlgorithm: Literal['GOSTR3411_94', 'MD2', 'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512', 'UNKNOWN'] = ApiField(alias='hashAlgorithm')
    productName: str = ApiField(alias='productName')
    productTypes: List[Literal['CODESIGN', 'SSL']] = ApiField(alias='productTypes', default_factory=list)
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateAuthorityProductOptionInformation(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
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
    productOptions: List[CertificateAuthorityProductOptionInformation] = ApiField(
        alias='productOptions',
        default_factory=list
    )

class CertificateAuthorityProductOptionsTestIssuanceRequest(ObjectModel):
    productOptions: List[ProductOptionTestIssuanceInformation] = ApiField(alias='productOptions', default_factory=list)

class CertificateAuthorityProductOptionsTestIssuanceResultsResponse(ObjectModel):
    productOptionsResults: List[ProductOptionTestIssuanceInformation] = ApiField(
        alias='productOptionsResults',
        default_factory=list
    )

class CertificateAuthorityResponse(ObjectModel):
    certificateAuthorities: List[CertificateAuthorityInformation] = ApiField(
        alias='certificateAuthorities',
        default_factory=list
    )

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
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityAccountId: UUID = ApiField(alias='certificateAuthorityAccountId')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    description: str = ApiField(alias='description')
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    extendedKeyUsageValues: List[Literal['CLIENT', 'SERVER']] = ApiField(
        alias='extendedKeyUsageValues',
        default_factory=list
    )
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
    trackingData: TrackingDataInformation = ApiField(alias='trackingData')

class CertificateIssuingTemplateRequest(ObjectModel):
    certificateAuthority: Literal['ACME', 'BUILTIN', 'CONNECTOR', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='certificateAuthority')
    certificateAuthorityProductOptionId: UUID = ApiField(alias='certificateAuthorityProductOptionId')
    csrUploadAllowed: bool = ApiField(alias='csrUploadAllowed')
    description: str = ApiField(alias='description')
    everyoneIsConsumer: bool = ApiField(alias='everyoneIsConsumer')
    extendedKeyUsageValues: List[Literal['CLIENT', 'SERVER']] = ApiField(
        alias='extendedKeyUsageValues',
        default_factory=list
    )
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
    sanUniformResourceIdentifierRegexes: List[str] = ApiField(
        alias='sanUniformResourceIdentifierRegexes',
        default_factory=list
    )
    subjectCNRegexes: List[str] = ApiField(alias='subjectCNRegexes', default_factory=list)
    subjectCValues: List[str] = ApiField(alias='subjectCValues', default_factory=list)
    subjectLRegexes: List[str] = ApiField(alias='subjectLRegexes', default_factory=list)
    subjectORegexes: List[str] = ApiField(alias='subjectORegexes', default_factory=list)
    subjectOURegexes: List[str] = ApiField(alias='subjectOURegexes', default_factory=list)
    subjectSTRegexes: List[str] = ApiField(alias='subjectSTRegexes', default_factory=list)
    trackingData: TrackingDataInformation = ApiField(alias='trackingData')

class CertificateIssuingTemplateResponse(ObjectModel):
    certificateIssuingTemplates: List[CertificateIssuingTemplateInformation] = ApiField(
        alias='certificateIssuingTemplates', default_factory=list
    )

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

class CertificateRequestApprovalConditionsFilterRuleInformation(ObjectModel):
    applicationIds: UUID = ApiField(alias='applicationIds')
    certificateAuthorityAccountIds: UUID = ApiField(alias='certificateAuthorityAccountIds')
    certificateIssuingTemplateIds: UUID = ApiField(alias='certificateIssuingTemplateIds')

class CertificateRequestApprovalExceptionsFilterRuleInformation(ObjectModel):
    applicationIds: UUID = ApiField(alias='applicationIds')
    requestors: List[ApproverProperty] = ApiField(alias='requestors', default_factory=list)

class CertificateRequestApprovalRuleDeleteResponseOpenApi(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')

class CertificateRequestApprovalRuleOpenApi(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoApproveOnRenew: bool = ApiField(alias='autoApproveOnRenew')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRequestApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    creationDate: datetime = ApiField(alias='creationDate')
    exceptions: CertificateRequestApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: ApproverPropertyOpenApi = ApiField(alias='finalApprover')
    id: UUID = ApiField(alias='id')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    priority: int = ApiField(alias='priority')
    type: str = ApiField(alias='type')

class CertificateRequestApprovalRulesRequest(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoApproveOnRenew: bool = ApiField(alias='autoApproveOnRenew')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRequestApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    continueProcessingOnException: bool = ApiField(alias='continueProcessingOnException')
    exceptions: CertificateRequestApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: UUID = ApiField(alias='finalApprover')
    name: str = ApiField(alias='name')
    type: Literal['ALL', 'AT_LEAST'] = ApiField(alias='type')

class CertificateRequestApprovalRulesResponseOpenApi(ObjectModel):
    approvalRules: List[CertificateRequestApprovalRuleOpenApi] = ApiField(alias='approvalRules', default_factory=list)

class CertificateRequestApprovalRulesUpdateRequest(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoApproveOnRenew: bool = ApiField(alias='autoApproveOnRenew')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRequestApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    continueProcessingOnException: bool = ApiField(alias='continueProcessingOnException')
    exceptions: CertificateRequestApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: UUID = ApiField(alias='finalApprover')
    name: str = ApiField(alias='name')
    priority: Any = ApiField(alias='priority')
    type: Literal['ALL', 'AT_LEAST'] = ApiField(alias='type')

class CertificateRequestApprovalStatus(ObjectModel):
    certificateRequestId: UUID = ApiField(alias='certificateRequestId')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    status: Literal['COMPLETED', 'FAILED', 'NOT_STARTED'] = ApiField(alias='status')

class CertificateRequestInformation(ObjectModel):
    caOrderId: str = ApiField(alias='caOrderId')
    certificateIds: List[UUID] = ApiField(alias='certificateIds', default_factory=list)
    certificateIssuingTemplateId: UUID = ApiField(alias='certificateIssuingTemplateId')
    certificateName: str = ApiField(alias='certificateName')
    certificateOwnerUserId: UUID = ApiField(alias='certificateOwnerUserId')
    certificateSigningRequest: str = ApiField(alias='certificateSigningRequest')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    customAttributes: CustomAttributes = ApiField(alias='customAttributes')
    dekHash: str = ApiField(alias='dekHash')
    encryptedPrivateKey: List[str] = ApiField(alias='encryptedPrivateKey', default_factory=list)
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    id: UUID = ApiField(alias='id')
    keyCurve: Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN'] = ApiField(alias='keyCurve')
    keyLength: int = ApiField(alias='keyLength')
    keyType: Literal['DSA', 'EC', 'ECGOST3410', 'GOST3410', 'RESERVED3', 'RSA', 'UNKNOWN'] = ApiField(alias='keyType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    product: CertificateAuthorityProductInformation = ApiField(alias='product')
    productEntitlement: Literal['ANY', 'CODESIGN', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION'] = ApiField(
        alias='productEntitlement'
    )
    status: Literal['CANCELLED', 'DELETED', 'FAILED', 'ISSUED', 'NEW', 'PENDING', 'PENDING_APPROVAL',
    'PENDING_FINAL_APPROVAL', 'REJECTED', 'REJECTED_APPROVAL', 'REQUESTED', 'REVOKED'] = ApiField(alias='status')
    subjectAlternativeNamesByType: GeneralNamesData = ApiField(alias='subjectAlternativeNamesByType')
    subjectDN: str = ApiField(alias='subjectDN')
    validityPeriod: str = ApiField(alias='validityPeriod')

class CertificateRevocationApprovalConditionsFilterRuleInformation(ObjectModel):
    certificateAuthorityAccountIds: UUID = ApiField(alias='certificateAuthorityAccountIds')

class CertificateRevocationApprovalExceptionsFilterRuleInformation(ObjectModel):
    applicationIds: UUID = ApiField(alias='applicationIds')
    requestors: List[ApproverProperty] = ApiField(alias='requestors', default_factory=list)

class CertificateRevocationApprovalRuleDeleteResponseOpenApi(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')

class CertificateRevocationApprovalRuleOpenApi(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRevocationApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    creationDate: datetime = ApiField(alias='creationDate')
    exceptions: CertificateRevocationApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: ApproverPropertyOpenApi = ApiField(alias='finalApprover')
    id: UUID = ApiField(alias='id')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    priority: int = ApiField(alias='priority')
    type: str = ApiField(alias='type')

class CertificateRevocationApprovalRulesRequest(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRevocationApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    continueProcessingOnException: bool = ApiField(alias='continueProcessingOnException')
    exceptions: CertificateRevocationApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: UUID = ApiField(alias='finalApprover')
    name: str = ApiField(alias='name')
    type: Literal['ALL', 'AT_LEAST'] = ApiField(alias='type')

class CertificateRevocationApprovalRulesResponseOpenApi(ObjectModel):
    approvalRules: List[CertificateRevocationApprovalRuleOpenApi] = ApiField(
        alias='approvalRules',
        default_factory=list
    )

class CertificateRevocationApprovalRulesUpdateRequest(ObjectModel):
    approvers: List[ApproverProperty] = ApiField(alias='approvers', default_factory=list)
    atLeast: int = ApiField(alias='atLeast')
    autoRejectionThreshold: Any = ApiField(alias='autoRejectionThreshold')
    conditions: CertificateRevocationApprovalConditionsFilterRuleInformation = ApiField(alias='conditions')
    continueProcessingOnException: bool = ApiField(alias='continueProcessingOnException')
    exceptions: CertificateRevocationApprovalExceptionsFilterRuleInformation = ApiField(alias='exceptions')
    finalApprover: UUID = ApiField(alias='finalApprover')
    name: str = ApiField(alias='name')
    priority: Any = ApiField(alias='priority')
    type: Literal['ALL', 'AT_LEAST'] = ApiField(alias='type')

class ClientCredentials(ObjectModel):
    apiKey: str = ApiField(alias='apiKey')
    secret: str = ApiField(alias='secret')

class ConnectorCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    configuration: JsonNode = ApiField(alias='configuration')

class ConnectorCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    importOptions: List[ImportOptionDetails] = ApiField(alias='importOptions', default_factory=list)
    productOptions: List[ProductOptionDetails] = ApiField(alias='productOptions', default_factory=list)

class ConnectorCAAccountImportConfigurationInformation(CAAccountImportConfigurationInformation):
    configuration: JsonNode = ApiField(alias='configuration')

class ConnectorCAImportDetailsInformation(CertificateAuthorityImportDetailsInformation):
    description: str = ApiField(alias='description')
    name: str = ApiField(alias='name')
    settings: JsonNode = ApiField(alias='settings')

class ConnectorCredentials(CertificateAuthorityCredentials):
    credentials: JsonNode = ApiField(alias='credentials')

class ConnectorCredentialsInformation(CertificateAuthorityCredentialsInformation):
    credentials: JsonNode = ApiField(alias='credentials')

class ConnectorProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    details: JsonNode = ApiField(alias='details')

class ConnectorProductInformation(CertificateAuthorityProductInformation):
    data: JsonNode = ApiField(alias='data')

class CustomAttributes(ObjectModel):
    dnsNames: List[str] = ApiField(alias='dnsNames', default_factory=list)
    overwriteSans: bool = ApiField(alias='overwriteSans')

class DigicertCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    organizationIds: List[int] = ApiField(alias='organizationIds', default_factory=list)

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

class DnsProviderInformation(ObjectModel):
    dekId: str = ApiField(alias='dekId')
    dnsProviderType: str = ApiField(alias='dnsProviderType')

class DurationFieldType(ObjectModel):
    name: str = ApiField(alias='name')

class EntrustCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    clientId: int = ApiField(alias='clientId')

class EntrustCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    allClientIds: Dict[str, str] = ApiField(alias='allClientIds', default_factory=dict)
    clientDetails: EntrustClientDetails = ApiField(alias='clientDetails')

class EntrustClientDetails(ObjectModel):
    clientId: int = ApiField(alias='clientId')
    clientName: str = ApiField(alias='clientName')
    evExpiryDate: datetime = ApiField(alias='evExpiryDate')
    evValidationStatus: Literal['APPROVED', 'DEACTIVATED', 'DECLINED', 'EXPIRED',
    'PENDING', 'PENDING_FINAL_APPROVAL'] = ApiField(alias='evValidationStatus')
    friendlyClientName: str = ApiField(alias='friendlyClientName')
    ovExpiryDate: datetime = ApiField(alias='ovExpiryDate')
    qvExpiryDate: datetime = ApiField(alias='qvExpiryDate')
    qvValidationStatus: Literal['APPROVED', 'DEACTIVATED', 'DECLINED', 'EXPIRED',
    'PENDING', 'PENDING_FINAL_APPROVAL'] = ApiField(alias='qvValidationStatus')
    uri: str = ApiField(alias='uri')
    validationStatus: Literal['APPROVED', 'DEACTIVATED', 'DECLINED', 'EXPIRED',
    'PENDING', 'PENDING_FINAL_APPROVAL'] = ApiField(alias='validationStatus')

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

class EntrustProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    ...

class EntrustProductInformation(CertificateAuthorityProductInformation):
    ...

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class EtsiQcPds(ObjectModel):
    policies: Dict[str, str] = ApiField(alias='policies', default_factory=dict)
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')

class ExtendedCertificateAuthorityAccountInformation(ObjectModel):
    account: CertificateAuthorityAccountInformation = ApiField(alias='account')
    importOptions: List[CertificateAuthorityImportOptionInformation] = ApiField(
        alias='importOptions',
        default_factory=list
    )
    productOptions: List[CertificateAuthorityProductOptionInformation] = ApiField(
        alias='productOptions',
        default_factory=list
    )

class ExtendedKeyUsages(ObjectModel):
    critical: bool = ApiField(alias='critical')
    ekus: ListValidationPolicy = ApiField(alias='ekus', default_factory=list)

class ExtentionsValidationPolicy(ObjectModel):
    critical: bool = ApiField(alias='critical')
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')
    valueFormat: str = ApiField(alias='valueFormat')
    valueType: Literal['DER', 'IA5STRING', 'INTEGER', 'NIL', 'PRINTABLESTRING', 'UTF8STRING'] = ApiField(
        alias='valueType'
    )

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

class GenerateCaCSROperationRequest(CaOperationRequest):
    intermediateProps: CertificateInformation = ApiField(alias='intermediateProps')

class GenericDnsProviderInformation(DnsProviderInformation):
    provider: str = ApiField(alias='provider')
    variables: Dict[str, str] = ApiField(alias='variables', default_factory=dict)

class GlobalSignCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    domainsDetails: List[GlobalSignDomainDetails] = ApiField(alias='domainsDetails', default_factory=list)
    trustChain: List[str] = ApiField(alias='trustChain', default_factory=list)
    validationPolicy: GlobalSignValidationPolicy = ApiField(alias='validationPolicy')

class GlobalSignCredentials(CertificateAuthorityCredentials):
    clientCredentials: ClientCredentials = ApiField(alias='clientCredentials')
    credentials: str = ApiField(alias='credentials')

class GlobalSignCredentialsInformation(CertificateAuthorityCredentialsInformation):
    credentials: str = ApiField(alias='credentials')

class GlobalSignDomainDetails(ObjectModel):
    assertBy: datetime = ApiField(alias='assertBy')
    claimId: str = ApiField(alias='claimId')
    createdAt: datetime = ApiField(alias='createdAt')
    domain: str = ApiField(alias='domain')
    expiresAt: datetime = ApiField(alias='expiresAt')
    identifier: str = ApiField(alias='identifier')
    log: List[GlobalSignLogEntry] = ApiField(alias='log', default_factory=list)
    status: Literal['INVALID', 'PENDING', 'REQUESTED', 'VALID'] = ApiField(alias='status')
    validationToken: str = ApiField(alias='validationToken')

class GlobalSignLogEntry(ObjectModel):
    description: str = ApiField(alias='description')
    status: Literal['ERROR', 'SUCCESS'] = ApiField(alias='status')
    timestamp: datetime = ApiField(alias='timestamp')

class GlobalSignMSSLCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    connectTestServer: bool = ApiField(alias='connectTestServer')
    profileId: str = ApiField(alias='profileId')
    useSyncApi: bool = ApiField(alias='useSyncApi')

class GlobalSignMSSLCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    domainsDetails: List[GlobalSignMSSLDomainDetails] = ApiField(alias='domainsDetails', default_factory=list)
    profiles: List[ProfileDetails] = ApiField(alias='profiles', default_factory=list)

class GlobalSignMSSLCredentials(CertificateAuthorityCredentials):
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')

class GlobalSignMSSLCredentialsInformation(CertificateAuthorityCredentialsInformation):
    password: str = ApiField(alias='password')
    username: str = ApiField(alias='username')

class GlobalSignMSSLDomainDetails(ObjectModel):
    domain: str = ApiField(alias='domain')
    domainId: str = ApiField(alias='domainId')
    identifier: str = ApiField(alias='identifier')
    status: Literal['INVALID', 'PENDING', 'REQUESTED', 'VALID'] = ApiField(alias='status')

class GlobalSignMSSLProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    productFriendlyName: str = ApiField(alias='productFriendlyName')

class GlobalSignMSSLProductInformation(CertificateAuthorityProductInformation):
    ...

class GlobalSignProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    ...

class GlobalSignProductInformation(CertificateAuthorityProductInformation):
    ...

class GlobalSignValidationPolicy(ObjectModel):
    customExtensions: Dict[str, ExtentionsValidationPolicy] = ApiField(alias='customExtensions', default_factory=dict)
    extendedKeyUsages: ExtendedKeyUsages = ApiField(alias='extendedKeyUsages')
    msExtensionTemplate: MsExtensionTemplate = ApiField(alias='msExtensionTemplate')
    publicKey: PublicKey = ApiField(alias='publicKey')
    publicKeySignature: Literal['FORBIDDEN', 'REQUIRED'] = ApiField(alias='publicKeySignature')
    qualifiedStatements: QualifiedStatements = ApiField(alias='qualifiedStatements')
    san: San = ApiField(alias='san')
    signature: Signature = ApiField(alias='signature')
    subjectDa: SubjectDa = ApiField(alias='subjectDa')
    subjectDn: SubjectDn = ApiField(alias='subjectDn')
    validity: Validity = ApiField(alias='validity')

class GoogleCloudDnsProviderInformation(DnsProviderInformation):
    clientEmail: str = ApiField(alias='clientEmail')
    privateKey: str = ApiField(alias='privateKey')
    privateKeyId: str = ApiField(alias='privateKeyId')
    projectId: str = ApiField(alias='projectId')
    tokenUri: str = ApiField(alias='tokenUri')

class ImportConfigurationDetails(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class ImportOptionDetails(ObjectModel):
    description: str = ApiField(alias='description')
    name: str = ApiField(alias='name')
    settings: AnyValue = ApiField(alias='settings')

class IntegerValidationPolicy(ObjectModel):
    max: int = ApiField(alias='max')
    min: int = ApiField(alias='min')
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')

class JsonNode(ObjectModel):
    ...

class KeyTypeInformation(ObjectModel):
    keyType: str = ApiField(alias='keyType')

class KeyTypeParameters(ObjectModel):
    keyCurves: List[Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN']] = ApiField(
        alias='keyCurves',
        default_factory=list
    )
    keyLengths: List[int] = ApiField(alias='keyLengths', default_factory=list)
    keyType: Literal['EC', 'RSA'] = ApiField(alias='keyType')

class ListValidationPolicy(ObjectModel):
    isStatic: bool = ApiField(alias='isStatic')
    list: List[str] = ApiField(alias='list', default_factory=list)
    maxcount: int = ApiField(alias='maxcount')
    mincount: int = ApiField(alias='mincount')

class MetadataDetails(ObjectModel):
    externalAccountRequired: bool = ApiField(alias='externalAccountRequired')
    termsOfService: str = ApiField(alias='termsOfService')

class MicrosoftCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    address: str = ApiField(alias='address')
    serviceName: str = ApiField(alias='serviceName')
    workerId: UUID = ApiField(alias='workerId')

class MicrosoftCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    maxRequestIdSnapshot: int = ApiField(alias='maxRequestIdSnapshot')
    templates: List[MicrosoftTemplateDetails] = ApiField(alias='templates', default_factory=list)

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
    includeExpiredCertificates: bool = ApiField(alias='includeExpiredCertificates')
    includeRevokedCertificates: bool = ApiField(alias='includeRevokedCertificates')

class MicrosoftProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    oid: str = ApiField(alias='oid')
    status: Literal['FAILED', 'IN_PROGRESS', 'OK', 'PENDING'] = ApiField(alias='status')

class MicrosoftProductInformation(CertificateAuthorityProductInformation):
    templateOid: str = ApiField(alias='templateOid')

class MicrosoftTemplateDetails(ObjectModel):
    name: str = ApiField(alias='name')
    oid: str = ApiField(alias='oid')

class MockCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    someId: int = ApiField(alias='someId')
    someName: str = ApiField(alias='someName')

class MockCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    accountName: str = ApiField(alias='accountName')
    caAccountConfigurationDescription: str = ApiField(alias='caAccountConfigurationDescription')
    creationDate: datetime = ApiField(alias='creationDate')
    domainsDetails: List[MockCADomainDetails] = ApiField(alias='domainsDetails', default_factory=list)

class MockCACredentials(CertificateAuthorityCredentials):
    apiKey: str = ApiField(alias='apiKey')

class MockCACredentialsInformation(CertificateAuthorityCredentialsInformation):
    apiKey: str = ApiField(alias='apiKey')

class MockCADomainDetails(ObjectModel):
    domain: str = ApiField(alias='domain')
    identifier: str = ApiField(alias='identifier')
    status: Literal['INVALID', 'PENDING', 'REQUESTED', 'VALID'] = ApiField(alias='status')

class MockCAImportConfiguration(ImportConfigurationDetails):
    includeExpiredCertificates: bool = ApiField(alias='includeExpiredCertificates')
    includeRevokedCertificates: bool = ApiField(alias='includeRevokedCertificates')

class MockCAProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    signatureAlgorithms: List[Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1']] = ApiField(
        alias='signatureAlgorithms',
        default_factory=list
    )

class MockCAProductInformation(CertificateAuthorityProductInformation):
    signatureAlgorithm: Literal[
        'EC_DSA_WITH_SHA1', 'EC_DSA_WITH_SHA224', 'EC_DSA_WITH_SHA256', 'EC_DSA_WITH_SHA384', 'EC_DSA_WITH_SHA512', 'GOST_R3411_94_WITH_GOST_R3410_2001', 'GOST_R3411_94_WITH_GOST_R3410_94', 'ID_DSA_WITH_SHA1', 'MD2_WITH_RSA_ENCRYPTION',
        'MD5_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION', 'SHA1_WITH_RSA_ENCRYPTION2', 'SHA1_WITH_RSAandMGF1', 'SHA256_WITH_RSA_ENCRYPTION', 'SHA384_WITH_RSA_ENCRYPTION', 'SHA512_WITH_RSA_ENCRYPTION', 'UNKNOWN', 'dsaWithSHA1'] = ApiField(
        alias='signatureAlgorithm'
    )

class MsExtensionTemplate(ObjectModel):
    critical: bool = ApiField(alias='critical')
    majorVersion: IntegerValidationPolicy = ApiField(alias='majorVersion')
    minorVersion: IntegerValidationPolicy = ApiField(alias='minorVersion')
    templateId: StringValidationPolicy = ApiField(alias='templateId')

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

class ProductOptionDetails(ObjectModel):
    name: str = ApiField(alias='name')
    productDetails: AnyValue = ApiField(alias='productDetails')
    types: List[Literal['CODESIGN', 'SSL']] = ApiField(alias='types', default_factory=list)

class ProductOptionTestIssuanceInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    status: Literal['FAILED', 'IN_PROGRESS', 'OK', 'PENDING'] = ApiField(alias='status')

class ProfileDetails(ObjectModel):
    email: str = ApiField(alias='email')
    firstName: str = ApiField(alias='firstName')
    lastName: str = ApiField(alias='lastName')
    phone: str = ApiField(alias='phone')
    profileId: str = ApiField(alias='profileId')

class PublicKey(ObjectModel):
    allowedLengths: List[int] = ApiField(alias='allowedLengths', default_factory=list)
    keyFormat: Literal['PKCS10', 'PKCS8'] = ApiField(alias='keyFormat')
    keyType: Literal['ECDSA', 'RSA'] = ApiField(alias='keyType')

class QualifiedStatements(ObjectModel):
    etsiQcCompliance: Literal['OPTIONAL', 'STATIC_FALSE', 'STATIC_TRUE'] = ApiField(alias='etsiQcCompliance')
    etsiQcPds: EtsiQcPds = ApiField(alias='etsiQcPds')
    etsiQcRetentionPeriod: IntegerValidationPolicy = ApiField(alias='etsiQcRetentionPeriod')
    etsiQcSscdCompliance: Literal['OPTIONAL', 'STATIC_FALSE', 'STATIC_TRUE'] = ApiField(alias='etsiQcSscdCompliance')
    etsiQcType: StringValidationPolicy = ApiField(alias='etsiQcType')
    semantics: Semantics = ApiField(alias='semantics')

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

class San(ObjectModel):
    dnsNames: ListValidationPolicy = ApiField(alias='dnsNames', default_factory=list)
    emails: ListValidationPolicy = ApiField(alias='emails', default_factory=list)
    ipAddresses: ListValidationPolicy = ApiField(alias='ipAddresses', default_factory=list)
    otherNames: Dict[str, ValueFieldValidationPolicy] = ApiField(alias='otherNames', default_factory=dict)
    uris: ListValidationPolicy = ApiField(alias='uris', default_factory=list)

class SchedulerPatternInformation(ObjectModel):
    recurrenceType: str = ApiField(alias='recurrenceType')

class Semantics(ObjectModel):
    identifier: StringValidationPolicy = ApiField(alias='identifier')
    nameAuthorities: ListValidationPolicy = ApiField(alias='nameAuthorities', default_factory=list)

class Signature(ObjectModel):
    algorithm: SignatureAlgorithmPolicy = ApiField(alias='algorithm')
    hashAlgorithm: SignatureHashAlgorithmPolicy = ApiField(alias='hashAlgorithm')

class SignatureAlgorithmPolicy(ObjectModel):
    list: List[Literal['ECDSA', 'RSA', 'RSA-PSS']] = ApiField(alias='list', default_factory=list)
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')

class SignatureHashAlgorithmPolicy(ObjectModel):
    list: List[Literal['SHA-256', 'SHA-384', 'SHA-512']] = ApiField(alias='list', default_factory=list)
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')

class StringField(ObjectModel):
    format: str = ApiField(alias='format')
    presence: str = ApiField(alias='presence')

class StringList(ObjectModel):
    format: List[str] = ApiField(alias='format', default_factory=list)
    presence: str = ApiField(alias='presence')

class StringValidationPolicy(ObjectModel):
    format: str = ApiField(alias='format')
    presence: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='presence')

class SubjectAltNamesInformation(ObjectModel):
    label: str = ApiField(alias='label')
    modifiable: bool = ApiField(alias='modifiable')
    required: bool = ApiField(alias='required')
    tag: str = ApiField(alias='tag')

class SubjectDa(ObjectModel):
    countryOfCitizenship: ListValidationPolicy = ApiField(alias='countryOfCitizenship', default_factory=list)
    countryOfResidence: ListValidationPolicy = ApiField(alias='countryOfResidence', default_factory=list)
    dateOfBirth: Literal['FORBIDDEN', 'OPTIONAL', 'REQUIRED', 'STATIC'] = ApiField(alias='dateOfBirth')
    extraAttributes: Dict[str, ValueFieldValidationPolicy] = ApiField(alias='extraAttributes', default_factory=dict)
    gender: StringValidationPolicy = ApiField(alias='gender')
    placeOfBirth: StringValidationPolicy = ApiField(alias='placeOfBirth')

class SubjectDn(ObjectModel):
    businessCategory: StringValidationPolicy = ApiField(alias='businessCategory')
    commonName: StringValidationPolicy = ApiField(alias='commonName')
    country: StringValidationPolicy = ApiField(alias='country')
    email: StringValidationPolicy = ApiField(alias='email')
    extraAttributes: Dict[str, ValueFieldValidationPolicy] = ApiField(alias='extraAttributes', default_factory=dict)
    joiCountryName: StringValidationPolicy = ApiField(alias='joiCountryName')
    joiLocalityName: StringValidationPolicy = ApiField(alias='joiLocalityName')
    joiStateOrProvinceName: StringValidationPolicy = ApiField(alias='joiStateOrProvinceName')
    locality: StringValidationPolicy = ApiField(alias='locality')
    organization: StringValidationPolicy = ApiField(alias='organization')
    organizationalUnit: ListValidationPolicy = ApiField(alias='organizationalUnit', default_factory=list)
    state: StringValidationPolicy = ApiField(alias='state')
    streetAddress: StringValidationPolicy = ApiField(alias='streetAddress')

class TppCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    clientId: str = ApiField(alias='clientId')
    hostnameOrAddress: str = ApiField(alias='hostnameOrAddress')
    pluginId: UUID = ApiField(alias='pluginId')

class TppCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    ...

class TppCredentials(CertificateAuthorityCredentials):
    accessToken: str = ApiField(alias='accessToken')
    dekId: str = ApiField(alias='dekId')
    expires: datetime = ApiField(alias='expires')
    refreshToken: str = ApiField(alias='refreshToken')
    refreshUntil: datetime = ApiField(alias='refreshUntil')
    username: str = ApiField(alias='username')

class TppCredentialsInformation(CertificateAuthorityCredentialsInformation):
    dekId: str = ApiField(alias='dekId')
    expires: datetime = ApiField(alias='expires')
    password: str = ApiField(alias='password')
    refreshToken: str = ApiField(alias='refreshToken')
    refreshUntil: datetime = ApiField(alias='refreshUntil')
    username: str = ApiField(alias='username')

class TppProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    ...

class TppProductInformation(CertificateAuthorityProductInformation):
    ...

class TrackingDataInformation(ObjectModel):
    certificateAuthority: str = ApiField(alias='certificateAuthority')

class UploadCaCertificateOperationRequest(CaOperationRequest):
    pemCertificates: str = ApiField(alias='pemCertificates')

class Validity(ObjectModel):
    notBeforeNegativeSkew: int = ApiField(alias='notBeforeNegativeSkew')
    notBeforePositiveSkew: int = ApiField(alias='notBeforePositiveSkew')
    secondsmax: int = ApiField(alias='secondsmax')
    secondsmin: int = ApiField(alias='secondsmin')

class ValidityInformation(ObjectModel):
    defaultValue: Period = ApiField(alias='defaultValue')
    maxValue: Period = ApiField(alias='maxValue')

class ValueFieldValidationPolicy(ObjectModel):
    isStatic: bool = ApiField(alias='isStatic')
    maxcount: int = ApiField(alias='maxcount')
    mincount: int = ApiField(alias='mincount')
    valueFormat: str = ApiField(alias='valueFormat')
    valueType: Literal['DER', 'IA5STRING', 'INTEGER', 'NIL', 'PRINTABLESTRING', 'UTF8STRING'] = ApiField(
        alias='valueType'
    )

class WeeklyPatternInformation(SchedulerPatternInformation):
    daysOfWeek: List[Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY',
    'TUESDAY', 'WEDNESDAY']] = ApiField(alias='daysOfWeek', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')

class ZtpkiCAAccountConfigurationInformation(CAAccountConfigurationInformation):
    serverUrl: str = ApiField(alias='serverUrl')

class ZtpkiCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    ...

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

class AcmeCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    kid: str = ApiField(alias='kid')
    metadataDetails: MetadataDetails = ApiField(alias='metadataDetails')
    newAccount: str = ApiField(alias='newAccount')
    newNonce: str = ApiField(alias='newNonce')
    newOrder: str = ApiField(alias='newOrder')

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
    ...

class AcmeProductInformation(CertificateAuthorityProductInformation):
    ...

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

class BuiltInCAAccountDetailsInformation(CertificateAuthorityAccountDetailsInformation):
    companyId: UUID = ApiField(alias='companyId')
    issuingCAPath: str = ApiField(alias='issuingCAPath')
    issuingRole: BuiltInCARole = ApiField(alias='issuingRole')
    pendingIssuingCAPath: str = ApiField(alias='pendingIssuingCAPath')
    pendingIssuingCaCsr: str = ApiField(alias='pendingIssuingCaCsr')
    rootCAPath: str = ApiField(alias='rootCAPath')
    trustChain: List[CACertificateInformation] = ApiField(alias='trustChain', default_factory=list)

class BuiltInCAProductDetailsInformation(CertificateAuthorityProductDetailsInformation):
    ...

class BuiltInCAProductInformation(CertificateAuthorityProductInformation):
    ...

class CloudFlareDnsProviderInformation(DnsProviderInformation):
    apiKey: str = ApiField(alias='apiKey')
    dnsApiToken: str = ApiField(alias='dnsApiToken')
    email: str = ApiField(alias='email')
    zoneApiToken: str = ApiField(alias='zoneApiToken')

class ConnectorImportConfigurationDetails(ImportConfigurationDetails):
    configuration: JsonNode = ApiField(alias='configuration')

class CronPatternInformation(SchedulerPatternInformation):
    cronExpression: str = ApiField(alias='cronExpression')

class DigitalOceanDnsProviderInformation(DnsProviderInformation):
    authenticationToken: str = ApiField(alias='authenticationToken')

class ECKeyTypeInformation(KeyTypeInformation):
    keyCurves: List[Literal['ED25519', 'P256', 'P384', 'P521', 'UNKNOWN']] = ApiField(
        alias='keyCurves',
        default_factory=list
    )

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
    ...

class MockCATrackingDataInformation(TrackingDataInformation):
    requesterName: str = ApiField(alias='requesterName')

class MonthlyPatternInformation(SchedulerPatternInformation):
    daysOfMonth: List[Literal[
        'D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25',
        'D26', 'D27', 'D28', 'D29', 'D3', 'D30', 'D31', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'L', 'LW']] = ApiField(
        alias='daysOfMonth',
        default_factory=list
    )
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')

AcmeCAAccountConfigurationInformation.update_forward_refs()
AcmeCAAccountDetailsInformation.update_forward_refs()
AcmeCredentials.update_forward_refs()
AcmeCredentialsInformation.update_forward_refs()
AcmeProductDetailsInformation.update_forward_refs()
AcmeProductInformation.update_forward_refs()
AkamaiDnsProviderInformation.update_forward_refs()
ApprovalDecisionRequest.update_forward_refs()
ApprovalRequestInformation.update_forward_refs()
ApproverOutcomeInformation.update_forward_refs()
ApproverProperty.update_forward_refs()
ApproverPropertyOpenApi.update_forward_refs()
AwsRoute53DnsProviderInformation.update_forward_refs()
AzureDnsProviderInformation.update_forward_refs()
BuiltInCAAccountDetailsInformation.update_forward_refs()
BuiltInCAProductDetailsInformation.update_forward_refs()
BuiltInCAProductInformation.update_forward_refs()
BuiltInCARole.update_forward_refs()
BulkApprovalRequest.update_forward_refs()
BulkApprovalResponse.update_forward_refs()
BulkApprovalStatusResponse.update_forward_refs()
CAAccountConfigurationInformation.update_forward_refs()
CAAccountImportConfigurationInformation.update_forward_refs()
CACertificateInformation.update_forward_refs()
CaOperationRequest.update_forward_refs()
CancelCaEditOperationRequest.update_forward_refs()
CertificateAuthorityAccountConfigurationRequest.update_forward_refs()
CertificateAuthorityAccountDeleteResponse.update_forward_refs()
CertificateAuthorityAccountDetailsInformation.update_forward_refs()
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
CertificateRequestApprovalConditionsFilterRuleInformation.update_forward_refs()
CertificateRequestApprovalExceptionsFilterRuleInformation.update_forward_refs()
CertificateRequestApprovalRuleDeleteResponseOpenApi.update_forward_refs()
CertificateRequestApprovalRuleOpenApi.update_forward_refs()
CertificateRequestApprovalRulesRequest.update_forward_refs()
CertificateRequestApprovalRulesResponseOpenApi.update_forward_refs()
CertificateRequestApprovalRulesUpdateRequest.update_forward_refs()
CertificateRequestApprovalStatus.update_forward_refs()
CertificateRequestInformation.update_forward_refs()
CertificateRevocationApprovalConditionsFilterRuleInformation.update_forward_refs()
CertificateRevocationApprovalExceptionsFilterRuleInformation.update_forward_refs()
CertificateRevocationApprovalRuleDeleteResponseOpenApi.update_forward_refs()
CertificateRevocationApprovalRuleOpenApi.update_forward_refs()
CertificateRevocationApprovalRulesRequest.update_forward_refs()
CertificateRevocationApprovalRulesResponseOpenApi.update_forward_refs()
CertificateRevocationApprovalRulesUpdateRequest.update_forward_refs()
ClientCredentials.update_forward_refs()
CloudFlareDnsProviderInformation.update_forward_refs()
ConnectorCAAccountConfigurationInformation.update_forward_refs()
ConnectorCAAccountDetailsInformation.update_forward_refs()
ConnectorCAAccountImportConfigurationInformation.update_forward_refs()
ConnectorCAImportDetailsInformation.update_forward_refs()
ConnectorCredentials.update_forward_refs()
ConnectorCredentialsInformation.update_forward_refs()
ConnectorImportConfigurationDetails.update_forward_refs()
ConnectorProductDetailsInformation.update_forward_refs()
ConnectorProductInformation.update_forward_refs()
CronPatternInformation.update_forward_refs()
CustomAttributes.update_forward_refs()
DigicertCAAccountDetailsInformation.update_forward_refs()
DigicertCredentials.update_forward_refs()
DigicertCredentialsInformation.update_forward_refs()
DigicertProductDetailsInformation.update_forward_refs()
DigicertProductInformation.update_forward_refs()
DigitalOceanDnsProviderInformation.update_forward_refs()
DnComponentInformation.update_forward_refs()
DnsProviderInformation.update_forward_refs()
DurationFieldType.update_forward_refs()
ECKeyTypeInformation.update_forward_refs()
EntrustCAAccountConfigurationInformation.update_forward_refs()
EntrustCAAccountDetailsInformation.update_forward_refs()
EntrustClientDetails.update_forward_refs()
EntrustCredentials.update_forward_refs()
EntrustCredentialsInformation.update_forward_refs()
EntrustProductDetailsInformation.update_forward_refs()
EntrustProductInformation.update_forward_refs()
EntrustTrackingDataInformation.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
EtsiQcPds.update_forward_refs()
ExtendedCertificateAuthorityAccountInformation.update_forward_refs()
ExtendedKeyUsages.update_forward_refs()
ExtentionsValidationPolicy.update_forward_refs()
GeneralNamesData.update_forward_refs()
GenerateCaCSROperationRequest.update_forward_refs()
GenericDnsProviderInformation.update_forward_refs()
GlobalSignCAAccountDetailsInformation.update_forward_refs()
GlobalSignCredentials.update_forward_refs()
GlobalSignCredentialsInformation.update_forward_refs()
GlobalSignDomainDetails.update_forward_refs()
GlobalSignLogEntry.update_forward_refs()
GlobalSignMSSLCAAccountConfigurationInformation.update_forward_refs()
GlobalSignMSSLCAAccountDetailsInformation.update_forward_refs()
GlobalSignMSSLCredentials.update_forward_refs()
GlobalSignMSSLCredentialsInformation.update_forward_refs()
GlobalSignMSSLDomainDetails.update_forward_refs()
GlobalSignMSSLProductDetailsInformation.update_forward_refs()
GlobalSignMSSLProductInformation.update_forward_refs()
GlobalSignMSSLTrackingDataInformation.update_forward_refs()
GlobalSignProductDetailsInformation.update_forward_refs()
GlobalSignProductInformation.update_forward_refs()
GlobalSignValidationPolicy.update_forward_refs()
GoogleCloudDnsProviderInformation.update_forward_refs()
ImportConfigurationDetails.update_forward_refs()
ImportOptionDetails.update_forward_refs()
IntegerValidationPolicy.update_forward_refs()
JsonNode.update_forward_refs()
KeyTypeInformation.update_forward_refs()
KeyTypeParameters.update_forward_refs()
ListValidationPolicy.update_forward_refs()
MetadataDetails.update_forward_refs()
MicrosoftCAAccountConfigurationInformation.update_forward_refs()
MicrosoftCAAccountDetailsInformation.update_forward_refs()
MicrosoftCAAccountImportConfigurationInformation.update_forward_refs()
MicrosoftCAImportDetailsInformation.update_forward_refs()
MicrosoftCredentials.update_forward_refs()
MicrosoftCredentialsInformation.update_forward_refs()
MicrosoftImportConfigurationDetails.update_forward_refs()
MicrosoftProductDetailsInformation.update_forward_refs()
MicrosoftProductInformation.update_forward_refs()
MicrosoftProductOptionTestIssuanceInformation.update_forward_refs()
MicrosoftTemplateDetails.update_forward_refs()
MockCAAccountConfigurationInformation.update_forward_refs()
MockCAAccountDetailsInformation.update_forward_refs()
MockCACredentials.update_forward_refs()
MockCACredentialsInformation.update_forward_refs()
MockCADomainDetails.update_forward_refs()
MockCAImportConfiguration.update_forward_refs()
MockCAProductDetailsInformation.update_forward_refs()
MockCAProductInformation.update_forward_refs()
MockCAProductOptionTestIssuanceInformation.update_forward_refs()
MockCATrackingDataInformation.update_forward_refs()
MonthlyPatternInformation.update_forward_refs()
MsExtensionTemplate.update_forward_refs()
NewCaCertificatesOperationRequest.update_forward_refs()
Period.update_forward_refs()
PeriodType.update_forward_refs()
ProductOptionDetails.update_forward_refs()
ProductOptionTestIssuanceInformation.update_forward_refs()
ProfileDetails.update_forward_refs()
PublicKey.update_forward_refs()
QualifiedStatements.update_forward_refs()
RSAKeyTypeInformation.update_forward_refs()
ReadablePeriod.update_forward_refs()
RecommendedSettingsInformation.update_forward_refs()
RecommendedSettingsKeyTypeInformation.update_forward_refs()
RecommendedSettingsKeyTypeParameter.update_forward_refs()
RecommendedSettingsRequest.update_forward_refs()
San.update_forward_refs()
SchedulerPatternInformation.update_forward_refs()
Semantics.update_forward_refs()
Signature.update_forward_refs()
SignatureAlgorithmPolicy.update_forward_refs()
SignatureHashAlgorithmPolicy.update_forward_refs()
StringField.update_forward_refs()
StringList.update_forward_refs()
StringValidationPolicy.update_forward_refs()
SubjectAltNamesInformation.update_forward_refs()
SubjectDa.update_forward_refs()
SubjectDn.update_forward_refs()
TppCAAccountConfigurationInformation.update_forward_refs()
TppCAAccountDetailsInformation.update_forward_refs()
TppCredentials.update_forward_refs()
TppCredentialsInformation.update_forward_refs()
TppProductDetailsInformation.update_forward_refs()
TppProductInformation.update_forward_refs()
TrackingDataInformation.update_forward_refs()
UploadCaCertificateOperationRequest.update_forward_refs()
Validity.update_forward_refs()
ValidityInformation.update_forward_refs()
ValueFieldValidationPolicy.update_forward_refs()
WeeklyPatternInformation.update_forward_refs()
ZtpkiCAAccountConfigurationInformation.update_forward_refs()
ZtpkiCAAccountDetailsInformation.update_forward_refs()
ZtpkiCredentials.update_forward_refs()
ZtpkiCredentialsInformation.update_forward_refs()
ZtpkiProductDetailsInformation.update_forward_refs()
ZtpkiProductInformation.update_forward_refs()
