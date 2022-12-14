from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LogApplicationCustomizationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Application Customization"
    customization_data = Attribute('Customization Data')
    language = Attribute('Language')
