from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.service_module import ServiceModuleAttributes


class OnboardDiscoveryManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "Onboard Discovery Manager"
