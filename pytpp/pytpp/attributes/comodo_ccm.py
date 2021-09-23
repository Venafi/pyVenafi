from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class ComodoCCMAttributes(CertificateAuthorityBaseAttributes, metaclass=PropertyMeta):
	customer_login_uri = Attribute('Customer Login URI')
	organization = Attribute('Organization')
	secret_key = Attribute('Secret Key')
