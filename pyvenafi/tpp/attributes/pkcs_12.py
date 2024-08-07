from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class PKCS12Attributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "PKCS#12"
    bundle_certificate = Attribute('Bundle Certificate', min_version='21.4')
    certificate_chain_file = Attribute('Certificate Chain File', min_version='21.4')
    certificate_file = Attribute('Certificate File', min_version='21.4')
    create_store = Attribute('Create Store', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    friendly_name = Attribute('Friendly Name', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    recycle_alias = Attribute('Recycle Alias', min_version='21.4')
    replace_store = Attribute('Replace Store', min_version='21.4')
