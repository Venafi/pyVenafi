from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class UniCERTCAAttributes(CertificateAuthorityBaseAttributes, metaclass=PropertyMeta):
	ca_dn = Attribute('CA DN')
	ra_dn = Attribute('RA DN')
	secure = Attribute('Secure')
	web_instance = Attribute('Web Instance')
