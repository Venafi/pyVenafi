from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class SSHCATemplateContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH CA Template Container"
