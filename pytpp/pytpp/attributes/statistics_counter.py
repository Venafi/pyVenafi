from pytpp.attributes._helper import PropertyMeta, Attribute
from pytpp.attributes.top import TopAttributes


class StatisticsCounterAttributes(TopAttributes, metaclass=PropertyMeta):
	sensitive = Attribute('Sensitive', min_version='19.3')
	statistic_id = Attribute('Statistic Id', min_version='19.3')
	tag_a_name = Attribute('Tag A Name', min_version='19.3')
	tag_b_name = Attribute('Tag B Name', min_version='19.3')
	tag_c_name = Attribute('Tag C Name', min_version='19.3')
	value_description = Attribute('Value Description', min_version='19.3')
