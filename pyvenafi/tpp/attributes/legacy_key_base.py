from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class LegacyKeyBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Legacy Key Base"
    algorithm = Attribute('Algorithm', min_version='21.4')
    approver = Attribute('Approver', min_version='21.4')
    key_bit_strength = Attribute('Key Bit Strength', min_version='21.4')
    key_vault_id = Attribute('Key Vault Id', min_version='21.4')
    protection_key = Attribute('Protection Key', min_version='21.4')
