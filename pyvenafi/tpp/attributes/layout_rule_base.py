from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class LayoutRuleBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Rule Base"
    rule = Attribute('Rule')
    vault_id = Attribute('Vault Id')
