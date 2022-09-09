from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class ClientWorkContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Work Container"
