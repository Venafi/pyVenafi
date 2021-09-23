from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class AutomaticPasswordCredentialAttributes(CredentialBaseAttributes, metaclass=PropertyMeta):
	self_destruct = Attribute('Self Destruct')
	usage_count = Attribute('Usage Count')
