from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes
from venafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportSSHAuthorizedUserAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH Authorized User"
    options = Attribute('Options')
