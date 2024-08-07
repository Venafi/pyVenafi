from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportSSHServerSummaryAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH Server Summary"
    options = Attribute('Options', min_version='21.4')
