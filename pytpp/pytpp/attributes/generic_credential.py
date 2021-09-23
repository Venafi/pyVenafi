from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.credential_base import CredentialBaseAttributes


class GenericCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	pass