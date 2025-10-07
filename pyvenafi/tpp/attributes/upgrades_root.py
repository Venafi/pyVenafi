from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class UpgradesRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Upgrades Root"
    grouping_id = Attribute('Grouping Id', min_version='21.4')
    origin_version = Attribute('Origin Version', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    stop_time = Attribute('Stop Time', min_version='21.4')
    target_version = Attribute('Target Version', min_version='21.4')
