from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes
from pyvenafi.tpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ServerCertificateWorkAttributes(ApplicationBaseAttributes, ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Server Certificate Work"
    application_attribute = Attribute('Application Attribute')
    application_type = Attribute('Application Type')
    certificate_container = Attribute('Certificate Container')
    friendly_name = Attribute('Friendly Name')
    interval = Attribute('Interval')
    log_threshold = Attribute('Log Threshold')
    naming_pattern = Attribute('Naming Pattern')
    nix_key_store = Attribute('Nix Key Store')
    nix_private_key = Attribute('Nix Private Key')
    path_type = Attribute('Path Type')
    private_key_trustee = Attribute('Private Key Trustee')
    win_key_store = Attribute('Win Key Store')
    win_private_key = Attribute('Win Private Key')
