from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class F5AuthenticationBundleAttributes(TopAttributes, metaclass=PropertyMeta):
	advanced_settings_bundle_name = Attribute('Advanced Settings Bundle Name')
	certificates = Attribute('Certificates')
