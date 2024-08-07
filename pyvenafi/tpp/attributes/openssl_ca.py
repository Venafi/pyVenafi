from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes

class OpenSSLCAAttributes(CertificateAuthorityBaseAttributes, ConnectionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "OpenSSL CA"
    certificate_directory = Attribute('Certificate Directory', min_version='21.4')
    certificate_file = Attribute('Certificate File', min_version='21.4')
    configuration_file = Attribute('Configuration File', min_version='21.4')
    copy_extensions = Attribute('Copy Extensions', min_version='21.4')
    private_key_file = Attribute('Private Key File', min_version='21.4')
    private_key_password_credential = Attribute('Private Key Password Credential', min_version='21.4')
    temp_directory = Attribute('Temp Directory', min_version='21.4')
