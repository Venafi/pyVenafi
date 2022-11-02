from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.top import TopAttributes


class WorkflowContainerAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Workflow Container"
