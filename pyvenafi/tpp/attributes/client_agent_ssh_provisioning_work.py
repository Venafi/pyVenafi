from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.client_work_base import ClientWorkBaseAttributes

class ClientAgentSSHProvisioningWorkAttributes(ClientWorkBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Agent SSH Provisioning Work"
    days_of_month = Attribute('Days Of Month', min_version='21.4')
    days_of_week = Attribute('Days Of Week', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    log_threshold = Attribute('Log Threshold', min_version='21.4')
    schedule_type = Attribute('Schedule Type', min_version='21.4')
    start_time = Attribute('Start Time', min_version='21.4')
