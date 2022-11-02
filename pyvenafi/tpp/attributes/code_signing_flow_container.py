from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningFlowContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Flow Container"
