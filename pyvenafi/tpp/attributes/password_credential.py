from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes

class PasswordCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Password Credential"
