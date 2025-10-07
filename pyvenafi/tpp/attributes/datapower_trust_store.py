from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.certificate_trust_store_base import CertificateTrustStoreBaseAttributes

class DataPowerTrustStoreAttributes(CertificateTrustStoreBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "DataPower Trust Store"
    application_domain = Attribute('Application Domain', min_version='21.4')
    crl_distribution_points_handling = Attribute('CRL Distribution Points Handling', min_version='21.4')
    certificate_validation_mode = Attribute('Certificate Validation Mode', min_version='21.4')
    check_dates = Attribute('Check Dates', min_version='21.4')
    crypto_validation_credential_name = Attribute('Crypto Validation Credential Name', min_version='21.4')
    folder = Attribute('Folder', min_version='21.4')
    maximum_length = Attribute('Maximum Length', min_version='21.4')
    require_crl = Attribute('Require CRL', min_version='21.4')
    use_crl = Attribute('Use CRL', min_version='21.4')
