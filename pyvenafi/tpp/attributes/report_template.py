from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class ReportTemplateAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Report Template"
    item_vault_id = Attribute('Item Vault Id')
    report_class = Attribute('Report Class')
    template_vault_id = Attribute('Template Vault Id')
