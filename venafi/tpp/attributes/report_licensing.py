from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportLicensingAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Licensing"
    options = Attribute('Options')
