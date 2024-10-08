from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class ApertureConfigurationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Aperture Configuration"
    applies_to = Attribute('Applies To')
    feedback_url = Attribute('Feedback Url')
    help_text = Attribute('Help Text')
    help_url = Attribute('Help Url')
    lost_and_found = Attribute('Lost and Found')
    timeout = Attribute('Timeout')
