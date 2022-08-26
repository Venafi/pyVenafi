from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField


class Condition(ObjectModel):
    field: str = ApiField(alias='field')
    comparison: str = ApiField(alias='comparison')
    value: str = ApiField(alias='value')
