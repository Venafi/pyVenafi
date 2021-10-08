from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class LicenseAttributes(TopAttributes, metaclass=PropertyMeta):
	license_key = Attribute('License Key')
