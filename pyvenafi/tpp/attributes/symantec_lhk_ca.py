from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from pyvenafi.tpp.attributes.proxy import ProxyAttributes


class SymantecLHKCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "Symantec LHK CA"
    fields = Attribute('Fields')
    uri = Attribute('URI')
