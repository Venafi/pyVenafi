from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Literal,
)
from uuid import UUID

ActivityLogFilterOperator = Literal[
    "EQ",
    "LT",
    "LTE",
    "GT",
    "GTE",
    "IN"
]
AnyValue = Any
Direction = Literal[
    "ASC",
    "DESC"
]
NaryOperator = Literal[
    "AND",
    "OR"
]
UnaryOperator = Literal['NOT']

class ActivityLogCondition(ObjectModel):
    field: str = ApiField(alias='field')
    operator: ActivityLogFilterOperator = ApiField(alias='operator')
    value: str = ApiField(alias='value')
    values: List[str] = ApiField(alias='values', default_factory=list)

class ActivityLogEntriesResponse(ObjectModel):
    activityLogEntries: List[ActivityLogEntryInformation] = ApiField(alias='activityLogEntries', default_factory=list)
    count: int = ApiField(alias='count')

class ActivityLogEntryInformation(ObjectModel):
    activityDate: datetime = ApiField(alias='activityDate')
    activityName: str = ApiField(alias='activityName')
    activityType: str = ApiField(alias='activityType')
    companyId: UUID = ApiField(alias='companyId')
    criticality: int = ApiField(alias='criticality')
    id: UUID = ApiField(alias='id')
    message: str = ApiField(alias='message')
    payload: Dict[str, str] = ApiField(alias='payload', default_factory=dict)

class ActivityLogFilter(ObjectModel):
    expression: BaseActivityLogFilter = ApiField(alias='expression')
    ordering: BaseActivityLogOrdering = ApiField(alias='ordering')
    paging: Page = ApiField(alias='paging')

class ActivityLogFilterOperand(ObjectModel):
    operand: ActivityLogCondition = ApiField(alias='operand')
    operator: UnaryOperator = ApiField(alias='operator')

class ActivityLogFilterOperands(ObjectModel):
    operands: List[BaseActivityLogFilter] = ApiField(alias='operands', default_factory=list)
    operator: NaryOperator = ApiField(alias='operator')

class ActivityLogName(ObjectModel):
    key: str = ApiField(alias='key')
    readableName: str = ApiField(alias='readableName')

class ActivityLogOrder(ObjectModel):
    direction: Direction = ApiField(alias='direction')
    field: str = ApiField(alias='field')

class ActivityLogType(ObjectModel):
    key: str = ApiField(alias='key')
    readableName: str = ApiField(alias='readableName')
    values: List[ActivityLogName] = ApiField(alias='values', default_factory=list)

class BaseActivityLogFilter(ObjectModel):
    ...

class BaseActivityLogOrdering(ObjectModel):
    orders: List[ActivityLogOrder] = ApiField(alias='orders', default_factory=list)

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class ExportedActivityLogEntryInformation(ObjectModel):
    activityDate: datetime = ApiField(alias='activityDate')
    activityName: str = ApiField(alias='activityName')
    activityType: str = ApiField(alias='activityType')
    criticality: int = ApiField(alias='criticality')
    id: UUID = ApiField(alias='id')
    message: str = ApiField(alias='message')
    payload: Dict[str, str] = ApiField(alias='payload', default_factory=dict)

class Page(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')

ActivityLogCondition.update_forward_refs()
ActivityLogEntriesResponse.update_forward_refs()
ActivityLogEntryInformation.update_forward_refs()
ActivityLogFilter.update_forward_refs()
ActivityLogFilterOperand.update_forward_refs()
ActivityLogFilterOperands.update_forward_refs()
ActivityLogName.update_forward_refs()
ActivityLogOrder.update_forward_refs()
ActivityLogType.update_forward_refs()
BaseActivityLogFilter.update_forward_refs()
BaseActivityLogOrdering.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExportedActivityLogEntryInformation.update_forward_refs()
Page.update_forward_refs()
