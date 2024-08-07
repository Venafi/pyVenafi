from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)

class SshDeviceBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Ssh Device Base"
    algorithm = Attribute('Algorithm', min_version='21.4')
    allow_duplicate_private_keys = Attribute('Allow Duplicate Private Keys', min_version='21.4')
    allow_from = Attribute('Allow From', min_version='21.4')
    allow_multiple_authorized_keys = Attribute('Allow Multiple Authorized Keys', min_version='21.4')
    allow_root_access = Attribute('Allow Root Access', min_version='21.4')
    allow_shared_server_accounts = Attribute('Allow Shared Server Accounts', min_version='21.4')
    allow_ssh1 = Attribute('Allow Ssh1', min_version='21.4')
    allow_unencrypted_private_keys = Attribute('Allow Unencrypted Private Keys', min_version='21.4')
    allowed_algorithm = Attribute('Allowed Algorithm', min_version='21.4')
    allowed_command = Attribute('Allowed Command', min_version='21.4')
    allowed_vendor_types = Attribute('Allowed Vendor Types', min_version='21.4')
    automatic_rotation_cleanup_wait = Attribute('Automatic Rotation Cleanup Wait', min_version='21.4')
    automatic_rotation_enabled = Attribute('Automatic Rotation Enabled', min_version='21.4')
    automatic_rotation_interval = Attribute('Automatic Rotation Interval', min_version='21.4')
    automatic_rotation_lead_time = Attribute('Automatic Rotation Lead Time', min_version='21.4')
    deny_from = Attribute('Deny From', min_version='21.4')
    environment = Attribute('Environment', min_version='21.4')
    host_trusts = Attribute('Host Trusts', min_version='21.4')
    key_bit_strength = Attribute('Key Bit Strength', min_version='21.4')
    known_hosts = Attribute('Known Hosts', min_version='21.4')
    management_type = Attribute('Management Type', min_version='21.4')
    maximum_key_age = Attribute('Maximum Key Age', min_version='21.4')
    minimum_key_bit_strength = Attribute('Minimum Key Bit Strength', min_version='21.4')
    required_options = Attribute('Required Options', min_version='21.4')
    root_server_access = Attribute('Root Server Access', min_version='21.4')
    server_access = Attribute('Server Access', min_version='21.4')
    ssh_device_status = Attribute('Ssh Device Status', min_version='21.4')
    ssh_device_type = Attribute('Ssh Device Type', min_version='21.4')
    trusted_root_users = Attribute('Trusted Root Users', min_version='21.4')
    trusted_users = Attribute('Trusted Users', min_version='21.4')
    update_cache = Attribute('Update Cache', min_version='21.4')
