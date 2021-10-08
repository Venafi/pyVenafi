from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogSplunkAttributes(LogChannelAttributes, metaclass=PropertyMeta):
	credential = Attribute('Credential')
	host = Attribute('Host')
	index = Attribute('Index')
	port = Attribute('Port')
	source = Attribute('Source')
	timeout = Attribute('Timeout')
	verbose = Attribute('Verbose')
