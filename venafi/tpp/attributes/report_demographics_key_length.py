from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.report_base import ReportBaseAttributes
from venafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportDemographicsKeyLengthAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Demographics Key Length"
