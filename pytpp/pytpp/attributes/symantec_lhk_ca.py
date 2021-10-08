from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class SymantecLHKCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=PropertyMeta):
	fields = Attribute('Fields')
	uri = Attribute('URI')
