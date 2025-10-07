from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class AzureKeyVaultAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Azure Key Vault"
    app_service_subscription_id = Attribute('App Service Subscription ID', min_version='22.1')
    binding_hostnames = Attribute('Binding Hostnames', min_version='21.4')
    binding_ssl_type = Attribute('Binding SSL Type', min_version='21.4')
    certificate_credential = Attribute('Certificate Credential', min_version='21.4')
    certificate_name = Attribute('Certificate Name', min_version='21.4')
    client_id = Attribute('Client ID', min_version='21.4')
    create_binding = Attribute('Create Binding', min_version='21.4')
    create_san_dns_bindings = Attribute('Create SAN DNS Bindings', min_version='21.4')
    environment = Attribute('Environment', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    non_exportable = Attribute('Non-Exportable', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    update_web_app = Attribute('Update Web App', min_version='21.4')
    vault_name = Attribute('Vault Name', min_version='21.4')
    web_app_name = Attribute('Web App Name', min_version='21.4')
