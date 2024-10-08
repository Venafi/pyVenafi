from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.connection_base import ConnectionBaseAttributes
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes

class CertificateTrustStoreBaseAttributes(ConnectionBaseAttributes, DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Trust Store Base"
    approver = Attribute('Approver')
    automatic_provisioning_disabled = Attribute('Automatic Provisioning Disabled')
    bundle = Attribute('Bundle')
    bundle_installed = Attribute('Bundle Installed')
    in_error = Attribute('In Error')
    interval = Attribute('Interval')
    stage = Attribute('Stage')
    status = Attribute('Status')
