from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes


class CodeSignManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Sign Manager"
