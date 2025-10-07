from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.cloud_instance_monitor_driver_base import CloudInstanceMonitorDriverBaseAttributes

class AWSEC2InstanceMonitorAttributes(CloudInstanceMonitorDriverBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "AWS EC2 Instance Monitor"
    access_key_credential_dn = Attribute('Access Key Credential DN', min_version='21.4')
    aws_credential_dn = Attribute('Aws Credential DN', min_version='21.4')
    secret_key_credential_dn = Attribute('Secret Key Credential DN', min_version='21.4')
