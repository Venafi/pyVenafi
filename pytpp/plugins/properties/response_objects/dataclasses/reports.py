from dataclasses import dataclass
from typing import List


@dataclass
class Column:
    stored_name : str
    nested_table : 'List[NestedTable]'
    show_time : bool
    show_date : bool
    name : str
    field : str
    rank : int
    is_active : bool
    can_sort : bool
    can_be_deactivated : bool
    allows_rank_change : bool
    column_width : int
    type_id : str


@dataclass
class NestedTable:
    type : str
    name : str
    columns : List[Column]
