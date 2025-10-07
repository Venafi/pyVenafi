from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class iPlanetAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "iPlanet"
    alias = Attribute('Alias', min_version='21.4')
    certutil_path = Attribute('Certutil Path', min_version='21.4')
    create_store = Attribute('Create Store', min_version='21.4')
    create_virtual_server = Attribute('Create Virtual Server', min_version='21.4')
    database_credential = Attribute('Database Credential', min_version='21.4')
    database_prefix = Attribute('Database Prefix', min_version='21.4')
    database_type = Attribute('Database Type', min_version='21.4')
    database_validation_disabled = Attribute('Database Validation Disabled', min_version='21.4')
    document_root = Attribute('Document Root', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    install_path = Attribute('Install Path', min_version='21.4')
    key_store = Attribute('Key Store', min_version='21.4')
    key_store_credential = Attribute('Key Store Credential', min_version='21.4')
    mta_host = Attribute('MTA Host', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    pk12util_path = Attribute('Pk12util Path', min_version='21.4')
    protocol = Attribute('Protocol', min_version='21.4')
    replace_store = Attribute('Replace Store', min_version='21.4')
    secure_server_name = Attribute('Secure Server Name', min_version='21.4')
    use_proxy = Attribute('Use Proxy', min_version='21.4')
    virtual_server_dns_value = Attribute('Virtual Server DNS Value', min_version='21.4')
    virtual_server_port = Attribute('Virtual Server Port', min_version='21.4')
    virtual_server_user = Attribute('Virtual Server User', min_version='21.4')
    web_credential = Attribute('Web Credential', min_version='21.4')
    web_port = Attribute('Web Port', min_version='21.4')
