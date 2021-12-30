from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ResultCode:
    code: int
    codesign_result: str


@dataclass
class Items:
    items: List[str]


@dataclass
class InfoValue:
    info: int
    value: 'Items'


@dataclass
class RightsKeyValue:
    key: str
    value: int


@dataclass
class CertificateTemplate:
    allow_user_key_import: bool
    certificate_authority_dn: 'InfoValue'
    certificate_subject: str
    city: 'InfoValue'
    country: 'InfoValue'
    dn: str
    guid: str
    id: int
    key_algorithm: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    object_naming_pattern: str
    organization: 'InfoValue'
    organizational_unit: 'InfoValue'
    per_user: bool
    san_email: 'InfoValue'
    state: 'InfoValue'
    target_policy_dn: str
    type: str
    visible_to: 'Items'


@dataclass
class CertificateEnvironment:
    allow_user_key_import: bool
    certificate_authority_dn: 'InfoValue'
    certificate_dn: str
    certificate_stage: int
    certificate_status_text: str
    certificate_subject: str
    certificate_template: 'CertificateTemplate'
    city: 'InfoValue'
    country: 'InfoValue'
    dn: str
    grouping: int
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_algorithm: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    object_naming_pattern: str
    organization: 'InfoValue'
    organizational_unit: 'InfoValue'
    per_user: bool
    read_only: bool
    san_email: 'InfoValue'
    state: 'InfoValue'
    target_policy_dn: str
    template_dn: str
    type: str
    visible_to: 'Items'


@dataclass
class KeyStorageLocations:
    items: List[str]


@dataclass
class Application:
    dn: str
    guid: str
    id: int


@dataclass
class ApplicationCollection:
    application_dns: 'Items'
    dn: str
    guid: str
    id: int


@dataclass
class CSPTemplate:
    allow_user_key_import: bool
    dn: str
    encryption_key_algorithm: 'InfoValue'
    expiration: 'InfoValue'
    guid: str
    id: int
    key_storage_location: 'InfoValue'
    max_uses: 'InfoValue'
    signing_key_algorithm: 'InfoValue'
    type: str
    visible_to: 'Items'


@dataclass
class DotNetTemplate:
    allow_user_key_import: bool
    description: str
    dn: str
    encryption_key_algorithm: 'InfoValue'
    expiration: 'InfoValue'
    guid: str
    id: int
    key_algorithm: 'InfoValue'
    key_container_dn: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    max_uses: 'InfoValue'
    type: str
    visible_to: 'Items'


@dataclass
class GPGTemplate:
    allow_user_key_import: bool
    authentication_key_algorithm: 'InfoValue'
    dn: str
    email: 'InfoValue'
    encryption_key_algorithm: 'InfoValue'
    expiration: 'InfoValue'
    guid: str
    id: int
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    max_uses: 'InfoValue'
    object_naming_pattern: str
    per_user: bool
    real_name: 'InfoValue'
    signing_key_algorithm: 'InfoValue'
    type: str
    visible_to: 'Items'


@dataclass
class GlobalConfiguration:
    approved_key_storage_locations: 'KeyStorageLocations'
    available_key_storage_locations: 'KeyStorageLocations'
    default_ca_container: str
    default_certificate_container: str
    default_credential_container: str
    key_use_timeout: int
    project_description_tooltip: str
    request_in_progress_message: str


@dataclass
class Project:
    application_dns: 'Items'
    applications: 'List[Application]'
    auditors: 'Items'
    certificate_environments: 'List[CertificateEnvironment]'
    collections: 'List[SignApplicationCollection]'
    created_on: datetime
    description: str
    dn: str
    guid: str
    id: int
    key_use_approvers: 'Items'
    key_users: 'Items'
    owners: 'Items'
    status: int


@dataclass
class Rights:
    none: int
    admin: int
    use: int
    audit: int
    owner: int
    project_approval: int
    application_admin: int
    approve_use: int


@dataclass
class SignApplicationCollection:
    description: str
    dn: str
    guid: str
    hash: str
    id: int
    location: str
    permitted_argument_pattern: str
    signatory_issuer: str
    signatory_subject: str
    size: int
    version: str
