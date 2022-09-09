from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class ClientWorkRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Work Root"
