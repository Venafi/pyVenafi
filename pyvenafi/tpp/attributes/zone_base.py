from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class ZoneBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Zone Base"
    address_range = Attribute('Address Range', min_version='21.4')
    window_end = Attribute('Window End', min_version='21.4')
    window_start = Attribute('Window Start', min_version='21.4')
    zone_contact = Attribute('Zone Contact', min_version='21.4')
    zone_description = Attribute('Zone Description', min_version='21.4')
