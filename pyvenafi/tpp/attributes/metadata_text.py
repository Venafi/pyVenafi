from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.metadata_base import MetadataBaseAttributes

class MetadataTextAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Text"
    allowed_characters = Attribute('Allowed Characters', min_version='21.4')
    error_message = Attribute('Error Message', min_version='21.4')
    mask = Attribute('Mask', min_version='21.4')
    maximum_length = Attribute('Maximum Length', min_version='21.4')
    minimum_length = Attribute('Minimum Length', min_version='21.4')
    regular_expression = Attribute('Regular Expression', min_version='21.4')
