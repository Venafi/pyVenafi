from __future__ import annotations
from venafi.cloud.api.api_base import ApiField, ObjectModel
from datetime import datetime
from typing import (Any, Dict, List, Literal)
from uuid import UUID


class BillOfMaterialResponse(ObjectModel):
    billsOfMaterials: List[BillOfMaterialsInformation] = ApiField(alias='billsOfMaterials', default_factory=list)


class BillOfMaterialsInformation(ObjectModel):
    name: str = ApiField(alias='name')
    version: str = ApiField(alias='version')
    charts: List[Chart] = ApiField(alias='charts', default_factory=list)


class Chart(ObjectModel):
    name: str = ApiField(alias='name')
    version: str = ApiField(alias='version')
    url: str = ApiField(alias='url')
    signature: str = ApiField(alias='signature')


class ChartDetails(ObjectModel):
    name: str = ApiField(alias='name')
    version: str = ApiField(alias='version')


class EdgeInstanceConnectionDetails(ObjectModel):
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    timestamp: datetime = ApiField(alias='timestamp')
    lastConnectedDate: datetime = ApiField(alias='lastConnectedDate')
    lastDisconnectedDate: datetime = ApiField(alias='lastDisconnectedDate')
    activeMessageCount: int = ApiField(alias='activeMessageCount')
    expiredMessageCount: int = ApiField(alias='expiredMessageCount')
    failedMessageCount: int = ApiField(alias='failedMessageCount')


class EdgeInstanceDeleteResponse(ObjectModel):
    name: str = ApiField(alias='name')


class EdgeInstanceHealthDetails(ObjectModel):
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    timestamp: datetime = ApiField(alias='timestamp')
    systemstatus: List[NamespaceStatusDetails] = ApiField(alias='systemstatus', default_factory=list)
    installedCharts: List[NamespaceChartDetails] = ApiField(alias='installedCharts', default_factory=list)
    nodeStatus: List[NodeStatusDetails] = ApiField(alias='nodeStatus', default_factory=list)


class EdgeInstanceInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    environmentId: UUID = ApiField(alias='environmentId')
    pairingCodeId: UUID = ApiField(alias='pairingCodeId')
    name: str = ApiField(alias='name')
    edgeType: Literal['ALL', 'HUB', 'SATELLITE'] = ApiField(alias='edgeType')
    edgeStatus: Literal['ACTIVE', 'ERROR', 'INSTALLED', 'INSTALLING', 'INSTALL_FAILED', 'LOST_CONNECTION',
                        'LOST_CONNECTION_DURING_INSTALL', 'PAIRED', 'REGISTERED', 'UNHEALTHY'] = ApiField(alias='edgeStatus')
    clientId: str = ApiField(alias='clientId')
    modificationDate: datetime = ApiField(alias='modificationDate')
    address: str = ApiField(alias='address')
    deploymentDate: datetime = ApiField(alias='deploymentDate')
    lastSeenOnDate: datetime = ApiField(alias='lastSeenOnDate')
    statusDetails: EdgeInstanceStatusDetailsInformation = ApiField(alias='statusDetails')
    workerStatusDetails: List[EdgeWorkerStatusDetailsInformation] = ApiField(alias='workerStatusDetails', default_factory=list)
    reconciliationFailed: bool = ApiField(alias='reconciliationFailed')
    encryptionKeyId: str = ApiField(alias='encryptionKeyId')
    encryptionKeyDeploymentDate: datetime = ApiField(alias='encryptionKeyDeploymentDate')
    kubernetesVersion: str = ApiField(alias='kubernetesVersion')
    integrationServicesCount: int = ApiField(alias='integrationServicesCount')


class EdgeInstanceRequest(ObjectModel):
    name: str = ApiField(alias='name')


class EdgeInstanceResponse(ObjectModel):
    edgeInstances: List[EdgeInstanceInformation] = ApiField(alias='edgeInstances', default_factory=list)


class EdgeInstanceStatusDetailsInformation(ObjectModel):
    connectionDetails: List[EdgeInstanceConnectionDetails] = ApiField(alias='connectionDetails', default_factory=list)
    healthDetails: List[EdgeInstanceHealthDetails] = ApiField(alias='healthDetails', default_factory=list)


class EdgeWorkerDeleteResponse(ObjectModel):
    id: UUID = ApiField(alias='id')
    pairingCode: str = ApiField(alias='pairingCode')


