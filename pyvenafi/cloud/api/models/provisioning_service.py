from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class DefaultOwnershipInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    type: str = ApiField(alias='type')


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class Expression(ObjectModel):
    pass


class JsonNode(ObjectModel):
    pass


class MachineCreationRequest(ObjectModel):
    connectionDetails: JsonNode = ApiField(alias='connectionDetails')
    dekId: str = ApiField(alias='dekId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    machineTypeId: UUID = ApiField(alias='machineTypeId')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    pluginId: UUID = ApiField(alias='pluginId')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    tags: List[str] = ApiField(alias='tags', default_factory=list)


class MachineDocumentInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    integrationId: UUID = ApiField(alias='integrationId')
    machineIdentitiesCount: int = ApiField(alias='machineIdentitiesCount')
    machineName: str = ApiField(alias='machineName')
    machineType: str = ApiField(alias='machineType')
    machineTypeId: UUID = ApiField(alias='machineTypeId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    ownership: DefaultOwnershipInformation = ApiField(alias='ownership')
    owningTeam: UUID = ApiField(alias='owningTeam')
    pluginId: UUID = ApiField(alias='pluginId')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')


class MachineDocumentResponse(ObjectModel):
    machines: List[MachineDocumentInformation] = ApiField(alias='machines', default_factory=list)
    totalCount: int = ApiField(alias='totalCount')


class MachineIdentityCreationRequest(ObjectModel):
    binding: JsonNode = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    keystore: JsonNode = ApiField(alias='keystore')
    machineId: UUID = ApiField(alias='machineId')


class MachineIdentityDocumentInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificateId: UUID = ApiField(alias='certificateId')
    certificateName: str = ApiField(alias='certificateName')
    certificateValidityEnd: datetime = ApiField(alias='certificateValidityEnd')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    machineId: UUID = ApiField(alias='machineId')
    machineName: str = ApiField(alias='machineName')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')


class MachineIdentityDocumentResponse(ObjectModel):
    machineIdentities: List[MachineIdentityDocumentInformation] = ApiField(alias='machineIdentities', default_factory=list)


class MachineIdentityInformation(ObjectModel):
    binding: JsonNode = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    keystore: JsonNode = ApiField(alias='keystore')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')


class MachineIdentityResponse(ObjectModel):
    machineIdentities: List[MachineIdentityInformation] = ApiField(alias='machineIdentities', default_factory=list)


class MachineIdentitySearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class MachineIdentityUpdateRequest(ObjectModel):
    binding: JsonNode = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    keystore: JsonNode = ApiField(alias='keystore')
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')


class MachineIdentityWorkflowInformation(ObjectModel):
    workflowId: str = ApiField(alias='workflowId')
    workflowName: str = ApiField(alias='workflowName')


class MachineIdentityWorkflowRequest(ObjectModel):
    workflowInput: ProvisionCertificateWorkflowInputInformation = ApiField(alias='workflowInput')
    workflowName: str = ApiField(alias='workflowName')


class MachineInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    id: UUID = ApiField(alias='id')
    integrationId: UUID = ApiField(alias='integrationId')
    machineType: str = ApiField(alias='machineType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    pluginId: UUID = ApiField(alias='pluginId')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')


class MachineTypeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    machineType: str = ApiField(alias='machineType')
    pluginId: UUID = ApiField(alias='pluginId')


class MachineTypeResponse(ObjectModel):
    machineTypes: List[MachineTypeInformation] = ApiField(alias='machineTypes', default_factory=list)


class MachineUpdateRequest(ObjectModel):
    connectionDetails: JsonNode = ApiField(alias='connectionDetails')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')


class MachineWorkflowRequest(ObjectModel):
    workflowInput: JsonNode = ApiField(alias='workflowInput')
    workflowName: str = ApiField(alias='workflowName')


class MachinesResponse(ObjectModel):
    machines: List[MachineInformation] = ApiField(alias='machines', default_factory=list)


class MachinesSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class OrderObject(ObjectModel):
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')
    field: str = ApiField(alias='field')


class Ordering(ObjectModel):
    orders: List[OrderObject] = ApiField(alias='orders', default_factory=list)


class OwnershipInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    type: str = ApiField(alias='type')


class Paging(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')


class ProvisionCertificateWorkflowInputInformation(ObjectModel):
    wsClientId: str = ApiField(alias='wsClientId')


DefaultOwnershipInformation.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Expression.update_forward_refs()
JsonNode.update_forward_refs()
MachineCreationRequest.update_forward_refs()
MachineDocumentInformation.update_forward_refs()
MachineDocumentResponse.update_forward_refs()
MachineIdentityCreationRequest.update_forward_refs()
MachineIdentityDocumentInformation.update_forward_refs()
MachineIdentityDocumentResponse.update_forward_refs()
MachineIdentityInformation.update_forward_refs()
MachineIdentityResponse.update_forward_refs()
MachineIdentitySearchRequest.update_forward_refs()
MachineIdentityUpdateRequest.update_forward_refs()
MachineIdentityWorkflowInformation.update_forward_refs()
MachineIdentityWorkflowRequest.update_forward_refs()
MachineInformation.update_forward_refs()
MachineTypeInformation.update_forward_refs()
MachineTypeResponse.update_forward_refs()
MachineUpdateRequest.update_forward_refs()
MachineWorkflowRequest.update_forward_refs()
MachinesResponse.update_forward_refs()
MachinesSearchRequest.update_forward_refs()
OrderObject.update_forward_refs()
Ordering.update_forward_refs()
OwnershipInformation.update_forward_refs()
Paging.update_forward_refs()
ProvisionCertificateWorkflowInputInformation.update_forward_refs()
