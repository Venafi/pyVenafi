from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class RemoteAccessApplicationContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Remote Access Application Container"
