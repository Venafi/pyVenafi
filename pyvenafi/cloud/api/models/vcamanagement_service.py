from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from typing import (
    Any,
    List,
    Literal,
    Union,
)
from uuid import UUID

AnyValue = Any

class AwsCloudProviderInformation(ObjectModel):
    accountIds: List[str] = ApiField(alias='accountIds', default_factory=list)
    regions: List[Literal[
        'af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'eu-central-1', 'eu-central-2',
        'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']] = ApiField(
        alias='regions',
        default_factory=list
    )

class AzureCloudProviderInformation(ObjectModel):
    subscriptionIds: List[UUID] = ApiField(alias='subscriptionIds', default_factory=list)

class ClientAuthenticationInformation(ObjectModel):
    type: str = ApiField(alias='type')

class ClientAuthenticationOpenApi(ObjectModel):
    type: str = ApiField(alias='type')

class ClientAuthenticationRequestOpenApi(ObjectModel):
    clientAuthentication: Union[JwtJwksAuthenticationOpenApi, JwtOidcAuthenticationOpenApi] = ApiField(
        alias='clientAuthentication'
    )

class CloudProvidersInformation(ObjectModel):
    aws: AwsCloudProviderInformation = ApiField(alias='aws')
    azure: AzureCloudProviderInformation = ApiField(alias='azure')
    google: GoogleCloudProviderInformation = ApiField(alias='google')

class ConfigurationCreateRequest(ObjectModel):
    clientAuthentication: ClientAuthenticationInformation = ApiField(alias='clientAuthentication')
    cloudProviders: CloudProvidersInformation = ApiField(alias='cloudProviders')
    name: str = ApiField(alias='name')
    policyIds: UUID = ApiField(alias='policyIds')
    serviceAccountIds: List[UUID] = ApiField(alias='serviceAccountIds', default_factory=list)
    subCaProviderId: UUID = ApiField(alias='subCaProviderId')

class ConfigurationDeleteResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')

class ConfigurationInformation(ObjectModel):
    clientAuthentication: ClientAuthenticationInformation = ApiField(alias='clientAuthentication')
    cloudProviders: CloudProvidersInformation = ApiField(alias='cloudProviders')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: str = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    longLivedCertCount: int = ApiField(alias='longLivedCertCount')
    modificationDate: str = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    serviceAccountIds: List[UUID] = ApiField(alias='serviceAccountIds', default_factory=list)
    shortLivedCertCount: int = ApiField(alias='shortLivedCertCount')
    ultraShortLivedCertCount: int = ApiField(alias='ultraShortLivedCertCount')

class ConfigurationResponse(ObjectModel):
    configurations: List[ExtendedConfigurationInformation] = ApiField(alias='configurations', default_factory=list)

class ConfigurationUpdateRequest(ObjectModel):
    clientAuthentication: ClientAuthenticationRequestOpenApi = ApiField(alias='clientAuthentication')
    cloudProviders: CloudProvidersInformation = ApiField(alias='cloudProviders')
    name: str = ApiField(alias='name')
    policyIds: UUID = ApiField(alias='policyIds')
    serviceAccountIds: List[UUID] = ApiField(alias='serviceAccountIds', default_factory=list)
    subCaProviderId: UUID = ApiField(alias='subCaProviderId')

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class ExtendedConfigurationInformation(ObjectModel):
    clientAuthentication: ClientAuthenticationInformation = ApiField(alias='clientAuthentication')
    cloudProviders: CloudProvidersInformation = ApiField(alias='cloudProviders')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: str = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    longLivedCertCount: int = ApiField(alias='longLivedCertCount')
    modificationDate: str = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    policies: List[PolicyInformation] = ApiField(alias='policies', default_factory=list)
    serviceAccountIds: List[UUID] = ApiField(alias='serviceAccountIds', default_factory=list)
    shortLivedCertCount: int = ApiField(alias='shortLivedCertCount')
    subCaProvider: SubCaProviderInformation = ApiField(alias='subCaProvider')
    ultraShortLivedCertCount: int = ApiField(alias='ultraShortLivedCertCount')

class ExtendedPolicyInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    configurations: List[ConfigurationInformation] = ApiField(alias='configurations', default_factory=list)
    creationDate: str = ApiField(alias='creationDate')
    extendedKeyUsages: Literal[
        'ANY', 'CAPWAP_AC', 'CAPWAP_WTP', 'CLIENT_AUTH', 'CODE_SIGNING', 'DVCS', 'EAP_OVER_LAN', 'EAP_OVER_PPP', 'EMAIL_PROTECTION', 'IPSEC_ENDSYSTEM', 'IPSEC_IKE', 'IPSEC_IKE_INTERMEDIATE',
        'IPSEC_TUNNEL', 'IPSEC_USER', 'OCSP_SIGNING', 'SBGP_CERT_AA_SERVER_AUTH', 'SCVP_CLIENT', 'SCVP_RESPONDER', 'SCVP_SERVER', 'SERVER_AUTH', 'SMARTCARD_LOGON', 'TIME_STAMPING'] = ApiField(
        alias='extendedKeyUsages'
    )
    id: UUID = ApiField(alias='id')
    keyAlgorithm: KeyAlgorithmInformation = ApiField(alias='keyAlgorithm')
    keyUsages: Literal['cRLSign', 'dataEncipherment', 'decipherOnly', 'digitalSignature', 'encipherOnly',
    'keyAgreement', 'keyCertSign', 'keyEncipherment', 'nonRepudiation'] = ApiField(alias='keyUsages')
    modificationDate: str = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    sans: SansInformation = ApiField(alias='sans')
    subject: SubjectAttributesInformation = ApiField(alias='subject')
    validityPeriod: str = ApiField(alias='validityPeriod')

class GoogleCloudProviderInformation(ObjectModel):
    projectIdentifiers: List[str] = ApiField(alias='projectIdentifiers', default_factory=list)
    regions: List[Literal[
        'asia-east1', 'asia-east2', 'asia-northeast1', 'asia-northeast2', 'asia-northeast3', 'asia-south1', 'asia-south2', 'asia-southeast1', 'asia-southeast2', 'australia-southeast1', 'australia-southeast2', 'europe-central2', 'europe-north1', 'europe-southwest1', 'europe-west1', 'europe-west12', 'europe-west2', 'europe-west3',
        'europe-west4', 'europe-west6', 'europe-west8', 'europe-west9', 'me-central1', 'me-west1', 'northamerica-northeast1', 'northamerica-northeast2', 'southamerica-east1', 'southamerica-west1', 'us-central1', 'us-east1', 'us-east4', 'us-east5', 'us-south1', 'us-west1', 'us-west2', 'us-west3', 'us-west4']] = ApiField(
        alias='regions',
        default_factory=list
    )

