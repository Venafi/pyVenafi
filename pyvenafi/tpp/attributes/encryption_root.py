from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.branch_base import BranchBaseAttributes

class EncryptionRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Encryption Root"
    compression_level = Attribute('Compression Level', min_version='22.3')
    encryption_driver = Attribute('Encryption Driver', min_version='21.4')
    protection_key = Attribute('Protection Key', min_version='21.4')
    rotation_log = Attribute('Rotation Log', min_version='24.1')
