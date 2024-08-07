from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class LogNotificationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Notification"
    factory_rule = Attribute('Factory Rule')
    log_channel = Attribute('Log Channel')
    rule = Attribute('Rule')
