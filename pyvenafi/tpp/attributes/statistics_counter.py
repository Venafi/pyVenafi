from pyvenafi.tpp.attributes._helper import IterableMeta, Attribute
from pyvenafi.tpp.attributes.top import TopAttributes


class StatisticsCounterAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "Statistics Counter"
    sensitive = Attribute('Sensitive')
    statistic_id = Attribute('Statistic Id')
    tag_a_name = Attribute('Tag A Name')
    tag_b_name = Attribute('Tag B Name')
    tag_c_name = Attribute('Tag C Name')
    value_description = Attribute('Value Description')
