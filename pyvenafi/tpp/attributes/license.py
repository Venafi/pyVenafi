from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LicenseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "License"
    license_key = Attribute('License Key')
