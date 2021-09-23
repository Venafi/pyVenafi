from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class DriverBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	driver_arguments = Attribute('Driver Arguments')
	driver_name = Attribute('Driver Name')
	rank = Attribute('Rank')
