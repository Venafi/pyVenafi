from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.organization import OrganizationAttributes


class CredentialContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
    __config_class__ = "Credential Container"
