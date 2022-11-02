from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class ClientWorkRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Work Root"
