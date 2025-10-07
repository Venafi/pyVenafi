from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class ConnectDirectAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "ConnectDirect"
    certificate_label = Attribute('Certificate Label', min_version='21.4')
    certificate_only = Attribute('Certificate Only', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    node_name = Attribute('Node Name', min_version='21.4')
    protocol = Attribute('Protocol', min_version='21.4')
