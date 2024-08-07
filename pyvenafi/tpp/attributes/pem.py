from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class PEMAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "PEM"
    certificate_chain_file = Attribute('Certificate Chain File', min_version='21.4')
    certificate_file = Attribute('Certificate File', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    overwrite_existing_chain = Attribute('Overwrite Existing Chain', min_version='21.4')
    pbes2_algorithm = Attribute('PBES2 Algorithm', min_version='21.4')
    private_key_file = Attribute('Private Key File', min_version='21.4')
    private_key_syntax = Attribute('Private Key Syntax')
