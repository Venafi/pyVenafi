from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportLicensingAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Licensing"
    contract_renewal_date = Attribute('Contract Renewal Date', min_version='23.3')
    long_lived_certs_minimum_validity_period = Attribute('Long Lived Certs Minimum Validity Period', min_version='23.3')
    options = Attribute('Options', min_version='21.4')
