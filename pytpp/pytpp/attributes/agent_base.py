from pytpp.attributes._helper import PropertyMeta, Attribute


class AgentBaseAttributes(metaclass=PropertyMeta):
	agent_guid = Attribute('Agent GUID')
	location = Attribute('Location')
