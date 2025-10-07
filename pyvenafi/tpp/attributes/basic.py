from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class BasicAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Basic"
    certificate_file = Attribute('Certificate File', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
