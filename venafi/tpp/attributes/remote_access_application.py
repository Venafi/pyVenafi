from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class RemoteAccessApplicationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Remote Access Application"
