from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class XolphinCAAttributes(CertificateAuthorityBaseAttributes, metaclass=PropertyMeta):
	brand = Attribute('Brand')
	included_domains = Attribute('Included Domains')
	product = Attribute('Product')
	type = Attribute('Type')
