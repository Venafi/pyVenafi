from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes

class ReportTrustAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Trust"
    discoverydn = Attribute('DiscoveryDN', min_version='21.4')
    grouping = Attribute('Grouping', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
    trustedca = Attribute('TrustedCA', min_version='21.4')
    untrustedca = Attribute('UntrustedCA', min_version='21.4')
