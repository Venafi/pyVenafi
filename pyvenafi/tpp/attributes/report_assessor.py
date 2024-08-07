from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportAssessorAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Assessor"
    jobdn = Attribute('JobDN')
    options = Attribute('Options')
