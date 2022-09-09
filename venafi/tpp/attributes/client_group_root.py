from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class ClientGroupRootAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Group Root"
