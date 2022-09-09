from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from venafi.tpp.attributes.top import TopAttributes


class CodeSigningKeyTimeConstraintAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Key Time Constraint"
