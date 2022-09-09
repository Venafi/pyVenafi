from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportAssessorAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Assessor"
    jobdn = Attribute('JobDN')
    options = Attribute('Options')
