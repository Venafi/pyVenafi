from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class DriverBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Driver Base"
    driver_arguments = Attribute('Driver Arguments', min_version='21.4')
    driver_name = Attribute('Driver Name', min_version='21.4')
    rank = Attribute('Rank', min_version='21.4')
