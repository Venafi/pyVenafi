from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportSSHKeyExpirationAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH Key Expiration"
    options = Attribute('Options')
