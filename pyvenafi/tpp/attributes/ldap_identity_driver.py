from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.identity_driver import IdentityDriverAttributes

class LDAPIdentityDriverAttributes(IdentityDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "LDAP Identity Driver"
    additional_name_attributes = Attribute('Additional Name Attributes', min_version='22.3')
    ambiguous_name_resolution = Attribute('Ambiguous Name Resolution', min_version='21.4')
    base_dn = Attribute('Base DN', min_version='21.4')
    configuration = Attribute('Configuration', min_version='21.4')
    connection_timeout = Attribute('Connection Timeout', min_version='21.4')
    container_class_name = Attribute('Container Class Name', min_version='21.4')
    container_query_expression = Attribute('Container Query Expression', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    friendly_name = Attribute('Friendly Name', min_version='21.4')
    group_class_name = Attribute('Group Class Name', min_version='21.4')
    group_query_expression = Attribute('Group Query Expression', min_version='21.4')
    group_search_root = Attribute('Group Search Root', min_version='21.4')
    host = Attribute('Host', min_version='21.4')
    internal_identifier = Attribute('Internal Identifier', min_version='21.4')
    lockout_timestamp_attribute = Attribute('Lockout Timestamp Attribute', min_version='22.3')
    login_name_resolution = Attribute('Login Name Resolution', min_version='21.4')
    member_identifier = Attribute('Member Identifier', min_version='21.4')
    memberof_enabled = Attribute('MemberOf Enabled', min_version='21.4')
    membership_resolution = Attribute('Membership Resolution', min_version='21.4')
    port = Attribute('Port', min_version='21.4')
    resolve_nested_groups = Attribute('Resolve Nested Groups', min_version='21.4')
    revocation = Attribute('Revocation', min_version='21.4')
    search_root = Attribute('Search Root', min_version='21.4')
    secure = Attribute('Secure', min_version='21.4')
    size_limit = Attribute('Size Limit', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    title = Attribute('Title', min_version='21.4')
    universal_identifier = Attribute('Universal Identifier', min_version='21.4')
    user_class_name = Attribute('User Class Name', min_version='21.4')
    user_query_expression = Attribute('User Query Expression', min_version='21.4')
    vault_id = Attribute('Vault Id', min_version='21.4')
    vendor = Attribute('Vendor', min_version='21.4')
