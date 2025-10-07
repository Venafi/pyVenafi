from __future__ import annotations

from pyvenafi.tpp.attributes._helper import (
    Attribute,
    IterableMeta,
)
from pyvenafi.tpp.attributes.flow_action_base import FlowActionBaseAttributes

class FlowEventActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "Flow Event Action"
    condition = Attribute('Condition', min_version='21.4')
    data_content = Attribute('Data Content', min_version='21.4')
    event = Attribute('Event', min_version='21.4')
    severity = Attribute('Severity', min_version='21.4')
    text1_content = Attribute('Text1 Content', min_version='21.4')
    text2_content = Attribute('Text2 Content', min_version='21.4')
    value1_content = Attribute('Value1 Content', min_version='21.4')
    value2_content = Attribute('Value2 Content', min_version='21.4')
