from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataChoiceAttributes(MetadataBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Choice"
    single = Attribute('Single')
