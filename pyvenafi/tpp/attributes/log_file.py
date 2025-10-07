from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogFileAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log File"
    expiration = Attribute('Expiration', min_version='21.4')
    language = Attribute('Language', min_version='21.4')
    log_directory = Attribute('Log Directory', min_version='21.4')
    max_fileage = Attribute('Max Fileage', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    translate = Attribute('Translate', min_version='21.4')
