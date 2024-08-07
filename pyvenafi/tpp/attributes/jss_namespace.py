from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class JSSNamespaceAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Namespace"
    contact = Attribute('Contact', min_version='22.4')
    description = Attribute('Description', min_version='22.4')
    disabled = Attribute('Disabled', min_version='22.4')
    discovered_by_dn = Attribute('Discovered By DN', min_version='22.4')
    jss_namespace_name = Attribute('JSS Namespace Name', min_version='22.4')
    last_sync = Attribute('Last Sync', min_version='22.4')
