from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class MetadataBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Metadata Base"
    allowed_values = Attribute('Allowed Values')
    associated_classes = Attribute('Associated Classes')
    category = Attribute('Category')
    default_values = Attribute('Default Values')
    help_text = Attribute('Help Text')
    label_text = Attribute('Label Text')
    localization = Attribute('Localization')
    mandatory = Attribute('Mandatory')
    not_before = Attribute('Not Before')
    policyable = Attribute('Policyable')
    render_hidden = Attribute('Render Hidden')
    render_read_only = Attribute('Render Read Only')
