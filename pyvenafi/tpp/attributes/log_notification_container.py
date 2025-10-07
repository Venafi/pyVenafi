from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class LogNotificationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Notification Container"
    description = Attribute('Description')
