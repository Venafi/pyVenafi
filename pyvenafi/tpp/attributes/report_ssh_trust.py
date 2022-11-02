from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportSSHTrustAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH Trust"
    options = Attribute('Options')
