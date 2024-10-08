from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.exclusion import ExclusionAttributes

class DiscoveryExclusionAttributes(ExclusionAttributes, metaclass=IterableMeta):
    __config_class__ = "Discovery Exclusion"
    address_range = Attribute('Address Range')
    managed_by_discovery_dn = Attribute('Managed By Discovery DN')
    managed_dn = Attribute('Managed DN')
    port_range = Attribute('Port Range')
