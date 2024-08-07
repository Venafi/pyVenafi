from __future__ import annotations
from pyvenafi.cloud.api.api_base import (
    ApiField,
    ObjectModel,
)
from datetime import datetime
from typing import (
    Any,
    List,
    Literal,
)
from uuid import UUID

AnyValue = Any

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class Expression(ObjectModel):
    ...

class JsonNode(ObjectModel):
    ...

class MachineBatchProvisioningResultInformation(ObjectModel):
    endDate: datetime = ApiField(alias='endDate')
    errorMessage: str = ApiField(alias='errorMessage')
    machineIdentitiesCount: int = ApiField(alias='machineIdentitiesCount')
    machineIdentitiesFailedCount: int = ApiField(alias='machineIdentitiesFailedCount')
    machineIdentitiesSucceedCount: int = ApiField(alias='machineIdentitiesSucceedCount')
    startDate: datetime = ApiField(alias='startDate')
    type: Literal['MANUAL', 'SCHEDULED'] = ApiField(alias='type')

class MachineCreationRequest(ObjectModel):
    connectionDetails: AnyValue = ApiField(alias='connectionDetails')
    dekId: str = ApiField(alias='dekId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    machineTypeId: UUID = ApiField(alias='machineTypeId')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    pluginId: UUID = ApiField(alias='pluginId')
    status: Literal['DELETING', 'DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')
    tags: List[str] = ApiField(alias='tags', default_factory=list)

class MachineDiscoveryResultInformation(ObjectModel):
    certificatesCountCurrent: int = ApiField(alias='certificatesCountCurrent')
    certificatesCountTotal: int = ApiField(alias='certificatesCountTotal')
    discoveryStatus: Literal['ABORTED', 'ABORTING', 'COMPLETED', 'FAILED',
    'INITIATED', 'NEVER INITIATED', 'RUNNING'] = ApiField(alias='discoveryStatus')
    endDate: datetime = ApiField(alias='endDate')
    errorCount: int = ApiField(alias='errorCount')
    machineIdentitiesCount: int = ApiField(alias='machineIdentitiesCount')
    machineIdentitiesDeletedCount: int = ApiField(alias='machineIdentitiesDeletedCount')
    machineIdentitiesMissingCount: int = ApiField(alias='machineIdentitiesMissingCount')
    startDate: datetime = ApiField(alias='startDate')

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
    ownership: MachineOwnership = ApiField(alias='ownership')
    owningTeam: UUID = ApiField(alias='owningTeam')
    pluginId: UUID = ApiField(alias='pluginId')
    pluginName: str = ApiField(alias='pluginName')
    status: Literal['DELETING', 'DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')

class MachineDocumentResponse(ObjectModel):
    machines: List[MachineDocumentInformation] = ApiField(alias='machines', default_factory=list)
    totalCount: int = ApiField(alias='totalCount')

class MachineIdentityCreationRequest(ObjectModel):
    binding: AnyValue = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    keystore: AnyValue = ApiField(alias='keystore')
    machineId: UUID = ApiField(alias='machineId')

class MachineIdentityDocumentInformation(ObjectModel):
    applicationIds: List[UUID] = ApiField(alias='applicationIds', default_factory=list)
    certificateFingerprint: str = ApiField(alias='certificateFingerprint')
    certificateId: UUID = ApiField(alias='certificateId')
    certificateName: str = ApiField(alias='certificateName')
    certificateValidityEnd: datetime = ApiField(alias='certificateValidityEnd')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    lastSeenOn: datetime = ApiField(alias='lastSeenOn')
    machineId: UUID = ApiField(alias='machineId')
    machineName: str = ApiField(alias='machineName')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['DISCOVERED', 'FAILED', 'INSTALLED', 'MISSING', 'NEW', 'PENDING', 'VALIDATED'] = ApiField(
        alias='status'
    )

class MachineIdentityDocumentResponse(ObjectModel):
    machineIdentities: List[MachineIdentityDocumentInformation] = ApiField(
        alias='machineIdentities',
        default_factory=list
    )

class MachineIdentityInformation(ObjectModel):
    binding: AnyValue = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    id: UUID = ApiField(alias='id')
    keystore: AnyValue = ApiField(alias='keystore')
    lastSeenOn: datetime = ApiField(alias='lastSeenOn')
    machineId: UUID = ApiField(alias='machineId')
    metadata: AnyValue = ApiField(alias='metadata')
    modificationDate: datetime = ApiField(alias='modificationDate')
    status: Literal['DISCOVERED', 'FAILED', 'INSTALLED', 'MISSING', 'NEW', 'PENDING', 'VALIDATED'] = ApiField(
        alias='status'
    )

class MachineIdentityResponse(ObjectModel):
    machineIdentities: List[MachineIdentityInformation] = ApiField(alias='machineIdentities', default_factory=list)

class MachineIdentitySearchRequest(ObjectModel):
    expression: Expression = ApiField(alias='expression')
    ordering: Ordering = ApiField(alias='ordering')
    paging: Paging = ApiField(alias='paging')

class MachineIdentityUpdateRequest(ObjectModel):
    binding: AnyValue = ApiField(alias='binding')
    certificateId: UUID = ApiField(alias='certificateId')
    keystore: AnyValue = ApiField(alias='keystore')
    status: Literal['DISCOVERED', 'FAILED', 'INSTALLED', 'MISSING', 'NEW', 'PENDING', 'VALIDATED'] = ApiField(
        alias='status'
    )

class MachineIdentityWorkflowInformation(ObjectModel):
    workflowId: str = ApiField(alias='workflowId')
    workflowName: str = ApiField(alias='workflowName')

class MachineIdentityWorkflowRequest(ObjectModel):
    workflowInput: ProvisionCertificateWorkflowInputInformation = ApiField(alias='workflowInput')
    workflowName: str = ApiField(alias='workflowName')

class MachineInformation(ObjectModel):
    batchProvisioningResult: MachineBatchProvisioningResultInformation = ApiField(alias='batchProvisioningResult')
    batchProvisioningSchedulerEnabled: bool = ApiField(alias='batchProvisioningSchedulerEnabled')
    batchProvisioningSchedulerPattern: SchedulerPatternInformation = ApiField(alias='batchProvisioningSchedulerPattern')
    batchProvisioningStatus: Literal['ABORTED', 'ABORTING', 'COMPLETED', 'FAILED',
    'INITIATED', 'NEVER_INITIATED', 'RUNNING'] = ApiField(alias='batchProvisioningStatus')
    companyId: UUID = ApiField(alias='companyId')
    creationDate: datetime = ApiField(alias='creationDate')
    discoveryJson: AnyValue = ApiField(alias='discoveryJson')
    discoverySchedulerEnabled: bool = ApiField(alias='discoverySchedulerEnabled')
    discoverySchedulerPattern: SchedulerPatternInformation = ApiField(alias='discoverySchedulerPattern')
    discoveryStatus: Literal['ABORTED', 'ABORTING', 'COMPLETED', 'FAILED',
    'INITIATED', 'NEVER INITIATED', 'RUNNING'] = ApiField(alias='discoveryStatus')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    id: UUID = ApiField(alias='id')
    integrationId: UUID = ApiField(alias='integrationId')
    machineType: str = ApiField(alias='machineType')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    pluginId: UUID = ApiField(alias='pluginId')
    status: Literal['DELETING', 'DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')

class MachineOwnership(ObjectModel):
    owningTeams: List[UUID] = ApiField(alias='owningTeams', default_factory=list)

class MachineTypeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    machineType: str = ApiField(alias='machineType')
    pluginId: UUID = ApiField(alias='pluginId')

class MachineTypeResponse(ObjectModel):
    machineTypes: List[MachineTypeInformation] = ApiField(alias='machineTypes', default_factory=list)

class MachineUpdateRequest(ObjectModel):
    batchProvisioningSchedulerEnabled: bool = ApiField(alias='batchProvisioningSchedulerEnabled')
    batchProvisioningSchedulerPattern: SchedulerPatternInformation = ApiField(alias='batchProvisioningSchedulerPattern')
    connectionDetails: AnyValue = ApiField(alias='connectionDetails')
    discoveryJson: AnyValue = ApiField(alias='discoveryJson')
    discoverySchedulerEnabled: bool = ApiField(alias='discoverySchedulerEnabled')
    discoverySchedulerPattern: SchedulerPatternInformation = ApiField(alias='discoverySchedulerPattern')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    name: str = ApiField(alias='name')
    owningTeamId: UUID = ApiField(alias='owningTeamId')
    status: Literal['DELETING', 'DRAFT', 'UNVERIFIED', 'VERIFIED'] = ApiField(alias='status')

class MachineWorkflowRequest(ObjectModel):
    workflowInput: AnyValue = ApiField(alias='workflowInput')
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

class Paging(ObjectModel):
    pageNumber: int = ApiField(alias='pageNumber')
    pageSize: int = ApiField(alias='pageSize')

class ProvisionCertificateWorkflowInputInformation(ObjectModel):
    wsClientId: str = ApiField(alias='wsClientId')

class SchedulerPatternInformation(ObjectModel):
    recurrenceType: str = ApiField(alias='recurrenceType')

class WeeklyPatternInformation(SchedulerPatternInformation):
    daysOfWeek: List[Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY',
    'TUESDAY', 'WEDNESDAY']] = ApiField(alias='daysOfWeek', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')

class CronPatternInformation(SchedulerPatternInformation):
    cronExpression: str = ApiField(alias='cronExpression')

class MonthlyPatternInformation(SchedulerPatternInformation):
    daysOfMonth: List[int] = ApiField(alias='daysOfMonth', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')

CronPatternInformation.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
Expression.update_forward_refs()
JsonNode.update_forward_refs()
MachineBatchProvisioningResultInformation.update_forward_refs()
MachineCreationRequest.update_forward_refs()
MachineDiscoveryResultInformation.update_forward_refs()
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
MachineOwnership.update_forward_refs()
MachineTypeInformation.update_forward_refs()
MachineTypeResponse.update_forward_refs()
MachineUpdateRequest.update_forward_refs()
MachineWorkflowRequest.update_forward_refs()
MachinesResponse.update_forward_refs()
MachinesSearchRequest.update_forward_refs()
MonthlyPatternInformation.update_forward_refs()
OrderObject.update_forward_refs()
Ordering.update_forward_refs()
Paging.update_forward_refs()
ProvisionCertificateWorkflowInputInformation.update_forward_refs()
SchedulerPatternInformation.update_forward_refs()
WeeklyPatternInformation.update_forward_refs()
