from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.encryption_driver import EncryptionDriverAttributes

class DPAPIEncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "DPAPI Encryption Driver"
    generation_only = Attribute('Generation Only', min_version='21.4')
    key_validation = Attribute('Key Validation', min_version='21.4')
    verigram = Attribute('VeriGram', min_version='21.4')
