from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataChoiceAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Choice"
    single = Attribute('Single')
