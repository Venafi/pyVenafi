from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.http_ca_base import HTTPCABaseAttributes
from venafi.tpp.attributes.proxy import ProxyAttributes


class SymantecLHKCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
    __config_class__ = "Symantec LHK CA"
    fields = Attribute('Fields')
    uri = Attribute('URI')
