from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes
from pyvenafi.tpp.attributes.report_filter_base import ReportFilterBaseAttributes


class ReportTrustAttributes(ReportBaseAttributes, ReportFilterBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:Trust"
    discoverydn = Attribute('DiscoveryDN')
    grouping = Attribute('Grouping')
    options = Attribute('Options')
    trustedca = Attribute('TrustedCA')
    untrustedca = Attribute('UntrustedCA')
