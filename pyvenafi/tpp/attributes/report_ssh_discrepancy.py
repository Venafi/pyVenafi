from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportSSHDiscrepancyAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH Discrepancy"
    options = Attribute('Options', min_version='21.4')
