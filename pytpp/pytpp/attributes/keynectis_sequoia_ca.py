from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes


class KeynectisSequoiaCAAttributes(HTTPCABaseAttributes, metaclass=PropertyMeta):
	csr_format_name = Attribute('CSR Format Name')
	csr_name = Attribute('CSR Name')
	customer = Attribute('Customer')
	encryption_certificate = Attribute('Encryption Certificate')
	enrollment_mode = Attribute('Enrollment Mode')
	enterprise = Attribute('Enterprise')
	fields = Attribute('Fields')
	offer = Attribute('Offer')
	uri = Attribute('URI')