class IntermediateCertificateInformation(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    commonName: str = ApiField(alias='commonName')
    companyId: UUID = ApiField(alias='companyId')
    configuration: ConfigurationInformation = ApiField(alias='configuration')
    creationDate: str = ApiField(alias='creationDate')
    errorInformation: ErrorInformation = ApiField(alias='errorInformation')
    fingerprint: str = ApiField(alias='fingerprint')
    id: UUID = ApiField(alias='id')
    issuerCertificates: List[str] = ApiField(alias='issuerCertificates', default_factory=list)
    longLivedCertCount: int = ApiField(alias='longLivedCertCount')
    modificationDate: str = ApiField(alias='modificationDate')
    shortLivedCertCount: int = ApiField(alias='shortLivedCertCount')
    status: str = ApiField(alias='status')
    ultraShortLivedCertCount: int = ApiField(alias='ultraShortLivedCertCount')
    validityEnd: str = ApiField(alias='validityEnd')
    validityStart: str = ApiField(alias='validityStart')
    workflowId: str = ApiField(alias='workflowId')

class IntermediateCertificateResponse(ObjectModel):
    intermediateCertificates: List[IntermediateCertificateInformation] = ApiField(
        alias='intermediateCertificates',
        default_factory=list
    )

class JwtJwksAuthenticationInformation(ClientAuthenticationInformation):
    urls: List[str] = ApiField(alias='urls', default_factory=list)

class JwtJwksAuthenticationOpenApi(ClientAuthenticationOpenApi):
    urls: List[str] = ApiField(alias='urls', default_factory=list)

class JwtOidcAuthenticationInformation(ClientAuthenticationInformation):
    audience: str = ApiField(alias='audience')
    baseUrl: str = ApiField(alias='baseUrl')

class JwtOidcAuthenticationOpenApi(ClientAuthenticationOpenApi):
    audience: str = ApiField(alias='audience')
    baseUrl: str = ApiField(alias='baseUrl')

class KeyAlgorithmInformation(ObjectModel):
    allowedValues: Literal[
        'EC_ED25519', 'EC_P256', 'EC_P384', 'EC_P521', 'RSA_2048', 'RSA_3072', 'RSA_4096'] = ApiField(
        alias='allowedValues'
    )
    defaultValue: Literal['EC_ED25519', 'EC_P256', 'EC_P384', 'EC_P521', 'RSA_2048', 'RSA_3072', 'RSA_4096'] = ApiField(
        alias='defaultValue'
    )

class PolicyCreateRequest(ObjectModel):
    extendedKeyUsages: Literal[
        'ANY', 'CAPWAP_AC', 'CAPWAP_WTP', 'CLIENT_AUTH', 'CODE_SIGNING', 'DVCS', 'EAP_OVER_LAN', 'EAP_OVER_PPP', 'EMAIL_PROTECTION', 'IPSEC_ENDSYSTEM', 'IPSEC_IKE', 'IPSEC_IKE_INTERMEDIATE',
        'IPSEC_TUNNEL', 'IPSEC_USER', 'OCSP_SIGNING', 'SBGP_CERT_AA_SERVER_AUTH', 'SCVP_CLIENT', 'SCVP_RESPONDER', 'SCVP_SERVER', 'SERVER_AUTH', 'SMARTCARD_LOGON', 'TIME_STAMPING'] = ApiField(
        alias='extendedKeyUsages'
    )
    keyAlgorithm: KeyAlgorithmInformation = ApiField(alias='keyAlgorithm')
    keyUsages: Literal['cRLSign', 'dataEncipherment', 'decipherOnly', 'digitalSignature', 'encipherOnly',
    'keyAgreement', 'keyCertSign', 'keyEncipherment', 'nonRepudiation'] = ApiField(alias='keyUsages')
    name: str = ApiField(alias='name')
    sans: SansInformation = ApiField(alias='sans')
    subject: SubjectAttributesInformation = ApiField(alias='subject')
    validityPeriod: str = ApiField(alias='validityPeriod')

class PolicyDeleteResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')

class PolicyInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: str = ApiField(alias='creationDate')
    extendedKeyUsages: Literal[
        'ANY', 'CAPWAP_AC', 'CAPWAP_WTP', 'CLIENT_AUTH', 'CODE_SIGNING', 'DVCS', 'EAP_OVER_LAN', 'EAP_OVER_PPP', 'EMAIL_PROTECTION', 'IPSEC_ENDSYSTEM', 'IPSEC_IKE', 'IPSEC_IKE_INTERMEDIATE',
        'IPSEC_TUNNEL', 'IPSEC_USER', 'OCSP_SIGNING', 'SBGP_CERT_AA_SERVER_AUTH', 'SCVP_CLIENT', 'SCVP_RESPONDER', 'SCVP_SERVER', 'SERVER_AUTH', 'SMARTCARD_LOGON', 'TIME_STAMPING'] = ApiField(
        alias='extendedKeyUsages'
    )
    id: UUID = ApiField(alias='id')
    keyAlgorithm: KeyAlgorithmInformation = ApiField(alias='keyAlgorithm')
    keyUsages: Literal['cRLSign', 'dataEncipherment', 'decipherOnly', 'digitalSignature', 'encipherOnly',
    'keyAgreement', 'keyCertSign', 'keyEncipherment', 'nonRepudiation'] = ApiField(alias='keyUsages')
    modificationDate: str = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    sans: SansInformation = ApiField(alias='sans')
    subject: SubjectAttributesInformation = ApiField(alias='subject')
    validityPeriod: str = ApiField(alias='validityPeriod')

class PolicyResponse(ObjectModel):
    policies: List[ExtendedPolicyInformation] = ApiField(alias='policies', default_factory=list)

class PolicyUpdateRequest(ObjectModel):
    extendedKeyUsages: Literal[
        'ANY', 'CAPWAP_AC', 'CAPWAP_WTP', 'CLIENT_AUTH', 'CODE_SIGNING', 'DVCS', 'EAP_OVER_LAN', 'EAP_OVER_PPP', 'EMAIL_PROTECTION', 'IPSEC_ENDSYSTEM', 'IPSEC_IKE', 'IPSEC_IKE_INTERMEDIATE',
        'IPSEC_TUNNEL', 'IPSEC_USER', 'OCSP_SIGNING', 'SBGP_CERT_AA_SERVER_AUTH', 'SCVP_CLIENT', 'SCVP_RESPONDER', 'SCVP_SERVER', 'SERVER_AUTH', 'SMARTCARD_LOGON', 'TIME_STAMPING'] = ApiField(
        alias='extendedKeyUsages'
    )
    keyAlgorithm: KeyAlgorithmInformation = ApiField(alias='keyAlgorithm')
    keyUsages: Literal['cRLSign', 'dataEncipherment', 'decipherOnly', 'digitalSignature', 'encipherOnly',
    'keyAgreement', 'keyCertSign', 'keyEncipherment', 'nonRepudiation'] = ApiField(alias='keyUsages')
    name: str = ApiField(alias='name')
    sans: SansInformation = ApiField(alias='sans')
    subject: SubjectAttributesInformation = ApiField(alias='subject')
    validityPeriod: str = ApiField(alias='validityPeriod')

class PropertyInformation(ObjectModel):
    allowedValues: List[str] = ApiField(alias='allowedValues', default_factory=list)
    defaultValues: List[str] = ApiField(alias='defaultValues', default_factory=list)
    maxOccurrences: int = ApiField(alias='maxOccurrences')
    minOccurrences: int = ApiField(alias='minOccurrences')
    type: Literal['FORBIDDEN', 'IGNORED', 'LOCKED', 'OPTIONAL', 'REQUIRED'] = ApiField(alias='type')

class SansInformation(ObjectModel):
    dnsNames: PropertyInformation = ApiField(alias='dnsNames')
    ipAddresses: PropertyInformation = ApiField(alias='ipAddresses')
    rfc822Names: PropertyInformation = ApiField(alias='rfc822Names')
    uniformResourceIdentifiers: PropertyInformation = ApiField(alias='uniformResourceIdentifiers')

class SubCaProviderCreateRequest(ObjectModel):
    caAccountId: UUID = ApiField(alias='caAccountId')
    caProductOptionId: UUID = ApiField(alias='caProductOptionId')
    caType: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='caType')
    commonName: str = ApiField(alias='commonName')
    country: str = ApiField(alias='country')
    keyAlgorithm: Literal['EC_ED25519', 'EC_P256', 'EC_P384', 'EC_P521', 'RSA_2048', 'RSA_3072', 'RSA_4096'] = ApiField(
        alias='keyAlgorithm'
    )
    locality: str = ApiField(alias='locality')
    name: str = ApiField(alias='name')
    organization: str = ApiField(alias='organization')
    organizationalUnit: str = ApiField(alias='organizationalUnit')
    pkcs11: SubCaProviderPkcs11ConfigurationInformation = ApiField(alias='pkcs11')
    stateOrProvince: str = ApiField(alias='stateOrProvince')
    validityPeriod: str = ApiField(alias='validityPeriod')

class SubCaProviderDeleteResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')

class SubCaProviderInformation(ObjectModel):
    caAccountId: UUID = ApiField(alias='caAccountId')
    caProductOptionId: UUID = ApiField(alias='caProductOptionId')
    caType: Literal['ACME', 'BUILTIN', 'DIGICERT', 'ENTRUST', 'GLOBALSIGN',
    'GLOBALSIGNMSSL', 'MICROSOFT', 'MOCKCA', 'TPP', 'ZTPKI'] = ApiField(alias='caType')
    commonName: str = ApiField(alias='commonName')
    companyId: UUID = ApiField(alias='companyId')
    country: str = ApiField(alias='country')
    creationDate: str = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    keyAlgorithm: Literal['EC_ED25519', 'EC_P256', 'EC_P384', 'EC_P521', 'RSA_2048', 'RSA_3072', 'RSA_4096'] = ApiField(
        alias='keyAlgorithm'
    )
    locality: str = ApiField(alias='locality')
    modificationDate: str = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    organization: str = ApiField(alias='organization')
    organizationalUnit: str = ApiField(alias='organizationalUnit')
    pkcs11: SubCaProviderPkcs11ConfigurationInformation = ApiField(alias='pkcs11')
    stateOrProvince: str = ApiField(alias='stateOrProvince')
    validityPeriod: str = ApiField(alias='validityPeriod')

