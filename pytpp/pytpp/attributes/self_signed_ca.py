from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class SelfSignedCAAttributes(CertificateAuthorityBaseAttributes, metaclass=PropertyMeta):
	algorithm = Attribute('Algorithm')
	enhanced_key_usage = Attribute('Enhanced Key Usage')
	key_usage = Attribute('Key Usage')
