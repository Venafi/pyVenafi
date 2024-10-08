from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_group import ApplicationGroupAttributes

class ApacheApplicationGroupAttributes(ApplicationGroupAttributes, metaclass=IterableMeta):
    __config_class__ = "Apache Application Group"
    client_tools_path = Attribute('Client Tools Path', min_version='21.4')
    kmdata_key_file = Attribute('KMDATA Key File', min_version='22.2')
    ocs_identifier = Attribute('OCS Identifier', min_version='21.4')
    partition_password_credential = Attribute('Partition Password Credential', min_version='21.4')
    private_key_label = Attribute('Private Key Label', min_version='21.4')
    private_key_location = Attribute('Private Key Location', min_version='21.4')
    protection_type = Attribute('Protection Type', min_version='21.4')
    softcard_identifier = Attribute('Softcard Identifier', min_version='21.4')
