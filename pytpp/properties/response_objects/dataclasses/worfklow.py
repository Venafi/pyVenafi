from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    workflow_result: str = PayloadField(alias='WorkflowResult', default=None)


class Details(PayloadModel):
    approval_explanation: str = PayloadField(alias='ApprovalExplanation', default=None)
    approval_from: str = PayloadField(alias='ApprovalFrom', default=None)
    approvers: List[str] = PayloadField(alias='Approvers', default=None)
    blocking: str = PayloadField(alias='Blocking', default=None)
    created: datetime = PayloadField(alias='Created', default=None)
    issued_due_to: str = PayloadField(alias='IssuedDueTo', default=None)
    status: str = PayloadField(alias='Status', default=None)
    updated: datetime = PayloadField(alias='Updated', default=None)
