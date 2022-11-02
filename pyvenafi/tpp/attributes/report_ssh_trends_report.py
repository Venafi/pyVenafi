from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportSshTrendsReportAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Ssh Trends Report"
