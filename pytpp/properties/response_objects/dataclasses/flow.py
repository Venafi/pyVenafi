from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def flow_result(self) -> str:
        return ResultCodes.Flow.get(self.code, 'Unknown')


class Approval(PayloadModel):
    approval_time: datetime = PayloadField(alias='ApprovalTime')
    universal: str = PayloadField(alias='Universal')


class KeyValue(PayloadModel):
    key: str = PayloadField(alias='Key')
    value: str = PayloadField(alias='Value')


class Ticket(PayloadModel):
    approvals: List[Approval] = PayloadField(alias='Approvals')
    approvers: List[str] = PayloadField(alias='Approvers')
    creation_time: datetime = PayloadField(alias='CreationTime')
    environment: List[KeyValue] = PayloadField(alias='Environment')
    flow_process_id: int = PayloadField(alias='FlowProcessId')
    id: int = PayloadField(alias='Id')
    identifier: str = PayloadField(alias='Identifier')
    product_code: int = PayloadField(alias='ProductCode')
    remaining_uses: int = PayloadField(alias='RemainingUses')
    required_approvals: int = PayloadField(alias='RequiredApprovals')
