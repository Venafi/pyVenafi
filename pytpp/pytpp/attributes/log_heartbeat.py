from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogHeartbeatAttributes(TopAttributes, metaclass=PropertyMeta):
	event = Attribute('Event')
	rule = Attribute('Rule')
	timeout = Attribute('Timeout')
