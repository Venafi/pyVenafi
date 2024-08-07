from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.key_base import KeyBaseAttributes

class KeyPairAttributes(KeyBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Key Pair"
    created_by = Attribute('Created By', min_version='21.4')
    gpg_public_key_vault_id = Attribute('GPG Public Key Vault ID', min_version='21.4')
    key_pair_renewal_flow = Attribute('Key Pair Renewal Flow', min_version='21.4')
    key_usage = Attribute('Key Usage', min_version='22.1')
    original_creation_date = Attribute('Original Creation Date', min_version='21.4')
    owner = Attribute('Owner', min_version='22.1')
    pending_private_key_vault_id = Attribute('Pending Private Key Vault Id', min_version='23.3')
    pending_public_key_vault_id = Attribute('Pending Public Key Vault Id', min_version='23.3')
    public_key_vault_id = Attribute('Public Key Vault Id', min_version='21.4')
