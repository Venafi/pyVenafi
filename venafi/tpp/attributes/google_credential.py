from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.credential_base import CredentialBaseAttributes


class GoogleCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Google Credential"
