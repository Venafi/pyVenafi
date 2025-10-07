from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes

class ReportCertificateNetworkValidationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:CertificateNetworkValidation"
    certificateslimit = Attribute('CertificatesLimit', min_version='21.4')
    grouping = Attribute('Grouping', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
    policydn = Attribute('PolicyDN', min_version='21.4')
