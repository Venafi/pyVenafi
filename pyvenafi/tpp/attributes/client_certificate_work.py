from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes
from pyvenafi.tpp.attributes.x509_certificate_base import X509CertificateBaseAttributes

class ClientCertificateWorkAttributes(ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Certificate Work"
    certificate_container = Attribute('Certificate Container')
    naming_pattern = Attribute('Naming Pattern')
    pkix_parameter_set = Attribute('PKIX Parameter Set')
    transfer_allowed = Attribute('Transfer Allowed')
