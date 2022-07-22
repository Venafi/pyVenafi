from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Result(PayloadModel):
    code: int = PayloadField(alias='Code', default=None)
    flow_result: str = PayloadField(alias='FlowResult', default=None)


class Ticket(PayloadModel):
    approvals: 'List[Approval]' = PayloadField(alias='Approvals', default=None)
    approvers: List[str] = PayloadField(alias='Approvers', default=None)
    creation_time: datetime = PayloadField(alias='CreationTime', default=None)
    environment: 'List[KeyValue]' = PayloadField(alias='Environment', default=None)
    flow_process_id: int = PayloadField(alias='FlowProcessId', default=None)
    id: int = PayloadField(alias='Id', default=None)
    identifier: str = PayloadField(alias='Identifier', default=None)
    product_code: int = PayloadField(alias='ProductCode', default=None)
    remaining_uses: int = PayloadField(alias='RemainingUses', default=None)
    required_approvals: int = PayloadField(alias='RequiredApprovals', default=None)


class Approval(PayloadModel):
    approval_time: datetime = PayloadField(alias='ApprovalTime', default=None)
    universal: str = PayloadField(alias='Universal', default=None)


class KeyValue(PayloadModel):
    key: str = PayloadField(alias='Key', default=None)
    value: str = PayloadField(alias='Value', default=None)
