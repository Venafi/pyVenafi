from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class TealeafSunimpAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "TealeafSunimp"
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    key_store_name = Attribute('Key Store Name', min_version='21.4')
    key_store_validation_disabled = Attribute('Key Store Validation Disabled', min_version='21.4')
    sunimp_utility_path = Attribute('Sunimp Utility Path', min_version='21.4')
    tealeaf_utility_path = Attribute('Tealeaf Utility Path', min_version='21.4')
