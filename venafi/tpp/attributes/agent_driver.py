from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from venafi.tpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentDriverAttributes(AgentDriverBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent Driver"
