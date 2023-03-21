from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class JSSClusterAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Cluster"
    contact = Attribute('Contact')
    description = Attribute('Description')
    disabled = Attribute('Disabled')
    discovered_by_dn = Attribute('Discovered By DN')
    jss_cluster_name = Attribute('JSS Cluster Name')
    jss_cluster_type = Attribute('JSS Cluster Type')
    jss_last_seen = Attribute('JSS Last Seen')
    jss_status = Attribute('JSS Status')
    last_sync = Attribute('Last Sync')
