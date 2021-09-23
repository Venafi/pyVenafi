from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class IdentityDriverAttributes(DriverBaseAttributes, metaclass=PropertyMeta):
	display_name_attributes = Attribute('Display Name Attributes', min_version='15.3')
	mapping_table = Attribute('Mapping Table')
