from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class CodeSigningKeyTimeConstraintAttributes(TopAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Key Time Constraint"
