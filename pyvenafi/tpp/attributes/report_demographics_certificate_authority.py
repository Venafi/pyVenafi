from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes

class ReportDemographicsCertificateAuthorityAttributes(
    ReportBaseAttributes,
    ReportFilterBaseAttributes,
    metaclass=IterableMeta
):
    __config_class__ = "Report:Demographics Certificate Authority"
