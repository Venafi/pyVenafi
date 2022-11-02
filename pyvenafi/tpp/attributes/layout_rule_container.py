from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.organization import OrganizationAttributes


class LayoutRuleContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Rule Container"
