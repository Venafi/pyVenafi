from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from venafi.tpp.attributes.top import TopAttributes


class JumpServerAttributes(ConnectionBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Jump Server"
    consumers = Attribute('Consumers')
    location = Attribute('Location')
    ssh_connection_string = Attribute('SSH Connection String')
    ssh_version = Attribute('SSH Version')
