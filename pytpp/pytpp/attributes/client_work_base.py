from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ClientWorkBaseAttributes(TopAttributes, metaclass=PropertyMeta):
	work_guid = Attribute('Work Guid')
