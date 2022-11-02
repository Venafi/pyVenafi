from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class OpenSSLCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "OpenSSL CA"
    certificate_directory = Attribute('Certificate Directory')
    certificate_file = Attribute('Certificate File')
    configuration_file = Attribute('Configuration File')
    copy_extensions = Attribute('Copy Extensions')
    private_key_file = Attribute('Private Key File')
    private_key_password_credential = Attribute('Private Key Password Credential')
    temp_directory = Attribute('Temp Directory')
