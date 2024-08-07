from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ExclusionAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Exclusion"
    rule = Attribute('Rule', min_version='21.4')
