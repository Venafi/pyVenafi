from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.identity_driver import IdentityDriverAttributes

class ActiveDirectoryIdentityDriverAttributes(IdentityDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "ActiveDirectory Identity Driver"
    base_dn = Attribute('Base DN', min_version='21.4')
    computer_class_name = Attribute('Computer Class Name', min_version='21.4')
    computer_query_expression = Attribute('Computer Query Expression', min_version='21.4')
    configuration = Attribute('Configuration', min_version='21.4')
    container_class_name = Attribute('Container Class Name', min_version='21.4')
    container_query_expression = Attribute('Container Query Expression', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    distribution_list_class_name = Attribute('Distribution List Class Name', min_version='21.4')
    distribution_list_query_expression = Attribute('Distribution List Query Expression', min_version='21.4')
    friendly_name = Attribute('Friendly Name', min_version='21.4')
    group_class_name = Attribute('Group Class Name', min_version='21.4')
    group_query_expression = Attribute('Group Query Expression', min_version='21.4')
    host = Attribute('Host', min_version='21.4')
    no_rediscovery_on = Attribute('No Rediscovery On', min_version='21.4')
    port = Attribute('Port', min_version='21.4')
    resolve_nested_groups = Attribute('Resolve Nested Groups', min_version='21.4')
    search_filter = Attribute('Search Filter', min_version='21.4')
    search_root = Attribute('Search Root', min_version='21.4')
    secure = Attribute('Secure', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    user_class_name = Attribute('User Class Name', min_version='21.4')
    user_query_expression = Attribute('User Query Expression', min_version='21.4')
    vault_id = Attribute('Vault Id', min_version='21.4')
