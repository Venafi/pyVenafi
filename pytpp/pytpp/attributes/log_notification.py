from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LogNotificationAttributes(TopAttributes, metaclass=PropertyMeta):
	log_channel = Attribute('Log Channel')
	rule = Attribute('Rule')
