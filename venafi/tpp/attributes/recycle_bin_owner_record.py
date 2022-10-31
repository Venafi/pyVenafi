from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.top import TopAttributes


class RecycleBinOwnerRecordAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Recycle Bin Owner Record"
