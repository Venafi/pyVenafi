from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes
from pyvenafi.tpp.attributes.device import DeviceAttributes


class CertificateTrustStoreBaseAttributes(DriverBaseAttributes, DeviceAttributes, metaclass=IterableMeta):
    __config_class__ = "Certificate Trust Store Base"
    approver = Attribute('Approver')
    automatic_provisioning_disabled = Attribute('Automatic Provisioning Disabled')
    bundle = Attribute('Bundle')
    bundle_installed = Attribute('Bundle Installed')
    in_error = Attribute('In Error')
    interval = Attribute('Interval')
    stage = Attribute('Stage')
    status = Attribute('Status')
