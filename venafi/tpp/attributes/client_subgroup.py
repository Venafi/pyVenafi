from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.client_group_base import ClientGroupBaseAttributes


class ClientSubgroupAttributes(ClientGroupBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Subgroup"
