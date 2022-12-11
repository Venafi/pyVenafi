from __future__ import annotations
from pyvenafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class EnvironmentInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: UUID = ApiField(alias='id')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)


class EnvironmentResponse(ObjectModel):
    environments: List[EnvironmentInformation] = ApiField(alias='environments', default_factory=list)


class ErrorInformation(ObjectModel):
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class IntegrationServiceCreationRequest(ObjectModel):
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    environmentId: UUID = ApiField(alias='environmentId')
    name: str = ApiField(alias='name')
    runNow: bool = ApiField(alias='runNow')
    scheduleEnabled: bool = ApiField(alias='scheduleEnabled')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    serviceType: Literal['ACME', 'BASIC_DISCOVERY', 'ENHANCED_DISCOVERY', 'EXTERNAL_SCAN', 'INTERNET_DISCOVERY',
                         'KEY_GENERATION', 'MSCA', 'SMART_DISCOVERY_EXTERNAL'] = ApiField(alias='serviceType')
    targets: TargetsInformation = ApiField(alias='targets')
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)


class IntegrationServiceDetailsResponse(ObjectModel):
    integrationsServices: List[IntegrationServiceInformation] = ApiField(alias='integrationsServices', default_factory=list)
    totalCount: int = ApiField(alias='totalCount')


class IntegrationServiceInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    encryptionKeyId: UUID = ApiField(alias='encryptionKeyId')
    environmentId: UUID = ApiField(alias='environmentId')
    id: UUID = ApiField(alias='id')
    lastRunDate: datetime = ApiField(alias='lastRunDate')
    name: str = ApiField(alias='name')
    operationsCount: int = ApiField(alias='operationsCount')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    schedulerEnabled: bool = ApiField(alias='schedulerEnabled')
    serviceType: Literal['ACME', 'BASIC_DISCOVERY', 'ENHANCED_DISCOVERY', 'EXTERNAL_SCAN', 'INTERNET_DISCOVERY',
                         'KEY_GENERATION', 'MSCA', 'SMART_DISCOVERY_EXTERNAL'] = ApiField(alias='serviceType')
    status: Literal['ACTIVE', 'DISABLED', 'DRAFT', 'ERROR', 'RUNNING', 'WARNING'] = ApiField(alias='status')
    statusMessage: str = ApiField(alias='statusMessage')
    systemGenerated: bool = ApiField(alias='systemGenerated')
    targets: TargetsInformation = ApiField(alias='targets')
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)


class IntegrationServiceUpdateRequest(ObjectModel):
    edgeInstancesIds: List[UUID] = ApiField(alias='edgeInstancesIds', default_factory=list)
    name: str = ApiField(alias='name')
    scheduleEnabled: bool = ApiField(alias='scheduleEnabled')
    schedulePattern: SchedulerPatternInformation = ApiField(alias='schedulePattern')
    targets: TargetsInformation = ApiField(alias='targets')
    workTypes: List[Literal['DISCOVER', 'MANAGE']] = ApiField(alias='workTypes', default_factory=list)


class IntegrationsServicesAggregatesResponse(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    integrationsServices: List[Dict[str, Dict[str, Dict[str, int]]]] = ApiField(alias='integrationsServices', default_factory=list)
    totalServicesCount: int = ApiField(alias='totalServicesCount')


class SchedulerPatternInformation(ObjectModel):
    recurrenceType: str = ApiField(alias='recurrenceType')


class TargetsInformation(ObjectModel):
    serviceType: str = ApiField(alias='serviceType')


class WeeklyPatternInformation(SchedulerPatternInformation):
    daysOfWeek: List[Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY',
                             'TUESDAY', 'WEDNESDAY']] = ApiField(alias='daysOfWeek', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')


class BasicDiscoveryTargetsInformation(TargetsInformation):
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    retireCertificates: bool = ApiField(alias='retireCertificates')


class CronPatternInformation(SchedulerPatternInformation):
    cronExpression: str = ApiField(alias='cronExpression')


class EnhancedDiscoveryTargetsInformation(TargetsInformation):
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    retireCertificates: bool = ApiField(alias='retireCertificates')


class ExternalScanTargetsInformation(TargetsInformation):
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    retireCertificates: bool = ApiField(alias='retireCertificates')


class InternetDiscoveryTargetsInformation(TargetsInformation):
    domains: List[str] = ApiField(alias='domains', default_factory=list)
    fqdns: List[str] = ApiField(alias='fqdns', default_factory=list)
    ipRanges: List[str] = ApiField(alias='ipRanges', default_factory=list)
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    retireCertificates: bool = ApiField(alias='retireCertificates')


class KeyGenerationTargetsInformation(TargetsInformation):
    pass


class MonthlyPatternInformation(SchedulerPatternInformation):
    daysOfMonth: List[Literal['D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25',
                              'D26', 'D27', 'D28', 'D29', 'D3', 'D30', 'D31', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'L', 'LW']] = ApiField(alias='daysOfMonth', default_factory=list)
    recurrenceTime: datetime = ApiField(alias='recurrenceTime')


class SmartDiscoveryExternalTargetsInformation(TargetsInformation):
    ports: List[str] = ApiField(alias='ports', default_factory=list)
    retireCertificates: bool = ApiField(alias='retireCertificates')


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
