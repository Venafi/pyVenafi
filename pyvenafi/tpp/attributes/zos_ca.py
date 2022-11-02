from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from pyvenafi.tpp.attributes.proxy import ProxyAttributes


class zOSCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "zOS CA"
    client_port = Attribute('Client Port')
    client_secure = Attribute('Client Secure')
    domain = Attribute('Domain')
    secure = Attribute('Secure')
