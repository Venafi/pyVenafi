from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class CodeSigningProjectRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Project Root"
