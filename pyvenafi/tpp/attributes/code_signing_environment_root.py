from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningEnvironmentRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Root"
