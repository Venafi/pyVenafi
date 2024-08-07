from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes

class SpiLoggerAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Spi Logger"
    uri = Attribute('URI')
