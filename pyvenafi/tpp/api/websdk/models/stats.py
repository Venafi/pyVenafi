from __future__ import annotations

from datetime import datetime

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)

class Counter(ObjectModel):
    a_name: str = ApiField(alias='AName')
    b_name: str = ApiField(alias='BName')
    c_name: str = ApiField(alias='CName')
    description: str = ApiField(alias='Description')
    disabled: bool = ApiField(alias='Disabled')
    error: str = ApiField(alias='Error')
    ignore_count: bool = ApiField(alias='IgnoreCount')
    name: str = ApiField(alias='Name')
    sensitive: bool = ApiField(alias='Sensitive')
    stats_type: int = ApiField(alias='StatsType')
    value_description: str = ApiField(alias='ValueDescription')

class Key(ObjectModel):
    m_item1: str = ApiField(alias='MItem1')
    m_item2: str = ApiField(alias='MItem2')
    m_item3: str = ApiField(alias='MItem3')

class Value(ObjectModel):
    count: int = ApiField(alias='Count')
    sum_value: int = ApiField(alias='SumValue')
    tag_a: str = ApiField(alias='TagA')
    tag_b: str = ApiField(alias='TagB')
    tag_c: str = ApiField(alias='TagC')
    time_frame: datetime = ApiField(alias='TimeFrame')
    type: int = ApiField(alias='Type')

class Result(ObjectModel):
    key: Key = ApiField(alias='Key')
    value: list[Value] = ApiField(alias='Value', default_factory=list)

class CounterContainer(ObjectModel):
    name: str = ApiField(alias='Name')
    stats_code: int = ApiField(alias='StatsCode')
