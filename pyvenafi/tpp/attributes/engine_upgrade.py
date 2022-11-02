from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class EngineUpgradeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Engine Upgrade"
    engine_id = Attribute('Engine Id')
    start_time = Attribute('Start Time')
    stop_time = Attribute('Stop Time')
    warning_count = Attribute('Warning Count')
