from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class RecycleBinOwnerRecordAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Recycle Bin Owner Record"
