from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportLicensingAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Licensing"
    options = Attribute('Options')
