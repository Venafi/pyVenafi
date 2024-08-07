from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class BlueCoatSSLVAAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "BlueCoat SSLVA"
    certificate_label = Attribute('Certificate Label', min_version='21.4')
    certificate_oid = Attribute('Certificate OID', min_version='21.4')
    certificate_only = Attribute('Certificate Only', min_version='21.4')
    create_lists = Attribute('Create Lists', min_version='21.4')
    device_certificate = Attribute('Device Certificate', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    replace_store = Attribute('Replace Store', min_version='21.4')
