from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class NetScalerAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "NetScaler"
    certificate_file = Attribute('Certificate File', min_version='21.4')
    chain_cert = Attribute('Chain Cert', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    fips_key = Attribute('Fips Key', min_version='21.4')
    import_only = Attribute('Import Only', min_version='21.4')
    install_path = Attribute('Install Path', min_version='21.4')
    issuer_certificate_name = Attribute('Issuer Certificate Name', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    partition = Attribute('Partition', min_version='22.2')
    private_key_file = Attribute('Private Key File', min_version='21.4')
    sni_certificate = Attribute('SNI Certificate', min_version='21.4')
    ssl_object_type = Attribute('SSL Object Type', min_version='21.4')
    temp_certificate_label = Attribute('Temp Certificate Label', min_version='21.4')
    virtual_server_name = Attribute('Virtual Server Name', min_version='21.4')
