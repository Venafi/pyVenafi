from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class SSHCATemplateContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH CA Template Container"
