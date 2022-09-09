from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class LogApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Application Container"
