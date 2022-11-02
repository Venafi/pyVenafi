from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.driver_base import DriverBaseAttributes


class CloudInstanceMonitorDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Cloud Instance Monitor Driver Base"
    certificate_cleanup_options = Attribute('Certificate Cleanup Options')
    certificate_relocation_policy_dn = Attribute('Certificate Relocation Policy DN')
    cleanup_after = Attribute('Cleanup After')
    cloud_region = Attribute('Cloud Region')
    last_run = Attribute('Last Run')
    policydn = Attribute('PolicyDN')
