from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class ResultCode(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)

    @property
    def codesign_result(self):
        return ResultCodes.CodeSign.get(self.code, 'Unknown')


class Items(PayloadModel):
    items: List[str] = PayloadField(alias='Items', default=None)


class InfoValue(PayloadModel):
    info: int = PayloadField(alias='Info', default=None)
    value: 'Items' = PayloadField(alias='Value', default=None)


class CustomFieldAttributes(PayloadModel):
    field_name: str = PayloadField(alias='FieldName', default=None)
    values: List[str] = PayloadField(alias='Values', default=None)


class EnvironmentTemplateDetails(InfoValue):
    template_values: 'InfoValue' = PayloadField(alias='TemplateValues', default=None)


class RightsKeyValue(PayloadModel):
    key: str = PayloadField(alias='Key', default=None)
    value: int = PayloadField(alias='Value', default=None)


class AppleTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    cn_pattern: str = PayloadField(alias='CnPattern', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    read_only: bool = PayloadField(alias='ReadOnly', default=None)
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn', default=None)
    type: str = PayloadField(alias='Type', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class AppleEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    apple_template: 'AppleTemplate' = PayloadField(alias='AppleTemplate', default=None)
    custom_field_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldAttributes', default=None)
    dirty: bool = PayloadField(alias='Dirty', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)


class CertificateTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    certificate_authority_dn: 'InfoValue' = PayloadField(alias='CertificateAuthorityDn', default=None)
    certificate_subject: str = PayloadField(alias='CertificateSubject', default=None)
    city: 'InfoValue' = PayloadField(alias='City', default=None)
    country: 'InfoValue' = PayloadField(alias='Country', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern', default=None)
    organization: 'InfoValue' = PayloadField(alias='Organization', default=None)
    organization_unit: 'InfoValue' = PayloadField(alias='OrganizationUnit', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    read_only: bool = PayloadField(alias='ReadOnly', default=None)
    san_email: 'InfoValue' = PayloadField(alias='SanEmail', default=None)
    state: 'InfoValue' = PayloadField(alias='State', default=None)
    target_policy_dn: str = PayloadField(alias='TargetPolicyDn', default=None)
    type: str = PayloadField(alias='Type', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class CertificateEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    ca_specific_attributes: 'Items' = PayloadField(alias='CaSpecificAttributes', default=None)
    certificate_authority_dn: 'InfoValue' = PayloadField(alias='CertificateAuthorityDn', default=None)
    certificate_subject: str = PayloadField(alias='CertificateSubject', default=None)
    certificate_template: 'CertificateTemplate' = PayloadField(alias='CertificateTemplate', default=None)
    city: 'InfoValue' = PayloadField(alias='City', default=None)
    country: 'InfoValue' = PayloadField(alias='Country', default=None)
    custom_field_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldAttributes', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    organization: 'InfoValue' = PayloadField(alias='Organization', default=None)
    organization_unit: 'InfoValue' = PayloadField(alias='OrganizationUnit', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    san_email: 'InfoValue' = PayloadField(alias='SanEmail', default=None)
    state: 'InfoValue' = PayloadField(alias='State', default=None)
    status: int = PayloadField(alias='Status', default=None)
    target_store: str = PayloadField(alias='TargetStore', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)
    type: str = PayloadField(alias='Type', default=None)


class CSPTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    dirty: bool = PayloadField(alias='Dirty', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    encryption_key_algorithm: 'InfoValue' = PayloadField(alias='EncryptionKeyAlgorithm', default=None)
    expiration: 'InfoValue' = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_container_dn: str = PayloadField(alias='KeyContainerDn', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses', default=None)
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    signing_key_algorithm: 'InfoValue' = PayloadField(alias='SigningKeyAlgorithm', default=None)
    type: str = PayloadField(alias='Type', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class CSPEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    csp_template: 'CSPTemplate' = PayloadField(alias='CspTemplate', default=None)
    disabled: bool = PayloadField(alias='Disabled', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    encryption_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='EncryptionKeyAlgorithm', default=None)
    encryption_key_dn: str = PayloadField(alias='EncryptionKeyDn', default=None)
    expiration: int = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    max_uses: int = PayloadField(alias='MaxUses', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    signing_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='SigningKeyAlgorithm', default=None)
    signing_key_dn: str = PayloadField(alias='SigningKeyDn', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)


class DotNetTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    disabled: bool = PayloadField(alias='Disabled', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    expiration: 'InfoValue' = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_container_dn: 'InfoValue' = PayloadField(alias='KeyContainerDn', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses', default=None)
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    type: str = PayloadField(alias='Type', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class DotNetEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    dot_net_template: 'DotNetTemplate' = PayloadField(alias='DotNetTemplate', default=None)
    disabled: bool = PayloadField(alias='Disabled', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    expiration: int = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyAlgorithm', default=None)
    key_dn: str = PayloadField(alias='KeyDn', default=None)
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    max_uses: int = PayloadField(alias='MaxUses', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)


class GPGTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    authentication_key_algorithm: 'InfoValue' = PayloadField(alias='AuthenticationKeyAlgorithm', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    email: 'InfoValue' = PayloadField(alias='Email', default=None)
    encryption_key_algorithm: 'InfoValue' = PayloadField(alias='EncryptionKeyAlgorithm', default=None)
    expiration: 'InfoValue' = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    max_uses: 'InfoValue' = PayloadField(alias='MaxUses', default=None)
    object_naming_pattern: str = PayloadField(alias='ObjectNamingPattern', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    read_only: bool = PayloadField(alias='ReadOnly', default=None)
    real_name: 'InfoValue' = PayloadField(alias='RealName', default=None)
    signing_key_algorithm: 'InfoValue' = PayloadField(alias='SigningKeyAlgorithm', default=None)
    type: str = PayloadField(alias='Type', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class GPGEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    authentication_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='AuthenticationKeyAlgorithm', default=None)
    custom_fields_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldsAttributes', default=None)
    dirty: bool = PayloadField(alias='Dirty', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    email: List[str] = PayloadField(alias='Email', default=None)
    encryption_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='EncryptionKeyAlgorithm', default=None)
    expiration: int = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    gpg_template: 'GPGTemplate' = PayloadField(alias='GpgTemplate', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    max_uses: int = PayloadField(alias='MaxUses', default=None)
    per_user: bool = PayloadField(alias='PerUser', default=None)
    real_name: 'EnvironmentTemplateDetails' = PayloadField(alias='RealName', default=None)
    read_only: bool = PayloadField(alias='ReadOnly', default=None)
    signing_key_algorithm: 'EnvironmentTemplateDetails' = PayloadField(alias='SigningKeyAlgorithm', default=None)
    status: int = PayloadField(alias='Status', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)
    type: str = PayloadField(alias='Type', default=None)


class KeyPairTemplate(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    description: str = PayloadField(alias='Description', default=None)
    dirty: bool = PayloadField(alias='Dirty', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    expiration: 'InfoValue' = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_container_dn: str = PayloadField(alias='KeyContainerDn', default=None)
    key_storage_location: 'InfoValue' = PayloadField(alias='KeyStorageLocation', default=None)
    max_uses: int = PayloadField(alias='MaxUses', default=None)
    type: str = PayloadField(alias='Type', default=None)
    validity_period: int = PayloadField(alias='ValidityPeriod', default=None)
    visible_to: 'Items' = PayloadField(alias='VisibleTo', default=None)


class KeyPairEnvironment(PayloadModel):
    allow_user_key_import: bool = PayloadField(alias='AllowUserKeyImport', default=None)
    custom_fields_attributes: 'List[CustomFieldAttributes]' = PayloadField(alias='CustomFieldsAttributes', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    expiration: int = PayloadField(alias='Expiration', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    ip_address_restriction: 'Items' = PayloadField(alias='IpAddressRestriction', default=None)
    key_algorithm: 'InfoValue' = PayloadField(alias='KeyAlgorithm', default=None)
    key_dn: str = PayloadField(alias='KeyDn', default=None)
    key_pair_template: 'KeyPairTemplate' = PayloadField(alias='KeyPairTemplate', default=None)
    key_storage_location: 'EnvironmentTemplateDetails' = PayloadField(alias='KeyStorageLocation', default=None)
    key_time_constraints: 'Items' = PayloadField(alias='KeyTimeConstraints', default=None)
    key_use_flow_dn: str = PayloadField(alias='KeyUseFlowDn', default=None)
    status: int = PayloadField(alias='Status', default=None)
    template_dn: str = PayloadField(alias='TemplateDn', default=None)
    type: str = PayloadField(alias='Type', default=None)


class KeyStorageLocations(PayloadModel):
    items: List[str] = PayloadField(alias='Items', default=None)


class Application(PayloadModel):
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)


class ApplicationCollection(PayloadModel):
    application_dns: 'Items' = PayloadField(alias='ApplicationDns', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)


class GlobalConfiguration(PayloadModel):
    approved_key_storage_locations: 'KeyStorageLocations' = PayloadField(alias='ApprovedKeyStorageLocations', default=None)
    available_key_storage_locations: 'KeyStorageLocations' = PayloadField(alias='AvailableKeyStorageLocations', default=None)
    default_ca_container: str = PayloadField(alias='DefaultCaContainer', default=None)
    default_certificate_container: str = PayloadField(alias='DefaultCertificateContainer', default=None)
    default_credential_container: str = PayloadField(alias='DefaultCredentialContainer', default=None)
    key_use_timeout: int = PayloadField(alias='KeyUseTimeout', default=None)
    project_description_tooltip: str = PayloadField(alias='ProjectDescriptionTooltip', default=None)
    request_in_progress_message: str = PayloadField(alias='RequestInProgressMessage', default=None)


class Project(PayloadModel):
    application_dns: 'Items' = PayloadField(alias='ApplicationDns', default=None)
    applications: 'List[Application]' = PayloadField(alias='Applications', default=None)
    auditors: 'Items' = PayloadField(alias='Auditors', default=None)
    certificate_environments: 'List[CertificateEnvironment]' = PayloadField(alias='CertificateEnvironments', default=None)
    collections: 'List[SignApplicationCollection]' = PayloadField(alias='Collections', default=None)
    created_on: datetime = PayloadField(alias='CreatedOn', default=None)
    description: str = PayloadField(alias='Description', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    key_use_approvers: 'Items' = PayloadField(alias='KeyUseApprovers', default=None)
    key_users: 'Items' = PayloadField(alias='KeyUsers', default=None)
    owners: 'Items' = PayloadField(alias='Owners', default=None)
    status: int = PayloadField(alias='Status', default=None)


class Rights(PayloadModel):
    none: int = PayloadField(alias='None', default=None)
    admin: int = PayloadField(alias='Admin', default=None)
    use: int = PayloadField(alias='Use', default=None)
    audit: int = PayloadField(alias='Audit', default=None)
    owner: int = PayloadField(alias='Owner', default=None)
    project_approval: int = PayloadField(alias='ProjectApproval', default=None)
    application_admin: int = PayloadField(alias='ApplicationAdmin', default=None)
    approve_use: int = PayloadField(alias='ApproveUse', default=None)


class SignApplicationCollection(PayloadModel):
    description: str = PayloadField(alias='Description', default=None)
    dn: str = PayloadField(alias='Dn', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    hash: str = PayloadField(alias='Hash', default=None)
    id: int = PayloadField(alias='Id', default=None)
    location: str = PayloadField(alias='Location', default=None)
    permitted_argument_pattern: str = PayloadField(alias='PermittedArgumentPattern', default=None)
    signatory_issuer: str = PayloadField(alias='SignatoryIssuer', default=None)
    signatory_subject: str = PayloadField(alias='SignatorySubject', default=None)
    size: int = PayloadField(alias='Size', default=None)
    version: str = PayloadField(alias='Version', default=None)
