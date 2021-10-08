from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class PrivateKeyCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	username = Attribute('Username')
