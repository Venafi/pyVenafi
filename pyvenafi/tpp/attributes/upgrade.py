from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class UpgradeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Upgrade"
    grouping_id = Attribute('Grouping Id', min_version='21.4')
