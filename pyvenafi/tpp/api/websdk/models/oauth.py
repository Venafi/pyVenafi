from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class Permissions(ObjectModel):
    delete: bool = ApiField(alias='Delete')
    discover: bool = ApiField(alias='Discover')
    manage: bool = ApiField(alias='Manage')
    read: bool = ApiField(alias='Read')
    revoke: bool = ApiField(alias='Revoke')

class DeviceConfiguration(ObjectModel):
    verification_uri: str = ApiField(alias='VerificationUri')
    verification_uri_complete_format: str = ApiField(alias='VerificationUriCompleteFormat')

class CertificateConfiguration(ObjectModel):
    attempt_sidextension_before_source_field: bool = ApiField(alias='AttemptSIDExtensionBeforeSourceField')
    source_field: str = ApiField(alias='SourceField')
    authorized_issuer_dns: list[str] = ApiField(alias='AuthorizedIssuerDns')

class Configuration(ObjectModel):
    session_pool_size: int = ApiField(alias='SessionPoolSize')
    session_pool_age: int = ApiField(alias='SessionPoolAge')
    session_pool_expiration_interval: int = ApiField(alias='SessionPoolExpirationInterval')
    session_rights_refresh_interval: int = ApiField(alias='SessionRightsRefreshInterval')
    strict_expiration: bool = ApiField(alias='StrictExpiration')
    statistics_api_tracking: bool = ApiField(alias='StatisticsApiTracking')
    statistics_tracking_includes_time: bool = ApiField(alias='StatisticsTrackingIncludesTime')
    open_api_enabled: bool = ApiField(alias='OpenApiEnabled')
    open_api_ui: str = ApiField(alias='OpenApiUi')
    default_access_token_validity: int = ApiField(alias='DefaultAccessTokenValidity')
    default_grant_validity: int = ApiField(alias='DefaultGrantValidity')
    default_grant_refreshable: bool = ApiField(alias='DefaultGrantRefreshable')
    unused_access_token_expiration: int = ApiField(alias='UnusedAccessTokenExpiration')
    refresh_endpoint_enabled: bool = ApiField(alias='RefreshEndpointEnabled')
    authorize_by_password: bool = ApiField(alias='AuthorizeByPassword')
    authorize_by_certificate: bool = ApiField(alias='AuthorizeByCertificate')
    authorize_by_integrated: bool = ApiField(alias='AuthorizeByIntegrated')
    authorize_by_jwt: bool = ApiField(alias='AuthorizeByJwt')
    authorize_device: bool = ApiField(alias='AuthorizeDevice')
    device_configuration: DeviceConfiguration = ApiField(alias='DeviceConfiguration')
    certificate_configuration: CertificateConfiguration = ApiField(alias='CertificateConfiguration')

class OwnedApplication(ObjectModel):
    application_id: str = ApiField(alias='ApplicationId')
    role: int = ApiField(alias='Role')

class Role(ObjectModel):
    role: int = ApiField(alias='Role')
    grantee: str = ApiField(alias='Grantee')
    application_id: str = ApiField(alias='ApplicationId')
    permitted_applications: list[str] = ApiField(alias='PermittedApplications')
    owned_applications: list[OwnedApplication] = ApiField(alias='OwnedApplications')

class Application(ObjectModel):
    access_validity: str = ApiField(alias='AccessValidity')
    description: str = ApiField(alias='Description')
    grant_count: str = ApiField(alias='GrantCount')
    grant_validity: str = ApiField(alias='GrantValidity')
    id: str = ApiField(alias='ID')
    maximum_scope: str = ApiField(alias='MaximumScope')
    name: str = ApiField(alias='Name')
    renewable: str = ApiField(alias='Renewable')
    scope: str = ApiField(alias='Scope')
    unused_expiration: str = ApiField(alias='UnusedExpiration')
    url: str = ApiField(alias='Url')
    user_count: str = ApiField(alias='UserCount')
    vendor: str = ApiField(alias='Vendor')

class Scope(ObjectModel):
    scope: str = ApiField(alias='Scope')
    restrictionList: list[str] = ApiField(alias='RestrictionList')

class Grant(ObjectModel):
    scope: str = ApiField(alias='Scope')
    access_token: str = ApiField(alias='AccessToken')
    valid_for: int = ApiField(alias='ValidFor')
    access_issued_on: str = ApiField(alias='AccessIssuedOn')
    access_issued_on_unix_time: int = ApiField(alias='AccessIssuedOnUnixTime')
    access_issued_on_iso_8601: str = ApiField(alias='AccessIssuedOnISO8601')
    refresh_token: str = ApiField(alias='RefreshToken')
    expires: str = ApiField(alias='Expires')
    expires_unix_time: int = ApiField(alias='ExpiresUnixTime')
    expires_iso_8601: str = ApiField(alias='ExpiresISO8601')
    grant_issued_on: str = ApiField(alias='GrantIssuedOn')
    grant_issued_on_unix_time: int = ApiField(alias='GrantIssuedOnUnixTime')
    grant_issued_on_iso_8601: str = ApiField(alias='GrantIssuedOnISO8601')
    application: str = ApiField(alias='Application')
    grantee_prefixed_universal: str = ApiField(alias='GranteePrefixedUniversal')
    granted_to_prefixed_universal: str = ApiField(alias='GrantedToPrefixedUniversal')

class Rule(ObjectModel):
    description: str = ApiField(alias='Description')
    maximum_scope: str = ApiField(alias='MaximumScope')
    access_validity: int = ApiField(alias='AccessValidity')
    grant_validity: int = ApiField(alias='GrantValidity')
    renewable: bool = ApiField(alias='Renewable')
    trustee_prefixed_universal: str = ApiField(alias='TrusteePrefixedUniversal')
    application_id: str = ApiField(alias='ApplicationId')

class JwtMapping(ObjectModel):
    issuer_uri: str = ApiField(alias='IssuerUri')
    purpose_field: str = ApiField(alias='PurposeField')
    purpose_match: str = ApiField(alias='PurposeMatch')
    id_field: str = ApiField(alias='IdField')
    id_match: str = ApiField(alias='IdMatch')
    grantee_prefixed_universal: str = ApiField(alias='GranteePrefixedUniversal')
    name: str = ApiField(alias='Name')
