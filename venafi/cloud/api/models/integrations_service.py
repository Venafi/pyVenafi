from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from uuid import UUID
from typing import (Any, Dict, List, Literal)
from datetime import datetime


class BasicDiscoveryTargetsInformation(ObjectModel):
    pass


class CronPatternInformation(ObjectModel):
    pass


class EnhancedDiscoveryTargetsInformation(ObjectModel):
    pass


class EnvironmentInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    name: str = ApiField(alias='name')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    modificationDate: datetime = ApiField(alias='modificationDate')


class EnvironmentResponse(ObjectModel):
    environments: List[EnvironmentInformation] = ApiField(alias='environments', default_factory=list)


class ErrorInformation(ObjectModel):
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class ExternalScanTargetsInformation(ObjectModel):
    pass


class IntegrationServiceCreationRequest(ObjectModel):
    environmentId: UUID = ApiField(alias='environmentId')
    name: str = ApiField(alias='name')
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)
    serviceType: Literal['ACME', 'BASIC_DISCOVERY', 'ENHANCED_DISCOVERY', 'EXTERNAL_SCAN', 'INTERNET_DISCOVERY',
                         'KEY_GENERATION', 'MSCA', 'SMART_DISCOVERY_EXTERNAL'] = ApiField(alias='serviceType')
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    scheduleEnabled: bool = ApiField(alias='scheduleEnabled')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    runNow: bool = ApiField(alias='runNow')
    targets: TargetsInformation = ApiField(alias='targets')


class IntegrationServiceDetailsResponse(ObjectModel):
    integrationsServices: List[IntegrationServiceInformation] = ApiField(alias='integrationsServices', default_factory=list)
    totalCount: int = ApiField(alias='totalCount')


class IntegrationServiceInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    environmentId: UUID = ApiField(alias='environmentId')
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    name: str = ApiField(alias='name')
    status: Literal['ACTIVE', 'DISABLED', 'DRAFT', 'ERROR', 'RUNNING', 'WARNING'] = ApiField(alias='status')
    statusMessage: str = ApiField(alias='statusMessage')
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)
    serviceType: Literal['ACME', 'BASIC_DISCOVERY', 'ENHANCED_DISCOVERY', 'EXTERNAL_SCAN', 'INTERNET_DISCOVERY',
                         'KEY_GENERATION', 'MSCA', 'SMART_DISCOVERY_EXTERNAL'] = ApiField(alias='serviceType')
    schedulerEnabled: bool = ApiField(alias='schedulerEnabled')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    operationsCount: int = ApiField(alias='operationsCount')
    lastRunDate: datetime = ApiField(alias='lastRunDate')
    systemGenerated: bool = ApiField(alias='systemGenerated')
    targets: TargetsInformation = ApiField(alias='targets')
    encryptionKeyId: UUID = ApiField(alias='encryptionKeyId')


class IntegrationServiceUpdateRequest(ObjectModel):
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)
    name: str = ApiField(alias='name')
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    scheduleEnabled: bool = ApiField(alias='scheduleEnabled')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    targets: TargetsInformation = ApiField(alias='targets')


class IntegrationsServicesAggregatesResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    totalServicesCount: int = ApiField(alias='totalServicesCount')
    integrationsServices: Dict[str, Dict[str, Dict[str, int]]] = ApiField(alias='integrationsServices', default_factory=dict)


class InternetDiscoveryTargetsInformation(ObjectModel):
    pass


class KeyGenerationTargetsInformation(ObjectModel):
    pass


class MonthlyPatternInformation(ObjectModel):
    pass


class SchedulerPatternInformation(ObjectModel):
    recurrenceType: str = ApiField(alias='recurrenceType')


class SmartDiscoveryExternalTargetsInformation(ObjectModel):
    pass


class TargetsInformation(ObjectModel):
    serviceType: str = ApiField(alias='serviceType')


class WeeklyPatternInformation(ObjectModel):
    pass


BasicDiscoveryTargetsInformation.update_forward_refs()
CronPatternInformation.update_forward_refs()
EnhancedDiscoveryTargetsInformation.update_forward_refs()
EnvironmentInformation.update_forward_refs()
EnvironmentResponse.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
ExternalScanTargetsInformation.update_forward_refs()
IntegrationServiceCreationRequest.update_forward_refs()
IntegrationServiceDetailsResponse.update_forward_refs()
IntegrationServiceInformation.update_forward_refs()
IntegrationServiceUpdateRequest.update_forward_refs()
IntegrationsServicesAggregatesResponse.update_forward_refs()
InternetDiscoveryTargetsInformation.update_forward_refs()
KeyGenerationTargetsInformation.update_forward_refs()
MonthlyPatternInformation.update_forward_refs()
SchedulerPatternInformation.update_forward_refs()
SmartDiscoveryExternalTargetsInformation.update_forward_refs()
TargetsInformation.update_forward_refs()
WeeklyPatternInformation.update_forward_refs()
