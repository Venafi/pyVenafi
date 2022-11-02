from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.report_base import ReportBaseAttributes


class ReportSSHUserKeyAttributes(ReportBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Report:SSH User Key"
    options = Attribute('Options')
