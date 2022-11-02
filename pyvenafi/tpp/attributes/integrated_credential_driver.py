from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.credential_driver_base import CredentialDriverBaseAttributes


class IntegratedCredentialDriverAttributes(CredentialDriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Integrated Credential Driver"
