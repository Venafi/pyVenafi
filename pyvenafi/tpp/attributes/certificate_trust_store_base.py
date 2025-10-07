from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes

class CertificateTrustStoreBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Trust Store Base"
    approver = Attribute('Approver', min_version='21.4')
    automatic_provisioning_disabled = Attribute('Automatic Provisioning Disabled', min_version='21.4')
    bundle = Attribute('Bundle', min_version='21.4')
    bundle_installed = Attribute('Bundle Installed', min_version='21.4')
    in_error = Attribute('In Error', min_version='21.4')
    interval = Attribute('Interval', min_version='21.4')
    stage = Attribute('Stage', min_version='21.4')
    status = Attribute('Status', min_version='21.4')
