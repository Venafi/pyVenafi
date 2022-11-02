from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.ssh_key import SSHKeyAttributes


class SSHUserKeyAttributes(SSHKeyAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH User Key"
