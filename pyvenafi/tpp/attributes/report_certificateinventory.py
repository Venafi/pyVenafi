from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportCertificateInventoryAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:CertificateInventory"
    grouping = Attribute('Grouping')
    options = Attribute('Options')
    policydn = Attribute('PolicyDN')
