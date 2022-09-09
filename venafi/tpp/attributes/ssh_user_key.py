from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.ssh_key import SSHKeyAttributes


class SSHUserKeyAttributes(SSHKeyAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH User Key"
