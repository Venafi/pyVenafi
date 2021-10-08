from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.service_module import ServiceModuleAttributes


class KmipServiceModuleAttributes(ServiceModuleAttributes, metaclass=PropertyMeta):
	agent_module_handlers = Attribute('Agent Module Handlers')
	agent_upgrade_rule = Attribute('Agent Upgrade Rule')
	credential = Attribute('Credential')
	interval = Attribute('Interval')
	port = Attribute('Port')
	start_time = Attribute('Start Time')
	upgrade = Attribute('Upgrade')
	version = Attribute('Version')
