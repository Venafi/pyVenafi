from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List, Literal, TypeVar, Generic

T = TypeVar('T')

EnvironmentType = Literal[
    'Code Signing Apple Environment',
    'Code Signing Certificate Environment',
    'Code Signing CSP Environment',
    'Code Signing DotNet Environment',
    'Code Signing Key Pair Environment',
    'Code Signing GPG Environment'
]

TemplateType = Literal[
    'Code Signing Apple Environment Template',
    'Code Signing Certificate Environment Template',
    'Code Signing CSP Environment Template',
    'Code Signing DotNet Environment Template',
    'Code Signing Key Pair Environment Template',
    'Code Signing GPG Environment Template',
]


class ResultCode(PayloadModel):
    code: int = PayloadField()

    @property
    def codesign_result(self):
        return ResultCodes.CodeSign.get(self.code, 'Unknown')


class Items(PayloadModel, Generic[T]):
    dirty: bool = PayloadField(alias='Dirty')
    items: List[T] = PayloadField(alias='Items')


class InfoValue(PayloadModel, Generic[T]):
    info: int = PayloadField(alias='Info')
    value: Items[T] = PayloadField(alias='Value')


class CustomFieldAttributes(PayloadModel):
    field_name: str = PayloadField(alias='FieldName')
    values: List[str] = PayloadField(alias='Values')


class EnvironmentTemplateDetails(InfoValue[str]):
    template_values: InfoValue[str] = PayloadField(alias='TemplateValues')


class RightsKeyValue(PayloadModel):
    key: str = PayloadField(alias='Key')
    value: int = PayloadField(alias='Value')


class SignApplicationCollection(PayloadModel):
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    hash: str = PayloadField(alias='Hash')
    id: int = PayloadField(alias='Id')
    location: str = PayloadField(alias='Location')
    permitted_argument_pattern: str = PayloadField(alias='PermittedArgumentPattern')
    signatory_issuer: str = PayloadField(alias='SignatoryIssuer')
    signatory_subject: str = PayloadField(alias='SignatorySubject')
    size: int = PayloadField(alias='Size')
    version: str = PayloadField(alias='Version')


class AppleTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    certificate_authority_dn: InfoValue[str] = PayloadField(alias='CertificateAuthorityDN')
    certificate_subject: InfoValue[str] = PayloadField(alias='CertificateSubject')
    city: InfoValue[str] = PayloadField(alias='City')
    country: InfoValue[str] = PayloadField(alias='Country')
    cn_pattern: InfoValue[str] = PayloadField(alias='CNPattern')
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDN')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    organization: InfoValue[str] = PayloadField(alias='Organization')
    organizational_unit: InfoValue[str] = PayloadField(alias='OrganizationalUnit')
    per_user: bool = PayloadField(alias='PerUser')
    read_only: bool = PayloadField(alias='ReadOnly')
    state: InfoValue[str] = PayloadField(alias='State')
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn')
    type: TemplateType = PayloadField(alias='Type')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class AppleEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    apple_template: AppleTemplate = PayloadField(alias='AppleTemplate')
    custom_field_attributes: Items[CustomFieldAttributes] = PayloadField(alias='CustomFieldAttributes')
    dirty: bool = PayloadField(alias='Dirty')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    per_user: bool = PayloadField(alias='PerUser')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: EnvironmentType = PayloadField(alias='Type')


class CertificateTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    certificate_authority_dn: InfoValue[str] = PayloadField(alias='CertificateAuthorityDn')
    certificate_subject: str = PayloadField(alias='CertificateSubject')
    certificate_stage: str = PayloadField(alias='CertificateStage')
    certificate_status_text: str = PayloadField(alias='CertificateStatusText')
    city: InfoValue[str] = PayloadField(alias='City')
    country: InfoValue[str] = PayloadField(alias='Country')
    custom_field_attributes: Items[CustomFieldAttributes] = PayloadField(alias='CustomFieldAttributes')
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    organization: InfoValue[str] = PayloadField(alias='Organization')
    organization_unit: InfoValue[str] = PayloadField(alias='OrganizationUnit')
    per_user: bool = PayloadField(alias='PerUser')
    read_only: bool = PayloadField(alias='ReadOnly')
    san_email: InfoValue[str] = PayloadField(alias='SanEmail')
    state: InfoValue[str] = PayloadField(alias='State')
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn')
    type: TemplateType = PayloadField(alias='Type')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class CertificateEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    ca_specific_attributes: Items[str] = PayloadField(alias='CaSpecificAttributes')
    certificate_authority_dn: InfoValue[str] = PayloadField(alias='CertificateAuthorityDn')
    certificate_subject: str = PayloadField(alias='CertificateSubject')
    certificate_template: CertificateTemplate = PayloadField(alias='CertificateTemplate')
    city: InfoValue[str] = PayloadField(alias='City')
    country: InfoValue[str] = PayloadField(alias='Country')
    custom_field_attributes: CustomFieldAttributes = PayloadField(alias='CustomFieldAttributes')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    organization: InfoValue[str] = PayloadField(alias='Organization')
    organization_unit: InfoValue[str] = PayloadField(alias='OrganizationUnit')
    per_user: bool = PayloadField(alias='PerUser')
    san_email: InfoValue[str] = PayloadField(alias='SanEmail')
    state: InfoValue[str] = PayloadField(alias='State')
    status: int = PayloadField(alias='Status')
    target_store: str = PayloadField(alias='TargetStore')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: EnvironmentType = PayloadField(alias='Type')


class CSPTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    description: str = PayloadField(alias='Description')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    encryption_key_algorithm: InfoValue[str] = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: InfoValue[str] = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_container_dn: str = PayloadField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    max_uses: InfoValue[str] = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    signing_key_algorithm: InfoValue[str] = PayloadField(alias='SigningKeyAlgorithm')
    type: TemplateType = PayloadField(alias='Type')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class CSPEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    csp_template: CSPTemplate = PayloadField(alias='CspTemplate')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    encryption_key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='EncryptionKeyAlgorithm')
    encryption_key_dn: str = PayloadField(alias='EncryptionKeyDn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_storage_location: EnvironmentTemplateDetails = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    signing_key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='SigningKeyAlgorithm')
    signing_key_dn: str = PayloadField(alias='SigningKeyDn')
    template_dn: str = PayloadField(alias='TemplateDn')


class DotNetTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    description: str = PayloadField(alias='Description')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    expiration: InfoValue[str] = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_container_dn: InfoValue[str] = PayloadField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: InfoValue[str] = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    type: TemplateType = PayloadField(alias='Type')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class DotNetEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    dot_net_template: DotNetTemplate = PayloadField(alias='DotNetTemplate')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='KeyAlgorithm')
    key_dn: str = PayloadField(alias='KeyDn')
    key_storage_location: EnvironmentTemplateDetails = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: TemplateType = PayloadField(alias='Type')


class GPGTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    authentication_key_algorithm: InfoValue[str] = PayloadField(alias='AuthenticationKeyAlgorithm')
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    email: InfoValue[str] = PayloadField(alias='Email')
    encryption_key_algorithm: InfoValue[str] = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: InfoValue[str] = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_container_dn: str = PayloadField(alias='KeyContainerDN')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: InfoValue[str] = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    read_only: bool = PayloadField(alias='ReadOnly')
    real_name: InfoValue[str] = PayloadField(alias='RealName')
    signing_key_algorithm: InfoValue[str] = PayloadField(alias='SigningKeyAlgorithm')
    type: TemplateType = PayloadField(alias='Type')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class GPGEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    authentication_key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='AuthenticationKeyAlgorithm')
    custom_field_attributes: Items[CustomFieldAttributes] = PayloadField(alias='CustomFieldsAttributes')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    email: List[str] = PayloadField(alias='Email')
    encryption_key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    gpg_template: GPGTemplate = PayloadField(alias='GpgTemplate')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_storage_location: EnvironmentTemplateDetails = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    real_name: EnvironmentTemplateDetails = PayloadField(alias='RealName')
    read_only: bool = PayloadField(alias='ReadOnly')
    signing_key_algorithm: EnvironmentTemplateDetails = PayloadField(alias='SigningKeyAlgorithm')
    status: int = PayloadField(alias='Status')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: EnvironmentType = PayloadField(alias='Type')


class KeyPairTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    description: str = PayloadField(alias='Description')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    expiration: InfoValue[str] = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_container_dn: str = PayloadField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = PayloadField(alias='KeyStorageLocation')
    max_uses: int = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    type: TemplateType = PayloadField(alias='Type')
    validity_period: int = PayloadField(alias='ValidityPeriod')
    visible_to: Items[str] = PayloadField(alias='VisibleTo')


class KeyPairEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    custom_field_attributes: Items[CustomFieldAttributes] = PayloadField(alias='CustomFieldsAttributes')
    dn: str = PayloadField(alias='Dn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: Items[str] = PayloadField(alias='IpAddressRestriction')
    key_algorithm: InfoValue[str] = PayloadField(alias='KeyAlgorithm')
    key_dn: str = PayloadField(alias='KeyDn')
    key_pair_template: KeyPairTemplate = PayloadField(alias='KeyPairTemplate')
    key_storage_location: EnvironmentTemplateDetails = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    status: int = PayloadField(alias='Status')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: EnvironmentType = PayloadField(alias='Type')


class Application(PayloadModel):
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    hash: str = PayloadField(alias='Hash')
    id: int = PayloadField(alias='Id')
    location: str = PayloadField(alias='Location')
    permitted_argument_pattern: str = PayloadField(alias='PermittedArgumentPattern')
    signatory_issuer: str = PayloadField(alias='SignatoryIssuer')
    signatory_subject: str = PayloadField(alias='SignatorySubject')
    size: int = PayloadField(alias='Size')
    version: str = PayloadField(alias='Version')


class ApplicationCollection(PayloadModel):
    application_dns: Items[str] = PayloadField(alias='ApplicationDns')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')


class GlobalConfiguration(PayloadModel):
    approved_key_storage_locations: Items[str] = PayloadField(alias='ApprovedKeyStorageLocations')
    available_key_storage_locations: Items[str] = PayloadField(alias='AvailableKeyStorageLocations')
    default_ca_container: str = PayloadField(alias='DefaultCaContainer')
    default_certificate_container: str = PayloadField(alias='DefaultCertificateContainer')
    default_credential_container: str = PayloadField(alias='DefaultCredentialContainer')
    key_use_timeout: int = PayloadField(alias='KeyUseTimeout')
    project_description_tooltip: str = PayloadField(alias='ProjectDescriptionTooltip')
    request_in_progress_message: str = PayloadField(alias='RequestInProgressMessage')


class Project(PayloadModel):
    application_dns: Items[str] = PayloadField(alias='ApplicationDns')
    applications: List[Application] = PayloadField(alias='Applications')
    auditors: Items[str] = PayloadField(alias='Auditors')
    certificate_environments: List[CertificateEnvironment] = PayloadField(alias='CertificateEnvironments')
    collections: List[SignApplicationCollection] = PayloadField(alias='Collections')
    created_on: datetime = PayloadField(alias='CreatedOn')
    csp_environments: List[CSPEnvironment] = PayloadField(alias='CSPEnvironments')
    custom_field_attributes: Items[CustomFieldAttributes] = PayloadField(alias='CustomFieldAttributes')
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    dot_net_environments: List[DotNetEnvironment] = PayloadField(alias='DotNetEnvironments')
    gpg_environments: List[GPGEnvironment] = PayloadField(alias='GPGEnvironments')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_use_approvers: Items[str] = PayloadField(alias='KeyUseApprovers')
    key_users: Items[str] = PayloadField(alias='KeyUsers')
    owners: Items[str] = PayloadField(alias='Owners')
    status: int = PayloadField(alias='Status')


class Rights(PayloadModel):
    value: int = PayloadField()

    @property
    def none(self) -> int:
        return self.value == 0

    @property
    def admin(self) -> int:
        return self.value & 1 == 1

    @property
    def use(self) -> int:
        return self.value & 2 == 2

    @property
    def audit(self) -> int:
        return self.value & 4 == 4

    @property
    def owner(self) -> int:
        return self.value & 8 == 8

    @property
    def project_approval(self) -> int:
        return self.value & 16 == 16

    @property
    def application_admin(self) -> int:
        return self.value & 32 == 32

    @property
    def approve_use(self) -> int:
        return self.value & 64 == 64
