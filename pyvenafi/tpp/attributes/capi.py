from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class CAPIAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "CAPI"
    binding_ip_address = Attribute('Binding IP Address', min_version='21.4')
    binding_port = Attribute('Binding Port', min_version='21.4')
    create_binding = Attribute('Create Binding', min_version='21.4')
    crypto_service_provider = Attribute('Crypto Service Provider', min_version='21.4')
    delete_previous_cert_and_key = Attribute('Delete Previous Cert And Key', min_version='23.3')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    friendly_name = Attribute('Friendly Name', min_version='21.4')
    hostname = Attribute('Hostname', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    non_exportable = Attribute('Non-Exportable', min_version='21.4')
    private_key_label = Attribute('Private Key Label', min_version='21.4')
    private_key_location = Attribute('Private Key Location', min_version='21.4')
    private_key_trustee = Attribute('Private Key Trustee', min_version='21.4')
    store_name = Attribute('Store Name', min_version='23.3')
    update_iis = Attribute('Update IIS', min_version='21.4')
    web_site_name = Attribute('Web Site Name', min_version='21.4')
