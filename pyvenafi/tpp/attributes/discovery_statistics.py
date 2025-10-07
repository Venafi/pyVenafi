from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class DiscoveryStatisticsAttributes(metaclass=IterableMeta):
    __config_class__ = "Discovery Statistics"
    certificates_found = Attribute('Certificates Found', min_version='21.4')
    completed_scans = Attribute('Completed Scans', min_version='21.4')
    connect_succeeded = Attribute('Connect Succeeded', min_version='21.4')
    keys_found = Attribute('Keys Found', min_version='21.4')
