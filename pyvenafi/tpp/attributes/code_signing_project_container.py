from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes

class CodeSigningProjectContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Project Container"
