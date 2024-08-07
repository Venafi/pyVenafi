from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class LogFilterAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Filter"
    filter_ids = Attribute('Filter IDs', min_version='21.4')
    filter_severity = Attribute('Filter Severity', min_version='21.4')
    log_channel = Attribute('Log Channel', min_version='21.4')
