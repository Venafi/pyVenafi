from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class DiscoveryRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Discovery Root"
    address_range = Attribute('Address Range', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    driver_name = Attribute('Driver Name', min_version='21.4')
    protection_key = Attribute('Protection Key', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
