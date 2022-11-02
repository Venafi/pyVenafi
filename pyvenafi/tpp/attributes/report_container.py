from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class ReportContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Report Container"
