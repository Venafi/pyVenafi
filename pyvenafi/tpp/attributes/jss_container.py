from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class JSSContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Container"
    contact = Attribute('Contact')
    description = Attribute('Description')
    discovered_by_dn = Attribute('Discovered By DN')
    jss_organization_name = Attribute('JSS Organization Name')
    last_sync = Attribute('Last Sync')
