from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField
from datetime import datetime
from typing import List


class Result(OutputModel):
    code: int = ApiField()

    @property
    def flow_result(self) -> str:
        return ResultCodes.Flow.get(self.code, 'Unknown')


class Approval(OutputModel):
    approval_time: datetime = ApiField(alias='ApprovalTime')
    universal: str = ApiField(alias='Universal')


class KeyValue(OutputModel):
    key: str = ApiField(alias='Key')
    value: str = ApiField(alias='Value')


class Ticket(OutputModel):
    approvals: List[Approval] = ApiField(alias='Approvals')
    approvers: List[str] = ApiField(alias='Approvers')
    creation_time: datetime = ApiField(alias='CreationTime')
    environment: List[KeyValue] = ApiField(alias='Environment')
    flow_process_id: int = ApiField(alias='FlowProcessId')
    id: int = ApiField(alias='Id')
    identifier: str = ApiField(alias='Identifier')
    product_code: int = ApiField(alias='ProductCode')
    remaining_uses: int = ApiField(alias='RemainingUses')
    required_approvals: int = ApiField(alias='RequiredApprovals')
