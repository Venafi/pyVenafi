from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningApplicationAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Application"
    application_hash = Attribute('Application Hash')
    application_location = Attribute('Application Location')
    application_signatory_issuer = Attribute('Application Signatory Issuer')
    application_signatory_subject = Attribute('Application Signatory Subject')
    application_size = Attribute('Application Size')
    application_version = Attribute('Application Version')
    permitted_argument_pattern = Attribute('Permitted Argument Pattern')
    regular_expression = Attribute('Regular Expression')
    signing_object_file_argument_pattern = Attribute('Signing Object File Argument Pattern')
