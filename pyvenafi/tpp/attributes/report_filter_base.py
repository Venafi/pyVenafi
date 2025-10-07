from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)

class ReportFilterBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "Report Filter Base"
    address = Attribute('Address', min_version='21.4')
    discoverydn = Attribute('DiscoveryDN', min_version='21.4')
    grouping = Attribute('Grouping', min_version='21.4')
    longrunning = Attribute('LongRunning', min_version='21.4')
    policydn = Attribute('PolicyDN', min_version='21.4')
    reporton = Attribute('ReportOn', min_version='21.4')
    selectedcontacts = Attribute('SelectedContacts', min_version='21.4')
