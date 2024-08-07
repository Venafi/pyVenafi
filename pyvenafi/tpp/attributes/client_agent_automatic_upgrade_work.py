from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class ClientAgentAutomaticUpgradeWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Agent Automatic Upgrade Work"
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    force_agent_upgrade = Attribute('Force Agent Upgrade', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    schedule_type = Attribute('Schedule Type', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
