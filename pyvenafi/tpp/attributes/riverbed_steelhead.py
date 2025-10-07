from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class RiverbedSteelHeadAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Riverbed SteelHead"
    certificate_type = Attribute('Certificate Type', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    install_chain = Attribute('Install Chain', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    replace_existing = Attribute('Replace Existing', min_version='21.4')
