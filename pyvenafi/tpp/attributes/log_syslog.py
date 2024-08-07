from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogSyslogAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Syslog"
    credential = Attribute('Credential', min_version='21.4')
    enable_tls = Attribute('Enable TLS', min_version='21.4')
    facility = Attribute('Facility', min_version='21.4')
    message_format = Attribute('Message Format', min_version='21.4')
    message_prefix = Attribute('Message Prefix', min_version='21.4')
    port = Attribute('Port', min_version='21.4')
    protocol = Attribute('Protocol', min_version='21.4')
    target = Attribute('Target', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
