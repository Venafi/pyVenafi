from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.discovery_statistics import DiscoveryStatisticsAttributes
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class DiscoveryManagerAttributes(DiscoveryStatisticsAttributes, ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Discovery Manager"
    connection_timeout = Attribute('Connection Timeout', min_version='21.4')
    delay = Attribute('Delay', min_version='21.4')
    load_percentage = Attribute('Load Percentage', min_version='21.4')
    max_work_units = Attribute('Max Work Units', min_version='21.4')
    maximum_threads = Attribute('Maximum Threads', min_version='21.4')
    minimum_threads = Attribute('Minimum Threads', min_version='21.4')
    placement_disabled = Attribute('Placement Disabled', min_version='21.4')
    timeout = Attribute('Timeout', min_version='21.4')
    window_days_of_week = Attribute('Window Days of Week', min_version='21.4')
    window_end = Attribute('Window End', min_version='21.4')
    window_start = Attribute('Window Start', min_version='21.4')
