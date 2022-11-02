from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportAnalyticsAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Analytics"
    options = Attribute('Options', min_version='17.1')
