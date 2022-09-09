from venafi.tpp.attributes._helper import IterableMeta, Attribute
from venafi.tpp.attributes.top import TopAttributes


class LayoutRuleBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Rule Base"
    rule = Attribute('Rule', min_version='19.1')
    vault_id = Attribute('Vault Id')
