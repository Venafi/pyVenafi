from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.metadata_base import MetadataBaseAttributes

class MetadataDateTimeAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata DateTime"
    date_only = Attribute('Date Only', min_version='21.4')
