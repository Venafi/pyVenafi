from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Result(PayloadModel):
    code: int = PayloadField(alias='Code')
    workflow_result: str = PayloadField(alias='WorkflowResult')


class Details(PayloadModel):
    approval_explanation: str = PayloadField(alias='ApprovalExplanation')
    approval_from: str = PayloadField(alias='ApprovalFrom')
    approvers: List[str] = PayloadField(alias='Approvers')
    blocking: str = PayloadField(alias='Blocking')
    created: datetime = PayloadField(alias='Created')
    issued_due_to: str = PayloadField(alias='IssuedDueTo')
    status: str = PayloadField(alias='Status')
    updated: datetime = PayloadField(alias='Updated')
