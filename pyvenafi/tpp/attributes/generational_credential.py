from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.credential_base import CredentialBaseAttributes

class GenerationalCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Generational Credential"
    last = Attribute('Last', min_version='21.4')
    visibility = Attribute('Visibility', min_version='21.4')
