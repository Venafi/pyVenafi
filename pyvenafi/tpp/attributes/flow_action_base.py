from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class FlowActionBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Action Base"
    rank = Attribute('Rank', min_version='21.4')
