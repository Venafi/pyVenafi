from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class MetadataCategoryAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Category"
    label_text = Attribute('Label Text')
    localization = Attribute('Localization')
