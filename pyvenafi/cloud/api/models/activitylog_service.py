from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


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


class ActivityLogName(ObjectModel):
    key: str = ApiField(alias='key')
    readableName: str = ApiField(alias='readableName')


class ActivityLogSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class ActivityLogType(ObjectModel):
    key: str = ApiField(alias='key')
    readableName: str = ApiField(alias='readableName')
    values: List[ActivityLogName] = ApiField(alias='values', default_factory=list)


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class Expression(ObjectModel):
    pass


class OrderObject(ObjectModel):
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')
    field: str = ApiField(alias='field')


class Ordering(ObjectModel):
    orders: List[OrderObject] = ApiField(alias='orders', default_factory=list)


class Paging(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')


ActivityLogEntriesResponse.update_forward_refs()
ActivityLogEntryInformation.update_forward_refs()
ActivityLogName.update_forward_refs()
ActivityLogSearchRequest.update_forward_refs()
ActivityLogType.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Expression.update_forward_refs()
OrderObject.update_forward_refs()
Ordering.update_forward_refs()
Paging.update_forward_refs()
