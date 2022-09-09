from __future__ import annotations
from venafi.tpp.api.api_base import ObjectModel, ApiField
from typing import List


class Column(ObjectModel):
    stored_name: str = ApiField(alias='storedName')
    nested_table: List[NestedTable] = ApiField(alias='nestedTable', default_factory=list)
    show_time: bool = ApiField(alias='showTime')
    show_date: bool = ApiField(alias='showDate')
    name: str = ApiField(alias='name')
    field: str = ApiField(alias='field')
    rank: int = ApiField(alias='rank')
    is_active: bool = ApiField(alias='isActive')
    can_sort: bool = ApiField(alias='canSort')
    can_be_deactivated: bool = ApiField(alias='canBeDeactivated')
    allows_rank_change: bool = ApiField(alias='allowsRankChange')
    column_width: int = ApiField(alias='columnWidth')
    type_id: str = ApiField(alias='typeId')


class NestedTable(ObjectModel):
    type: str = ApiField(alias='type')
    name: str = ApiField(alias='name')
    columns: List[Column] = ApiField(alias='columns', default_factory=list)


Column.update_forward_refs()
