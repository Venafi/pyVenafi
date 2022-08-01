from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class ResultCode(PayloadModel):
    code: int = PayloadField(alias='Code')

    @property
    def codesign_result(self):
        return ResultCodes.CodeSign.get(self.code, 'Unknown')


class Items(PayloadModel):
    items: List[str] = PayloadField(alias='Items')


class InfoValue(PayloadModel):
    info: int = PayloadField(alias='Info')
    value: 'Items' = PayloadField(alias='Value')


class CustomFieldAttributes(PayloadModel):
    field_name: str = PayloadField(alias='FieldName')
    values: List[str] = PayloadField(alias='Values')


class EnvironmentTemplateDetails(InfoValue):
    template_values: 'InfoValue' = PayloadField(alias='TemplateValues')


class RightsKeyValue(PayloadModel):
    key: str = PayloadField(alias='Key')
    value: int = PayloadField(alias='Value')


class AppleTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    cn_pattern: str = PayloadField(alias='CnPattern')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    read_only: bool = PayloadField(alias='ReadOnly')
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn')
    type: str = PayloadField(alias='Type')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class AppleEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    apple_template: 'AppleTemplate' = PayloadField(alias='AppleTemplate')
    custom_field_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldAttributes')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    per_user: bool = PayloadField(alias='PerUser')
    template_dn: str = PayloadField(alias='TemplateDn')


class CertificateTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    certificate_authority_dn: 'InfoValue' = PayloadField(alias='CertificateAuthorityDn')
    certificate_subject: str = PayloadField(alias='CertificateSubject')
    city: 'InfoValue' = PayloadField(alias='City')
    country: 'InfoValue' = PayloadField(alias='Country')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    organization: 'InfoValue' = PayloadField(alias='Organization')
    organization_unit: 'InfoValue' = PayloadField(alias='OrganizationUnit')
    per_user: bool = PayloadField(alias='PerUser')
    read_only: bool = PayloadField(alias='ReadOnly')
    san_email: 'InfoValue' = PayloadField(alias='SanEmail')
    state: 'InfoValue' = PayloadField(alias='State')
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn')
    type: str = PayloadField(alias='Type')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class CertificateEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    ca_specific_attributes: 'Items' = PayloadField(alias='CaSpecificAttributes')
    certificate_authority_dn: 'InfoValue' = PayloadField(alias='CertificateAuthorityDn')
    certificate_subject: str = PayloadField(alias='CertificateSubject')
    certificate_template: 'CertificateTemplate' = PayloadField(alias='CertificateTemplate')
    city: 'InfoValue' = PayloadField(alias='City')
    country: 'InfoValue' = PayloadField(alias='Country')
    custom_field_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldAttributes')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    organization: 'InfoValue' = PayloadField(alias='Organization')
    organization_unit: 'InfoValue' = PayloadField(alias='OrganizationUnit')
    per_user: bool = PayloadField(alias='PerUser')
    san_email: 'InfoValue' = PayloadField(alias='SanEmail')
    state: 'InfoValue' = PayloadField(alias='State')
    status: int = PayloadField(alias='Status')
    target_store: str = PayloadField(alias='TargetStore')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: str = PayloadField(alias='Type')


class CSPTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    encryption_key_algorithm: 'InfoValue' = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: 'InfoValue' = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_container_dn: str = PayloadField(alias='KeyContainerDn')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    signing_key_algorithm: 'InfoValue' = PayloadField(alias='SigningKeyAlgorithm')
    type: str = PayloadField(alias='Type')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class CSPEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    csp_template: 'CSPTemplate' = PayloadField(alias='CspTemplate')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    encryption_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='EncryptionKeyAlgorithm')
    encryption_key_dn: str = PayloadField(alias='EncryptionKeyDn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    signing_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='SigningKeyAlgorithm')
    signing_key_dn: str = PayloadField(alias='SigningKeyDn')
    template_dn: str = PayloadField(alias='TemplateDn')


class DotNetTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    expiration: 'InfoValue' = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm')
    key_container_dn: 'InfoValue' = PayloadField(alias='KeyContainerDn')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    type: str = PayloadField(alias='Type')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class DotNetEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    dot_net_template: 'DotNetTemplate' = PayloadField(alias='DotNetTemplate')
    disabled: bool = PayloadField(alias='Disabled')
    dn: str = PayloadField(alias='Dn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyAlgorithm')
    key_dn: str = PayloadField(alias='KeyDn')
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    template_dn: str = PayloadField(alias='TemplateDn')


class GPGTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    authentication_key_algorithm: 'InfoValue' = PayloadField(alias='AuthenticationKeyAlgorithm')
    dn: str = PayloadField(alias='Dn')
    email: 'InfoValue' = PayloadField(alias='Email')
    encryption_key_algorithm: 'InfoValue' = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: 'InfoValue' = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses')
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern')
    per_user: bool = PayloadField(alias='PerUser')
    read_only: bool = PayloadField(alias='ReadOnly')
    real_name: 'InfoValue' = PayloadField(alias='RealName')
    signing_key_algorithm: 'InfoValue' = PayloadField(alias='SigningKeyAlgorithm')
    type: str = PayloadField(alias='Type')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class GPGEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    authentication_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='AuthenticationKeyAlgorithm')
    custom_fields_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldsAttributes')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    email: List[str] = PayloadField(alias='Email')
    encryption_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='EncryptionKeyAlgorithm')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    gpg_template: 'GPGTemplate' = PayloadField(alias='GpgTemplate')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    max_uses: int = PayloadField(alias='MaxUses')
    per_user: bool = PayloadField(alias='PerUser')
    real_name: 'EnvironmentTemplateDetails' = PayloadField(alias='RealName')
    read_only: bool = PayloadField(alias='ReadOnly')
    signing_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='SigningKeyAlgorithm')
    status: int = PayloadField(alias='Status')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: str = PayloadField(alias='Type')


class KeyPairTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    description: str = PayloadField(alias='Description')
    dirty: bool = PayloadField(alias='Dirty')
    dn: str = PayloadField(alias='Dn')
    expiration: 'InfoValue' = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm')
    key_container_dn: str = PayloadField(alias='KeyContainerDn')
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation')
    max_uses: int = PayloadField(alias='MaxUses')
    type: str = PayloadField(alias='Type')
    validity_period: int = PayloadField(alias='ValidityPeriod')
    visible_to: 'Items' = PayloadField(alias='VisibleTo')


class KeyPairEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport')
    custom_fields_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldsAttributes')
    dn: str = PayloadField(alias='Dn')
    expiration: int = PayloadField(alias='Expiration')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction')
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm')
    key_dn: str = PayloadField(alias='KeyDn')
    key_pair_template: 'KeyPairTemplate' = PayloadField(alias='KeyPairTemplate')
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation')
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn')
    status: int = PayloadField(alias='Status')
    template_dn: str = PayloadField(alias='TemplateDn')
    type: str = PayloadField(alias='Type')


class KeyStorageLocations(PayloadModel):
    items: List[str] = PayloadField(alias='Items')


class Application(PayloadModel):
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')


class ApplicationCollection(PayloadModel):
    application_dns: 'Items' = PayloadField(alias='ApplicationDns')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')


class GlobalConfiguration(PayloadModel):
    approved_key_storage_locations: 'KeyStorageLocations' = PayloadField(alias='ApprovedKeyStorageLocations')
    available_key_storage_locations: 'KeyStorageLocations' = PayloadField(alias='AvailableKeyStorageLocations')
    default_ca_container: str = PayloadField(alias='DefaultCaContainer')
    default_certificate_container: str = PayloadField(alias='DefaultCertificateContainer')
    default_credential_container: str = PayloadField(alias='DefaultCredentialContainer')
    key_use_timeout: int = PayloadField(alias='KeyUseTimeout')
    project_description_tooltip: str = PayloadField(alias='ProjectDescriptionTooltip')
    request_in_progress_message: str = PayloadField(alias='RequestInProgressMessage')


class Project(PayloadModel):
    application_dns: 'Items' = PayloadField(alias='ApplicationDns')
    applications: 'List[Application]' = PayloadField(alias='Applications')
    auditors: 'Items' = PayloadField(alias='Auditors')
    certificate_environments: 'List[CertificateEnvironment]' = PayloadField(alias='CertificateEnvironments')
    collections: 'List[SignApplicationCollection]' = PayloadField(alias='Collections')
    created_on: datetime = PayloadField(alias='CreatedOn')
    description: str = PayloadField(alias='Description')
    dn: str = PayloadField(alias='Dn')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    key_use_approvers: 'Items' = PayloadField(alias='KeyUseApprovers')
    key_users: 'Items' = PayloadField(alias='KeyUsers')
    owners: 'Items' = PayloadField(alias='Owners')
    status: int = PayloadField(alias='Status')


class Rights(PayloadModel):
    none: int = PayloadField(alias='None')
    admin: int = PayloadField(alias='Admin')
    use: int = PayloadField(alias='Use')
    audit: int = PayloadField(alias='Audit')
    owner: int = PayloadField(alias='Owner')
    project_approval: int = PayloadField(alias='ProjectApproval')
    application_admin: int = PayloadField(alias='ApplicationAdmin')
    approve_use: int = PayloadField(alias='ApproveUse')


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
