from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogChannelContainerAttributes(TopAttributes, metaclass=PropertyMeta):
	description = Attribute('Description')
