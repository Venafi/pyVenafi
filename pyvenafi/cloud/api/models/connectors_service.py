from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from typing import (
    Any,
    List,
    Literal,
)
from uuid import UUID

AnyValue = Any

class ConnectorProperties(ObjectModel):
    connectorKind: str = ApiField(alias='connectorKind')
    connectorType: Literal['WEBHOOK'] = ApiField(alias='connectorType')

class ConnectorsCreationRequest(ObjectModel):
    name: str = ApiField(alias='name')
    properties: ConnectorProperties = ApiField(alias='properties')

class ConnectorsInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    name: str = ApiField(alias='name')
    properties: ConnectorProperties = ApiField(alias='properties')

class ConnectorsResponse(ObjectModel):
    connectors: List[ConnectorsInformation] = ApiField(alias='connectors', default_factory=list)

class ConnectorsUpdateRequest(ObjectModel):
    name: str = ApiField(alias='name')
    properties: ConnectorProperties = ApiField(alias='properties')

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class Filter(ObjectModel):
    filterType: str = ApiField(alias='filterType')

class JsonNode(ObjectModel):
    ...

class Target(ObjectModel):
    connection: AnyValue = ApiField(alias='connection')
    type: str = ApiField(alias='type')

class WebhookProperties(ConnectorProperties):
    filter: Filter = ApiField(alias='filter')
    target: Target = ApiField(alias='target')

class ActivityFilter(Filter):
    activities: List[str] = ApiField(alias='activities', default_factory=list)
    activityTypes: List[str] = ApiField(alias='activityTypes', default_factory=list)
    criticality: int = ApiField(alias='criticality')

class ExpirationFilter(Filter):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)

ActivityFilter.update_forward_refs()
ConnectorProperties.update_forward_refs()
ConnectorsCreationRequest.update_forward_refs()
ConnectorsInformation.update_forward_refs()
ConnectorsResponse.update_forward_refs()
ConnectorsUpdateRequest.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExpirationFilter.update_forward_refs()
Filter.update_forward_refs()
JsonNode.update_forward_refs()
Target.update_forward_refs()
WebhookProperties.update_forward_refs()
