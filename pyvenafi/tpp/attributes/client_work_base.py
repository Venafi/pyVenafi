from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class ClientWorkBaseAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Client Work Base"
    work_guid = Attribute('Work Guid')
