from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes

class CodeSigningDeleteObjectActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Delete Object Action"