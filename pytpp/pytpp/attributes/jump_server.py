from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.connection_base import ConnectionBaseAttributes
from pytpp.attributes.top import TopAttributes


class JumpServerAttributes(ConnectionBaseAttributes, TopAttributes, metaclass=PropertyMeta):
	consumers = Attribute('Consumers')
	location = Attribute('Location')
	ssh_connection_string = Attribute('SSH Connection String')
	ssh_version = Attribute('SSH Version')
