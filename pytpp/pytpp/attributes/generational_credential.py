from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class GenerationalCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	last = Attribute('Last')
	visibility = Attribute('Visibility')
