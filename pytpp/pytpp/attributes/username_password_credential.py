from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class UsernamePasswordCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	username = Attribute('Username')
