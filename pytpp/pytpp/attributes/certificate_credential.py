from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class CertificateCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	certificate = Attribute('Certificate')
