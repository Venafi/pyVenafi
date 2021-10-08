from pytpp.attributes._helper import PropertyMeta
from pytpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from pytpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentDriverAttributes(AgentDriverBaseAttributes, ScheduleBaseAttributes, metaclass=PropertyMeta):
	pass