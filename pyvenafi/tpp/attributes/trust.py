from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class TrustAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Trust"
    allow_from = Attribute('Allow From', min_version='21.4')
    allowed_algorithm = Attribute('Allowed Algorithm', min_version='21.4')
    allowed_command = Attribute('Allowed Command', min_version='21.4')
    allowed_vendor_types = Attribute('Allowed Vendor Types', min_version='21.4')
    automatic_rotation_enabled = Attribute('Automatic Rotation Enabled', min_version='23.3')
    automatic_rotation_interval = Attribute('Automatic Rotation Interval', min_version='23.3')
    automatic_rotation_lead_time = Attribute('Automatic Rotation Lead Time', min_version='23.3')
    contact = Attribute('Contact', min_version='21.4')
    deny_from = Attribute('Deny From', min_version='21.4')
    key_bit_strength = Attribute('Key Bit Strength', min_version='21.4')
    management_type = Attribute('Management Type', min_version='23.3')
    maximum_authorizations_per_keyset = Attribute('Maximum Authorizations Per Keyset', min_version='21.4')
    minimum_key_bit_strength = Attribute('Minimum Key Bit Strength', min_version='21.4')
    pbes2_algorithm = Attribute('PBES2 Algorithm', min_version='24.1')
    required_options = Attribute('Required Options', min_version='21.4')
    restricted_pbes2_algorithms = Attribute('Restricted PBES2 Algorithms', min_version='24.1')
    trust_id = Attribute('Trust Id', min_version='21.4')
