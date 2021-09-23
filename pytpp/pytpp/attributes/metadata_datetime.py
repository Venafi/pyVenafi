from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.metadata_base import MetadataBaseAttributes


class MetadataDateTimeAttributes(MetadataBaseAttributes, metaclass=PropertyMeta):
	date_only = Attribute('Date Only')
