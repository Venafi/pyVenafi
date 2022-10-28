from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class DefaultOwnershipInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    type: str = ApiField(alias='type')
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)


class ErrorInformation(ObjectModel):
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class Expression(ObjectModel):
    pass


class JsonNode(ObjectModel):
    pass


class MachineCreationRequest(ObjectModel):
    name: str = ApiField(alias='name')
    machineTypeId: UUID = ApiField(alias='machineTypeId')
    pluginId: UUID = ApiField(alias='pluginId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    dekId: str = ApiField(alias='dekId')
    tags: List[str] = ApiField(alias='tags', default_factory=list)
    connectionDetails: JsonNode = ApiField(alias='connectionDetails')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    owningTeamId: UUID = ApiField(alias='owningTeamId')


class MachineDocumentInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    machineTypeId: UUID = ApiField(alias='machineTypeId')
    pluginId: UUID = ApiField(alias='pluginId')
    integrationId: UUID = ApiField(alias='integrationId')
    machineName: str = ApiField(alias='machineName')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    machineType: str = ApiField(alias='machineType')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    machineIdentitiesCount: int = ApiField(alias='machineIdentitiesCount')
    owningTeam: UUID = ApiField(alias='owningTeam')
    ownership: DefaultOwnershipInformation = ApiField(alias='ownership')


class MachineDocumentResponse(ObjectModel):
    totalCount: int = ApiField(alias='totalCount')
    machines: List[MachineDocumentInformation] = ApiField(alias='machines', default_factory=list)


class MachineIdentityCreationRequest(ObjectModel):
    certificateId: UUID = ApiField(alias='certificateId')
    machineId: UUID = ApiField(alias='machineId')
    keystore: JsonNode = ApiField(alias='keystore')
    binding: JsonNode = ApiField(alias='binding')


class MachineIdentityDocumentInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    machineId: UUID = ApiField(alias='machineId')
    machineName: str = ApiField(alias='machineName')
    certificateId: UUID = ApiField(alias='certificateId')
    certificateName: str = ApiField(alias='certificateName')
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    certificateValidityEnd: datetime = ApiField(alias='certificateValidityEnd')


class MachineIdentityDocumentResponse(ObjectModel):
    machineIdentities: List[MachineIdentityDocumentInformation] = ApiField(alias='machineIdentities', default_factory=list)


class MachineIdentityInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    certificateId: UUID = ApiField(alias='certificateId')
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    keystore: JsonNode = ApiField(alias='keystore')
    binding: JsonNode = ApiField(alias='binding')


class MachineIdentityResponse(ObjectModel):
    machineIdentities: List[MachineIdentityInformation] = ApiField(alias='machineIdentities', default_factory=list)


class MachineIdentitySearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class MachineIdentityUpdateRequest(ObjectModel):
    certificateId: UUID = ApiField(alias='certificateId')
    status: Literal['FAILED', 'INSTALLED', 'NEW', 'PENDING'] = ApiField(alias='status')
    keystore: JsonNode = ApiField(alias='keystore')
    binding: JsonNode = ApiField(alias='binding')


class MachineIdentityWorkflowInformation(ObjectModel):
    workflowId: str = ApiField(alias='workflowId')
    workflowName: str = ApiField(alias='workflowName')


class MachineIdentityWorkflowRequest(ObjectModel):
    workflowName: str = ApiField(alias='workflowName')
    workflowInput: ProvisionCertificateWorkflowInputInformation = ApiField(alias='workflowInput')


class MachineInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    name: str = ApiField(alias='name')
    machineType: str = ApiField(alias='machineType')
    pluginId: UUID = ApiField(alias='pluginId')
    integrationId: UUID = ApiField(alias='integrationId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    creationDate: datetime = ApiField(alias='creationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    owningTeamId: UUID = ApiField(alias='owningTeamId')


class MachineTypeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    machineType: str = ApiField(alias='machineType')
    pluginId: UUID = ApiField(alias='pluginId')


class MachineTypeResponse(ObjectModel):
    machineTypes: List[MachineTypeInformation] = ApiField(alias='machineTypes', default_factory=list)


class MachineUpdateRequest(ObjectModel):
    name: str = ApiField(alias='name')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    connectionDetails: JsonNode = ApiField(alias='connectionDetails')
    status: Literal['DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    owningTeamId: UUID = ApiField(alias='owningTeamId')


class MachineWorkflowRequest(ObjectModel):
    workflowName: str = ApiField(alias='workflowName')
    workflowInput: JsonNode = ApiField(alias='workflowInput')


class MachinesResponse(ObjectModel):
    machines: List[MachineInformation] = ApiField(alias='machines', default_factory=list)


class MachinesSearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')


class OrderObject(ObjectModel):
    field: str = ApiField(alias='field')
    direction: Literal['ASC', 'DESC'] = ApiField(alias='direction')


class Ordering(ObjectModel):
    orders: List[OrderObject] = ApiField(alias='orders', default_factory=list)


class OwnershipInformation(ObjectModel):
    type: str = ApiField(alias='type')
    owningContainers: List[OwnershipInformation] = ApiField(alias='owningContainers', default_factory=list)
    owningUsers: List[UUID] = ApiField(alias='owningUsers', default_factory=list)
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)
    id: UUID = ApiField(alias='id')


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
