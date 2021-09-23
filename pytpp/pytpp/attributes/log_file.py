from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogFileAttributes(LogChannelAttributes, metaclass=PropertyMeta):
	expiration = Attribute('Expiration')
	language = Attribute('Language')
	log_directory = Attribute('Log Directory')
	max_fileage = Attribute('Max Fileage')
	max_filesize = Attribute('Max Filesize')
	translate = Attribute('Translate')
