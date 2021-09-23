from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.client_group_base import ClientGroupBaseAttributes


class ClientGroupAttributes(ClientGroupBaseAttributes, metaclass=PropertyMeta):
	agent_type = Attribute('Agent Type', min_version='15.2')
