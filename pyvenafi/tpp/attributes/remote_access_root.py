from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class RemoteAccessRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Remote Access Root"
    approved_issuer = Attribute('Approved Issuer', min_version='21.4')
    attempt_sid_extension_before_source_field = Attribute(
        'Attempt SID Extension Before Source Field',
        min_version='23.3'
    )
    authentication_methods = Attribute('Authentication Methods', min_version='21.4')
    certificate_auth_lookup_field = Attribute('Certificate Auth Lookup Field', min_version='21.4')
    certificate_auth_source_field = Attribute('Certificate Auth Source Field', min_version='21.4')
    certificate_auth_source_regex = Attribute('Certificate Auth Source Regex', min_version='21.4')
    certificate_pinning_options = Attribute('Certificate Pinning Options', min_version='21.4')
    certificate_pinning_work_dn = Attribute('Certificate Pinning Work DN', min_version='21.4')
    expiration = Attribute('Expiration', min_version='21.4')
    grant_validity = Attribute('Grant Validity', min_version='21.4')
    jwt_auth_source_field = Attribute('Jwt Auth Source Field', min_version='22.4')
    mapping_table = Attribute('Mapping Table', min_version='21.4')
    oauth_device_authorization_verification_uri = Attribute(
        'OAuth Device Authorization Verification URI',
        min_version='22.1'
    )
    oauth_device_authorization_verification_uri_complete_format = Attribute(
        'OAuth Device Authorization Verification URI Complete Format',
        min_version='22.1'
    )
    openapi_documentation = Attribute('OpenApi Documentation', min_version='22.4')
    refresh_api_enabled = Attribute('Refresh API Enabled', min_version='21.4')
    refresh_token_enabled = Attribute('Refresh Token Enabled', min_version='21.4')
    session_expiration_interval = Attribute('Session Expiration Interval', min_version='22.4')
    session_pool_entries = Attribute('Session Pool Entries', min_version='21.4')
    session_pool_max_age = Attribute('Session Pool Max Age', min_version='21.4')
    session_rights_refresh_age = Attribute('Session Rights Refresh Age', min_version='21.4')
    token_validity = Attribute('Token Validity', min_version='21.4')
    unused_token_expiration = Attribute('Unused Token Expiration', min_version='22.4')
