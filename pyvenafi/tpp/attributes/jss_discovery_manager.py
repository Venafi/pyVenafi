from __future__ import annotations

from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.service_module import ServiceModuleAttributes

class JSSDiscoveryManagerAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
    __config_class__ = "JSS Discovery Manager"
