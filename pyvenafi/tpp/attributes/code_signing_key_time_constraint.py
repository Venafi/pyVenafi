from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.top import TopAttributes


class CodeSigningKeyTimeConstraintAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Key Time Constraint"
