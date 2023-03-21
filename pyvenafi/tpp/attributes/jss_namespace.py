from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class JSSNamespaceAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Namespace"
    contact = Attribute('Contact')
    description = Attribute('Description')
    disabled = Attribute('Disabled')
    discovered_by_dn = Attribute('Discovered By DN')
    jss_namespace_name = Attribute('JSS Namespace Name')
    last_sync = Attribute('Last Sync')