class SubCaProviderPkcs11ConfigurationInformation(ObjectModel):
    allowedClientLibraries: List[str] = ApiField(alias='allowedClientLibraries', default_factory=list)
    pin: str = ApiField(alias='pin')
    signingEnabled: bool = ApiField(alias='signingEnabled')
    slot: int = ApiField(alias='slot')

class SubCaProviderResponse(ObjectModel):
    subCaProviders: List[SubCaProviderInformation] = ApiField(alias='subCaProviders', default_factory=list)

class SubCaProviderUpdateRequest(ObjectModel):
    caProductOptionId: UUID = ApiField(alias='caProductOptionId')
    commonName: str = ApiField(alias='commonName')
    country: str = ApiField(alias='country')
    keyAlgorithm: Literal['EC_ED25519', 'EC_P256', 'EC_P384', 'EC_P521', 'RSA_2048', 'RSA_3072', 'RSA_4096'] = ApiField(
        alias='keyAlgorithm'
    )
    locality: str = ApiField(alias='locality')
    name: str = ApiField(alias='name')
    organization: str = ApiField(alias='organization')
    organizationalUnit: str = ApiField(alias='organizationalUnit')
    pkcs11: SubCaProviderPkcs11ConfigurationInformation = ApiField(alias='pkcs11')
    stateOrProvince: str = ApiField(alias='stateOrProvince')
    validityPeriod: str = ApiField(alias='validityPeriod')

class SubjectAttributesInformation(ObjectModel):
    commonName: PropertyInformation = ApiField(alias='commonName')
    country: PropertyInformation = ApiField(alias='country')
    locality: PropertyInformation = ApiField(alias='locality')
    organization: PropertyInformation = ApiField(alias='organization')
    organizationalUnit: PropertyInformation = ApiField(alias='organizationalUnit')
    stateOrProvince: PropertyInformation = ApiField(alias='stateOrProvince')

AwsCloudProviderInformation.update_forward_refs()
AzureCloudProviderInformation.update_forward_refs()
ClientAuthenticationInformation.update_forward_refs()
ClientAuthenticationOpenApi.update_forward_refs()
ClientAuthenticationRequestOpenApi.update_forward_refs()
CloudProvidersInformation.update_forward_refs()
ConfigurationCreateRequest.update_forward_refs()
ConfigurationDeleteResponse.update_forward_refs()
ConfigurationInformation.update_forward_refs()
ConfigurationResponse.update_forward_refs()
ConfigurationUpdateRequest.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExtendedConfigurationInformation.update_forward_refs()
ExtendedPolicyInformation.update_forward_refs()
GoogleCloudProviderInformation.update_forward_refs()
IntermediateCertificateInformation.update_forward_refs()
IntermediateCertificateResponse.update_forward_refs()
JwtJwksAuthenticationInformation.update_forward_refs()
JwtJwksAuthenticationOpenApi.update_forward_refs()
JwtOidcAuthenticationInformation.update_forward_refs()
JwtOidcAuthenticationOpenApi.update_forward_refs()
KeyAlgorithmInformation.update_forward_refs()
PolicyCreateRequest.update_forward_refs()
PolicyDeleteResponse.update_forward_refs()
PolicyInformation.update_forward_refs()
PolicyResponse.update_forward_refs()
PolicyUpdateRequest.update_forward_refs()
PropertyInformation.update_forward_refs()
SansInformation.update_forward_refs()
SubCaProviderCreateRequest.update_forward_refs()
SubCaProviderDeleteResponse.update_forward_refs()
SubCaProviderInformation.update_forward_refs()
SubCaProviderPkcs11ConfigurationInformation.update_forward_refs()
SubCaProviderResponse.update_forward_refs()
SubCaProviderUpdateRequest.update_forward_refs()
SubjectAttributesInformation.update_forward_refs()
