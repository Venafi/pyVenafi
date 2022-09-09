from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.credential_base import CredentialBaseAttributes


class GenericCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Generic Credential"
