from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.ssh_key import SSHKeyAttributes
from pyvenafi.tpp.attributes.validation_base import ValidationBaseAttributes

class SSHServerKeyAttributes(SSHKeyAttributes, ValidationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "SSH Server Key"
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
