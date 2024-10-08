from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class VAMnShieldAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "VAM nShield"
    file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
    install_path = Attribute('Install Path')
    km_local_path = Attribute('KM Local Path')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled')
    module_id = Attribute('Module Id')
