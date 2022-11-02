from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes


class LogFileAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log File"
    expiration = Attribute('Expiration')
    language = Attribute('Language')
    log_directory = Attribute('Log Directory')
    max_fileage = Attribute('Max Fileage')
    max_filesize = Attribute('Max Filesize')
    translate = Attribute('Translate')
