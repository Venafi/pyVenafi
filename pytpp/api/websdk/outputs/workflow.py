from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime
from typing import List


class Result(OutputModel):
    code: int = ApiField()

    @property
    def workflow_result(self) -> str:
        return ResultCodes.Client.get(self.code, 'Unknown')


class Details(OutputModel):
    approval_explanation: str = ApiField(alias='ApprovalExplanation')
    approval_from: str = ApiField(alias='ApprovalFrom')
    approvers: List[str] = ApiField(alias='Approvers')
    blocking: str = ApiField(alias='Blocking')
    created: datetime = ApiField(alias='Created')
    issued_due_to: str = ApiField(alias='IssuedDueTo')
    status: str = ApiField(alias='Status')
    updated: datetime = ApiField(alias='Updated')
