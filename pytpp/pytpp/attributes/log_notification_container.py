from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogNotificationContainerAttributes(TopAttributes, metaclass=PropertyMeta):
	description = Attribute('Description')
