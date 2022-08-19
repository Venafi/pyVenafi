from __future__ import annotations
from pytpp.api.api_base import OutputModel, ApiField


class Condition(OutputModel):
    field: str = ApiField(alias='field')
    comparison: str = ApiField(alias='comparison')
    value: str = ApiField(alias='value')
