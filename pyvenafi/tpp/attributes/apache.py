from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class ApacheAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Apache"
    application_id = Attribute('Application ID', min_version='21.4')
    certificate_chain_file = Attribute('Certificate Chain File', min_version='21.4')
    certificate_file = Attribute('Certificate File', min_version='21.4')
    client_tools_path = Attribute('Client Tools Path', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    kmdata_key_file = Attribute('KMDATA Key File', min_version='22.2')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    ocs_identifier = Attribute('OCS Identifier', min_version='21.4')
    overwrite_existing_chain = Attribute('Overwrite Existing Chain', min_version='21.4')
    pbes2_algorithm = Attribute('PBES2 Algorithm', min_version='21.4')
    partition_password_credential = Attribute('Partition Password Credential', min_version='21.4')
    private_key_file = Attribute('Private Key File', min_version='21.4')
    private_key_label = Attribute('Private Key Label', min_version='21.4')
    private_key_location = Attribute('Private Key Location', min_version='21.4')
    protection_type = Attribute('Protection Type', min_version='21.4')
    slot_number = Attribute('Slot Number', min_version='21.4')
    softcard_identifier = Attribute('Softcard Identifier', min_version='21.4')
