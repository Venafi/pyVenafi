from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class JKSAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "JKS"
    backup_store = Attribute('Backup Store', min_version='24.1')
    certificate_label = Attribute('Certificate Label', min_version='21.4')
    create_store = Attribute('Create Store', min_version='21.4')
    disable_ssh_history = Attribute('Disable SSH History', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    java_vendor = Attribute('Java Vendor', min_version='21.4')
    key_algorithm = Attribute('Key Algorithm', min_version='21.4')
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled', min_version='21.4')
    keytool_path = Attribute('Keytool Path', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    private_key_location = Attribute('Private Key Location', min_version='21.4')
    protection_type = Attribute('Protection Type', min_version='21.4')
    recycle_alias = Attribute('Recycle Alias', min_version='21.4')
    replace_store = Attribute('Replace Store', min_version='21.4')
    slot_number = Attribute('Slot Number', min_version='21.4')
    softcard_identifier = Attribute('Softcard Identifier', min_version='21.4')
    store_type = Attribute('Store Type', min_version='21.4')
    temp_certificate_label = Attribute('Temp Certificate Label', min_version='21.4')
    use_external_process = Attribute('Use External Process', min_version='23.1')
    version = Attribute('Version', min_version='21.4')
