from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.encryption_driver import EncryptionDriverAttributes

class Pkcs11EncryptionDriverAttributes(EncryptionDriverAttributes, metaclass=IterableMeta):
    __config_class__ = "Pkcs11 Encryption Driver"
    account_type = Attribute('Account Type', min_version='21.4')
    credential = Attribute('Credential', min_version='21.4')
    cryptokipath = Attribute('CryptokiPath', min_version='21.4')
    dsn = Attribute('DSN', min_version='21.4')
    default_key = Attribute('Default Key', min_version='21.4')
    encrypted_pin = Attribute('Encrypted Pin', min_version='21.4')
    fallback_pin = Attribute('Fallback Pin', min_version='21.4')
    key_derivation = Attribute('Key Derivation', min_version='22.1')
    key_generation = Attribute('Key Generation', min_version='21.4')
    key_storage = Attribute('Key Storage', min_version='21.4')
    key_validation = Attribute('Key Validation', min_version='21.4')
    permitted_keys = Attribute('Permitted Keys', min_version='21.4')
    slot_id = Attribute('Slot Id', min_version='21.4')
    token_label = Attribute('Token Label', min_version='21.4')
    token_serial = Attribute('Token Serial', min_version='21.4')
    verigram = Attribute('VeriGram', min_version='21.4')
