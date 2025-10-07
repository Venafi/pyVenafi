from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class BulkProvisioningManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Bulk Provisioning Manager"
    retry_interval = Attribute('Retry Interval', min_version='21.4')
