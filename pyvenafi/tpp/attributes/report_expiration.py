from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportExpirationAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Expiration"
    options = Attribute('Options')
