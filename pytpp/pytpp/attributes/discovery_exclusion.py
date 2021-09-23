from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.exclusion import ExclusionAttributes


class DiscoveryExclusionAttributes(ExclusionAttributes, metaclass=PropertyMeta):
	address_range = Attribute('Address Range')
	managed_by_discovery_dn = Attribute('Managed By Discovery DN')
	managed_dn = Attribute('Managed DN')
	port_range = Attribute('Port Range')
