from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ServiceModuleAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Service Module"
    driver_arguments = Attribute('Driver Arguments')
    driver_name = Attribute('Driver Name')
    heartbeat_interval = Attribute('Heartbeat Interval')
    interval = Attribute('Interval')
    started_by = Attribute('Started By')
