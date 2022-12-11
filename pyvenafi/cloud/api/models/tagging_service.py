from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class TagInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    isReserved: bool = ApiField(alias='isReserved')
    key: str = ApiField(alias='key')
    name: str = ApiField(alias='name')


class TagRequest(ObjectModel):
    name: str = ApiField(alias='name')
    values: List[str] = ApiField(alias='values', default_factory=list)


class TagResponse(ObjectModel):
    count: int = ApiField(alias='count')
    tags: List[TagInformation] = ApiField(alias='tags', default_factory=list)


class TagValueInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    tagId: UUID = ApiField(alias='tagId')
    value: str = ApiField(alias='value')


class TagValuesRequest(ObjectModel):
    values: List[str] = ApiField(alias='values', default_factory=list)


class TagValuesResponse(ObjectModel):
    count: int = ApiField(alias='count')
    values: List[TagValueInformation] = ApiField(alias='values', default_factory=list)


class TagsAssignInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    entityId: UUID = ApiField(alias='entityId')
    entityType: Literal['APPLICATION', 'CERTIFICATE', 'CERTIFICATE_INSTANCE'] = ApiField(alias='entityType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    tags: List[str] = ApiField(alias='tags', default_factory=list)


class TagsAssignRequest(ObjectModel):
    action: Literal['ADD', 'DELETE', 'DELETE_ALL', 'REPLACE'] = ApiField(alias='action')
    entityIds: List[UUID] = ApiField(alias='entityIds', default_factory=list)
    entityType: Literal['APPLICATION', 'CERTIFICATE', 'CERTIFICATE_INSTANCE'] = ApiField(alias='entityType')
    targetedTags: List[str] = ApiField(alias='targetedTags', default_factory=list)


class TagsAssignResponse(ObjectModel):
    tagsAssignInformation: List[TagsAssignInformation] = ApiField(alias='tagsAssignInformation', default_factory=list)


ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
TagInformation.update_forward_refs()
TagRequest.update_forward_refs()
TagResponse.update_forward_refs()
TagValueInformation.update_forward_refs()
TagValuesRequest.update_forward_refs()
TagValuesResponse.update_forward_refs()
TagsAssignInformation.update_forward_refs()
TagsAssignRequest.update_forward_refs()
TagsAssignResponse.update_forward_refs()
