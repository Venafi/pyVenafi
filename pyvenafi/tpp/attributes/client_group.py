from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.client_group_base import ClientGroupBaseAttributes


class ClientGroupAttributes(ClientGroupBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Group"
    agent_type = Attribute('Agent Type')
