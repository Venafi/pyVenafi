from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.flow import FlowAttributes


class OAuthDeviceAuthorizationFlowAttributes(FlowAttributes, metaclass=IterableMeta):
    __config_class__ = "OAuth Device Authorization Flow"
    expiration = Attribute('Expiration')
    retry_interval = Attribute('Retry Interval')
