from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class CodeSigningApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Application Container"
