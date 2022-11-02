from pyvenafi.tpp.attributes._helper import IterableMeta
from pyvenafi.tpp.attributes.schedule_base import ScheduleBaseAttributes
from pyvenafi.tpp.attributes.code_signing_time_constraint_root import CodeSigningTimeConstraintRootAttributes


class CodeSigningKeyTimeConstraintAttributes(ScheduleBaseAttributes, CodeSigningTimeConstraintRootAttributes, metaclass=IterableMeta):
    __config_class__ = "Code Signing Key Time Constraint"
