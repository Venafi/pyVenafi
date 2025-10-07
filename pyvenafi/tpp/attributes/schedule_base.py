from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class ScheduleBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Schedule Base"
    blackout = Attribute('Blackout', min_version='21.4')
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    days_of_year = Attribute('Days Of Year', min_version='21.4')
    hour = Attribute('Hour', min_version='21.4')
    minute = Attribute('Minute', min_version='21.4')
    priority = Attribute('Priority', min_version='21.4')
    reschedule = Attribute('Reschedule', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
    stop_time = Attribute('Stop Time', min_version='21.4')
    timezone = Attribute('Timezone', min_version='21.4')
    utc = Attribute('UTC', min_version='21.4')
