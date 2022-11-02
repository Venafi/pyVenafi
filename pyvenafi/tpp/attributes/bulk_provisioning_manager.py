from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class BulkProvisioningManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Bulk Provisioning Manager"
    retry_interval = Attribute('Retry Interval', min_version='18.3')
