from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class EngineUpgradeAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Engine Upgrade"
    engine_id = Attribute('Engine Id', min_version='20.1')
    start_time = Attribute('Start Time', min_version='20.1')
    stop_time = Attribute('Stop Time', min_version='20.1')
    warning_count = Attribute('Warning Count', min_version='20.1')
