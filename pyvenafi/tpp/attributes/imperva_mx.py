from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class ImpervaMXAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Imperva MX"
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled', min_version='21.4')
    private_key_name = Attribute('Private Key Name', min_version='21.4')
    server_group = Attribute('Server Group', min_version='21.4')
    service = Attribute('Service', min_version='21.4')
    site = Attribute('Site', min_version='21.4')
    username_credential = Attribute('Username Credential', min_version='21.4')
    utility_path = Attribute('Utility Path', min_version='21.4')
