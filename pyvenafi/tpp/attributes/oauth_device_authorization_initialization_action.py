from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes


class OAuthDeviceAuthorizationInitializationActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "OAuth Device Authorization Initialization Action"
