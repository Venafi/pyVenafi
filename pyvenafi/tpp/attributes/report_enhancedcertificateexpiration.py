from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportEnhancedCertificateExpirationAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:EnhancedCertificateExpiration"
    debug_file = Attribute('Debug File', min_version='21.4')
    grouping = Attribute('Grouping', min_version='21.4')
    options = Attribute('Options', min_version='21.4')
