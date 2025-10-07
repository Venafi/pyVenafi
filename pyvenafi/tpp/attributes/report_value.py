from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportValueAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Value"
    options = Attribute('Options', min_version='22.3')
