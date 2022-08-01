from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Counter(PayloadModel):
    a_name: str = PayloadField(alias='AName')
    b_name: str = PayloadField(alias='BName')
    c_name: str = PayloadField(alias='CName')
    description: str = PayloadField(alias='Description')
    name: str = PayloadField(alias='Name')
    stats_type: int = PayloadField(alias='StatsType')


class Result(PayloadModel):
    key: 'Key' = PayloadField(alias='Key')
    value: 'List[Value]' = PayloadField(alias='Value')


class Key(PayloadModel):
    m_item1: str = PayloadField(alias='MItem1')
    m_item2: str = PayloadField(alias='MItem2')
    m_item3: str = PayloadField(alias='MItem3')


class Value(PayloadModel):
    count: int = PayloadField(alias='Count')
    sum_value: int = PayloadField(alias='SumValue')
    tag_a: str = PayloadField(alias='TagA')
    tag_b: str = PayloadField(alias='TagB')
    tag_c: str = PayloadField(alias='TagC')
    time_frame: datetime = PayloadField(alias='TimeFrame')
    type: int = PayloadField(alias='Type')
