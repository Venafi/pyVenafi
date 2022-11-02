from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.client_group_base import ClientGroupBaseAttributes


class UntrustedClientGroupAttributes(ClientGroupBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Untrusted Client Group"
