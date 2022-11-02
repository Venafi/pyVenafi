from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class KmipServiceModuleAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Kmip Service Module"
    agent_module_handlers = Attribute('Agent Module Handlers')
    agent_upgrade_rule = Attribute('Agent Upgrade Rule')
    credential = Attribute('Credential')
    interval = Attribute('Interval')
    port = Attribute('Port')
    start_time = Attribute('Start Time')
    upgrade = Attribute('Upgrade')
    version = Attribute('Version')
