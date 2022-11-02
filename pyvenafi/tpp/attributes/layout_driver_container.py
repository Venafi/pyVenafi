from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.organization import OrganizationAttributes


class LayoutDriverContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Layout Driver Container"
