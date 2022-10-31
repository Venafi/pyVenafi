from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportValueAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Value"
    options = Attribute('Options', min_version='22.3')
