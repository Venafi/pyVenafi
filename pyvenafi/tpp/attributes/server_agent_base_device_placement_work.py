from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class ServerAgentBaseDevicePlacementWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Server Agent Base Device Placement Work"
    device_object_location = Attribute('Device Object Location', min_version='21.4')
    device_share_mode = Attribute('Device Share Mode', min_version='21.4')