class EdgeWorkerHealthDetails(ObjectModel):
    edgeWorkerId: UUID = ApiField(alias='edgeWorkerId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    timestamp: datetime = ApiField(alias='timestamp')
    host: str = ApiField(alias='host')
    port: int = ApiField(alias='port')
    status: str = ApiField(alias='status')
    age: int = ApiField(alias='age')
    cpuUsage: int = ApiField(alias='cpuUsage')
    memoryUsage: int = ApiField(alias='memoryUsage')
    services: List[WorkerServiceStatusDetails] = ApiField(alias='services', default_factory=list)


class EdgeWorkerInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    host: str = ApiField(alias='host')
    port: int = ApiField(alias='port')
    pairingCode: str = ApiField(alias='pairingCode')
    pairingPublicKey: str = ApiField(alias='pairingPublicKey')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    environmentId: UUID = ApiField(alias='environmentId')
    status: Literal['ACTIVE', 'DRAFT', 'FAILED', 'INACTIVE', 'PAIRED'] = ApiField(alias='status')
    lastSeenOnDate: datetime = ApiField(alias='lastSeenOnDate')


class EdgeWorkerRequest(ObjectModel):
    host: str = ApiField(alias='host')
    port: int = ApiField(alias='port')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')


class EdgeWorkerStatusDetailsInformation(ObjectModel):
    edgeWorkerId: UUID = ApiField(alias='edgeWorkerId')
    healthDetails: List[EdgeWorkerHealthDetails] = ApiField(alias='healthDetails', default_factory=list)


class EdgeWorkersResponse(ObjectModel):
    edgeWorkers: List[EdgeWorkerInformation] = ApiField(alias='edgeWorkers', default_factory=list)


class EncryptionKeyInformation(ObjectModel):
    id: str = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    key: str = ApiField(alias='key')
    keyAlgorithm: Literal['ED25519', 'RSA'] = ApiField(alias='keyAlgorithm')
    lastBackupDate: datetime = ApiField(alias='lastBackupDate')


class EncryptionKeysResponse(ObjectModel):
    encryptionKeys: List[EncryptionKeyInformation] = ApiField(alias='encryptionKeys', default_factory=list)


class ErrorInformation(ObjectModel):
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')
    args: List[Dict[str, Any]] = ApiField(alias='args', default_factory=list)


class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)


class NamespaceChartDetails(ObjectModel):
    name: str = ApiField(alias='name')
    charts: List[ChartDetails] = ApiField(alias='charts', default_factory=list)


class NamespaceStatusDetails(ObjectModel):
    timestamp: datetime = ApiField(alias='timestamp')
    name: str = ApiField(alias='name')
    pods: List[PodStatusDetails] = ApiField(alias='pods', default_factory=list)


class NodeCondition(ObjectModel):
    Type: str = ApiField(alias='Type')
    Status: str = ApiField(alias='Status')
    type: str = ApiField(alias='type')
    status: str = ApiField(alias='status')


class NodeInfo(ObjectModel):
    kubelet_version: str = ApiField(alias='kubelet_version')


class NodeStatusDetails(ObjectModel):
    info: NodeInfo = ApiField(alias='info')
    conditions: List[NodeCondition] = ApiField(alias='conditions', default_factory=list)


class PairingCodeInformation(ObjectModel):
    id: UUID = ApiField(alias='id')
    companyId: UUID = ApiField(alias='companyId')
    productEntitlements: List[Literal['ANY', 'DEVOPS', 'MIRA', 'OUTAGE_DETECTION']] = ApiField(alias='productEntitlements', default_factory=list)
    environmentId: UUID = ApiField(alias='environmentId')
    pairingCode: str = ApiField(alias='pairingCode')
    reuseCount: int = ApiField(alias='reuseCount')
    expirationDate: datetime = ApiField(alias='expirationDate')
    modificationDate: datetime = ApiField(alias='modificationDate')


class PairingCodeRequest(ObjectModel):
    environmentId: UUID = ApiField(alias='environmentId')
    reuseCount: int = ApiField(alias='reuseCount')
    expirationDate: datetime = ApiField(alias='expirationDate')


class PairingCodeResponse(ObjectModel):
    pairingCodes: List[PairingCodeInformation] = ApiField(alias='pairingCodes', default_factory=list)


class PodStatusDetails(ObjectModel):
    name: str = ApiField(alias='name')
    age: int = ApiField(alias='age')
    restartCount: int = ApiField(alias='restartCount')
    status: str = ApiField(alias='status')
    cpuUsage: int = ApiField(alias='cpuUsage')
    memoryUsage: int = ApiField(alias='memoryUsage')


class WorkerServiceStatusDetails(ObjectModel):
    name: str = ApiField(alias='name')
    status: str = ApiField(alias='status')


BillOfMaterialResponse.update_forward_refs()
BillOfMaterialsInformation.update_forward_refs()
Chart.update_forward_refs()
ChartDetails.update_forward_refs()
EdgeInstanceConnectionDetails.update_forward_refs()
EdgeInstanceDeleteResponse.update_forward_refs()
EdgeInstanceHealthDetails.update_forward_refs()
EdgeInstanceInformation.update_forward_refs()
EdgeInstanceRequest.update_forward_refs()
EdgeInstanceResponse.update_forward_refs()
EdgeInstanceStatusDetailsInformation.update_forward_refs()
EdgeWorkerDeleteResponse.update_forward_refs()
EdgeWorkerHealthDetails.update_forward_refs()
EdgeWorkerInformation.update_forward_refs()
EdgeWorkerRequest.update_forward_refs()
EdgeWorkerStatusDetailsInformation.update_forward_refs()
EdgeWorkersResponse.update_forward_refs()
EncryptionKeyInformation.update_forward_refs()
EncryptionKeysResponse.update_forward_refs()
ErrorInformation.update_forward_refs()
ErrorResponse.update_forward_refs()
NamespaceChartDetails.update_forward_refs()
NamespaceStatusDetails.update_forward_refs()
NodeCondition.update_forward_refs()
NodeInfo.update_forward_refs()
NodeStatusDetails.update_forward_refs()
PairingCodeInformation.update_forward_refs()
PairingCodeRequest.update_forward_refs()
PairingCodeResponse.update_forward_refs()
PodStatusDetails.update_forward_refs()
WorkerServiceStatusDetails.update_forward_refs()
