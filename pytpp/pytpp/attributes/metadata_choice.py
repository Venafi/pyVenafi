from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataChoiceAttributes(MetadataBaseAttributes, metaclass=PropertyMeta):
	single = Attribute('Single')
