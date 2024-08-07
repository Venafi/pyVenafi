from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class DataPowerAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "DataPower"
    application_domain = Attribute('Application Domain', min_version='21.4')
    associate_to_cp = Attribute('Associate To CP', min_version='21.4')
    certificate_name = Attribute('Certificate Name', min_version='21.4')
    certificate_only = Attribute('Certificate Only', min_version='21.4')
    chain_cert = Attribute('Chain Cert', min_version='21.4')
    create_cp = Attribute('Create CP', min_version='21.4')
    create_ic = Attribute('Create IC', min_version='21.4')
    create_vc = Attribute('Create VC', min_version='21.4')
    credential_type = Attribute('Credential Type', min_version='21.4')
    crypto_profile = Attribute('Crypto Profile', min_version='21.4')
    ftp_credential = Attribute('FTP Credential', min_version='21.4')
    ftp_host = Attribute('FTP Host', min_version='21.4')
    ftp_path = Attribute('FTP Path', min_version='21.4')
    ftp_port = Attribute('FTP Port', min_version='21.4')
    file_validation_disabled = Attribute('File Validation Disabled', min_version='21.4')
    fips_key = Attribute('Fips Key', min_version='21.4')
    folder = Attribute('Folder', min_version='21.4')
    max_filesize = Attribute('Max Filesize', min_version='21.4')
    network_validation_disabled = Attribute('Network Validation Disabled', min_version='21.4')
    password_alias = Attribute('Password Alias', min_version='24.1')
    private_key_name = Attribute('Private Key Name', min_version='21.4')
    ssh_prompt = Attribute('SSH Prompt', min_version='21.4')
    ssl_profile_type = Attribute('SSL Profile Type', min_version='21.4')
    ssl_proxy_profile = Attribute('SSL Proxy Profile', min_version='21.4')
    temp_certificate_label = Attribute('Temp Certificate Label', min_version='21.4')
    use_basic_provisioning = Attribute('Use Basic Provisioning', min_version='21.4')
    xml_port = Attribute('XML Port', min_version='21.4')
