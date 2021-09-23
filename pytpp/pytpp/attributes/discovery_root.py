from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class DiscoveryRootAttributes(BranchBaseAttributes, metaclass=PropertyMeta):
	address_range = Attribute('Address Range')
	dsn = Attribute('DSN')
	driver_name = Attribute('Driver Name')
	protection_key = Attribute('Protection Key')
	timeout = Attribute('Timeout')
