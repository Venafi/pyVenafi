from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.top import TopAttributes

class LogChannelContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Log Channel Container"
    description = Attribute('Description')
    factory_item_vault_id = Attribute('Factory Item Vault Id')
    factory_vault_id = Attribute('Factory Vault Id')
    item_vault_id = Attribute('Item Vault Id')
    template = Attribute('Template')
    template_vault_id = Attribute('Template Vault Id')
