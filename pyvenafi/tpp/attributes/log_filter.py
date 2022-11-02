from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.log_channel import LogChannelAttributes


class LogFilterAttributes(LogChannelAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Filter"
    filter_ids = Attribute('Filter IDs')
    filter_severity = Attribute('Filter Severity')
    log_channel = Attribute('Log Channel')
