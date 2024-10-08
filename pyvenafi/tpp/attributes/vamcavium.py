from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.application_base import ApplicationBaseAttributes

class VamCaviumAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "VamCavium"
    cavium_utility_path = Attribute('Cavium Utility Path')
    key_list_path = Attribute('Key List Path')
