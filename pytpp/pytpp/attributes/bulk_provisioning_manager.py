from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class BulkProvisioningManagerAttributes(ServiceModuleAttributes, metaclass=PropertyMeta):
	retry_interval = Attribute('Retry Interval', min_version='18.3')
