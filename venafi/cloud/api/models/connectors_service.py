from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class ConnectorProperties(ObjectModel):
    connectorType: Literal['WEBHOOK'] = ApiField(alias='connectorType')
    connectorKind: str = ApiField(alias='connectorKind')


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
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class Filter(ObjectModel):
    activityTypes: List[str] = ApiField(alias='activityTypes', default_factory=list)


class JsonNode(ObjectModel):
    pass


class Target(ObjectModel):
    type: str = ApiField(alias='type')
    connection: JsonNode = ApiField(alias='connection')


class WebhookProperties(ObjectModel):
    pass


ConnectorProperties.update_forward_refs()
ConnectorsCreationRequest.update_forward_refs()
ConnectorsInformation.update_forward_refs()
ConnectorsResponse.update_forward_refs()
ConnectorsUpdateRequest.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Filter.update_forward_refs()
JsonNode.update_forward_refs()
Target.update_forward_refs()
WebhookProperties.update_forward_refs()
