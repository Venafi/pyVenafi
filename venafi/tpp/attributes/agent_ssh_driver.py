from venafi.tpp.attributes._helper import IterableMeta
from venafi.tpp.attributes.agent_driver_base import AgentDriverBaseAttributes
from venafi.tpp.attributes.agent_ssh_base import AgentSSHBaseAttributes
from venafi.tpp.attributes.schedule_base import ScheduleBaseAttributes


class AgentSSHDriverAttributes(AgentDriverBaseAttributes, AgentSSHBaseAttributes, ScheduleBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Agent SSH Driver"
