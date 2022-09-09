from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class ClientGroupMonitorAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "ClientGroup Monitor"
