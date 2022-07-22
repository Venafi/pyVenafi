from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Counter(PayloadModel):
    a_name: str = PayloadField(alias='AName', default=None)
    b_name: str = PayloadField(alias='BName', default=None)
    c_name: str = PayloadField(alias='CName', default=None)
    description: str = PayloadField(alias='Description', default=None)
    name: str = PayloadField(alias='Name', default=None)
    stats_type: int = PayloadField(alias='StatsType', default=None)


class Result(PayloadModel):
    key: 'Key' = PayloadField(alias='Key', default=None)
    value: 'List[Value]' = PayloadField(alias='Value', default=None)


class Key(PayloadModel):
    m_item1: str = PayloadField(alias='MItem1', default=None)
    m_item2: str = PayloadField(alias='MItem2', default=None)
    m_item3: str = PayloadField(alias='MItem3', default=None)


class Value(PayloadModel):
    count: int = PayloadField(alias='Count', default=None)
    sum_value: int = PayloadField(alias='SumValue', default=None)
    tag_a: str = PayloadField(alias='TagA', default=None)
    tag_b: str = PayloadField(alias='TagB', default=None)
    tag_c: str = PayloadField(alias='TagC', default=None)
    time_frame: datetime = PayloadField(alias='TimeFrame', default=None)
    type: int = PayloadField(alias='Type', default=None)
