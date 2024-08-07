from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class GSKAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "GSK"
    backup_store = Attribute('Backup Store', min_version='21.4')
    certificate_label = Attribute('Certificate Label', min_version='21.4')
    create_store = Attribute('Create Store', min_version='21.4')
    default_cert = Attribute('Default Cert', min_version='21.4')
    disable_ssh_history = Attribute('Disable SSH History', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    fips_key = Attribute('Fips Key', min_version='21.4')
    hide_command_line_passwords = Attribute('Hide Command Line Passwords', min_version='21.4')
    java_home_path = Attribute('Java Home Path', min_version='21.4')
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    password_expire_days = Attribute('Password Expire Days', min_version='21.4')
    recycle_alias = Attribute('Recycle Alias', min_version='21.4')
    refresh_security = Attribute('Refresh Security', min_version='21.4')
    replace_store = Attribute('Replace Store', min_version='21.4')
    stash_password = Attribute('Stash Password', min_version='21.4')
    store_type = Attribute('Store Type', min_version='21.4')
    temp_certificate_label = Attribute('Temp Certificate Label', min_version='21.4')
    utility_path = Attribute('Utility Path', min_version='21.4')
    version = Attribute('Version', min_version='21.4')
