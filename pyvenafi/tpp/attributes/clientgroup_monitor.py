from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class ClientGroupMonitorAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "ClientGroup Monitor"
