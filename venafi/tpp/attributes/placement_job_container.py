from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.organization import OrganizationAttributes


class PlacementJobContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Placement Job Container"
