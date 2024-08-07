from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes

class RSAKeonCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "RSA Keon CA"
    ca_md5 = Attribute('CA MD5', min_version='21.4')
    ca_name = Attribute('CA Name', min_version='21.4')
    certificate_block = Attribute('Certificate Block', min_version='21.4')
    jurisdiction_id = Attribute('Jurisdiction ID', min_version='21.4')
    jurisdiction_name = Attribute('Jurisdiction Name', min_version='21.4')
    supported_validity_periods = Attribute('Supported Validity Periods', min_version='21.4')
