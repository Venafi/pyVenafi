from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    IterableMeta,
    Attribute,
)
from pyvenafi.tpp.attributes.metadata_base import MetadataBaseAttributes

class MetadataListAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata List"
    single = Attribute('Single', min_version='21.4')
