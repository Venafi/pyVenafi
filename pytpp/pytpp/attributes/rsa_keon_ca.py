from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class RSAKeonCAAttributes(CertificateAuthorityBaseAttributes, metaclass=PropertyMeta):
	ca_md5 = Attribute('CA MD5')
	ca_name = Attribute('CA Name')
	certificate_block = Attribute('Certificate Block')
	jurisdiction_id = Attribute('Jurisdiction ID')
	jurisdiction_name = Attribute('Jurisdiction Name')
	supported_validity_periods = Attribute('Supported Validity Periods')
