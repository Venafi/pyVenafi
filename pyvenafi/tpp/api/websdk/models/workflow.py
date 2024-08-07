from __future__ import annotations

from datetime import datetime

from pyvenafi.tpp.api.api_base import (
    ApiField,
    ObjectModel,
)
from pyvenafi.tpp.api.websdk.models.resultcodes import ResultCodes

class Result(ObjectModel):
    code: int = ApiField()

    @property
    def workflow_result(self) -> str:
        return ResultCodes.Client.get(self.code, 'Unknown')

class Details(ObjectModel):
    approval_explanation: str = ApiField(alias='ApprovalExplanation')
    approval_from: str = ApiField(alias='ApprovalFrom')
    approvers: list[str] = ApiField(alias='Approvers', default_factory=list)
    blocking: str = ApiField(alias='Blocking')
    created: datetime = ApiField(alias='Created')
    issued_due_to: str = ApiField(alias='IssuedDueTo')
    status: str = ApiField(alias='Status')
    updated: datetime = ApiField(alias='Updated')
