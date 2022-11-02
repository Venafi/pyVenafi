from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes


class UsernamePasswordCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Username Password Credential"
    username = Attribute('Username')
