from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes


class PrivateKeyCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Private Key Credential"
    username = Attribute('Username')
