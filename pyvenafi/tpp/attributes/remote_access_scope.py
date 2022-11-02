from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class RemoteAccessScopeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Remote Access Scope"
