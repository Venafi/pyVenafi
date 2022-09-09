from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class AutoLayoutManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Auto Layout Manager"
