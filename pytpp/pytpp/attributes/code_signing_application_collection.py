from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CodeSigningApplicationCollectionAttributes(TopAttributes, metaclass=PropertyMeta):
	code_signing_application_dn = Attribute('Code Signing Application DN', min_version='19.2')
