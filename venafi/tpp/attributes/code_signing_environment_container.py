from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class CodeSigningEnvironmentContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Environment Container"