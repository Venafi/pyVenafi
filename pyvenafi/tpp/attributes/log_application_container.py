from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes

class LogApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Application Container"
