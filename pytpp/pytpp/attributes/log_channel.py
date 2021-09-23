from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogChannelAttributes(TopAttributes, metaclass=PropertyMeta):
	configuration = Attribute('Configuration')
	driver_arguments = Attribute('Driver Arguments')
