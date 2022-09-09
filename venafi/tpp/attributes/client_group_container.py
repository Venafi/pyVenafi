from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class ClientGroupContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Group Container"
