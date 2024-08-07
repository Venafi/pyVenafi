from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportHistoricalCertificatesAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:HistoricalCertificates"
    options = Attribute('Options', min_version='23.3')
    policydn = Attribute('PolicyDN', min_version='23.3')
