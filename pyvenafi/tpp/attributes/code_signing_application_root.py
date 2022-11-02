from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningApplicationRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Application Root"
