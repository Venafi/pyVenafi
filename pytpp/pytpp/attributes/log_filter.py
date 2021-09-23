from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogFilterAttributes(LogChannelAttributes, metaclass=PropertyMeta):
	filter_ids = Attribute('Filter IDs')
	filter_severity = Attribute('Filter Severity')
	log_channel = Attribute('Log Channel')
