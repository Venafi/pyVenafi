from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes

class ReportEntitlementAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Entitlement"
    options = Attribute('Options', min_version='21.4')
    policydn = Attribute('PolicyDN', min_version='21.4')
