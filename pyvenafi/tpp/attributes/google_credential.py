from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes


class GoogleCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Google Credential"
