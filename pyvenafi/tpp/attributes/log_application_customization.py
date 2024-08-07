from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class LogApplicationCustomizationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Application Customization"
    customization_data = Attribute('Customization Data', min_version='21.4')
    language = Attribute('Language', min_version='21.4')
