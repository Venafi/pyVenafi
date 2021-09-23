from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.ssh_key import SSHKeyAttributes


class SSHUserKeyAttributes(SSHKeyAttributes, metaclass=PropertyMeta):
	pass