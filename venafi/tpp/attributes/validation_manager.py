from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class ValidationManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Validation Manager"
    start_time = Attribute('Start Time')
