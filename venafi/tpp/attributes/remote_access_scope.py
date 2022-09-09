from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class RemoteAccessScopeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Remote Access Scope"
