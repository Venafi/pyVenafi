from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.flow import FlowAttributes


class OAuthDeviceAuthorizationFlowAttributes(FlowAttributes, metaclass=IterableMeta):
    __config_class__ = "OAuth Device Authorization Flow"
    expiration = Attribute('Expiration', min_version='22.1')
    retry_interval = Attribute('Retry Interval', min_version='22.1')
