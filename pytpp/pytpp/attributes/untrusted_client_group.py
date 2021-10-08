from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.client_group_base import ClientGroupBaseAttributes


class UntrustedClientGroupAttributes(ClientGroupBaseAttributes, metaclass=PropertyMeta):
	pass