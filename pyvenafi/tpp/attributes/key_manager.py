from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class KeyManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Key Manager"
