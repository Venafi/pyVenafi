from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class VerizonCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=PropertyMeta):
	admin_email = Attribute('Admin Email')
	admin_firstname = Attribute('Admin Firstname')
	admin_surname = Attribute('Admin Surname')
	admin_telnumber = Attribute('Admin Telnumber')
	certificate_block = Attribute('Certificate Block')
