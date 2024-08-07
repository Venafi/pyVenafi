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
EdgeStatus = Literal[
    "ACTIVE",
    "LOST_CONNECTION",
    "REGISTERED",
    "PAIRED",
    "LOST_CONNECTION_DURING_INSTALL",
    "INSTALLED",
    "INSTALL_FAILED",
    "UNHEALTHY",
    "ERROR",
    "INSTALLING"
]
EdgeType = Literal[
    "ALL",
    "HUB",
    "SATELLITE"
]
KeyAlgorithm = Literal[
    "RSA",
    "ED25519"
]
ProductEntitlement = Literal[
    "ANY",
    "MIRA",
    "DEVOPS",
    "OUTAGE_DETECTION",
    "CODESIGN"
]
WorkerStatus = Literal[
    "DRAFT",
    "PAIRED",
    "ACTIVE",
    "FAILED",
    "INACTIVE"
]

class BillOfMaterialResponse(ObjectModel):
    billsOfMaterials: List[BillOfMaterialsInformation] = ApiField(alias='billsOfMaterials', default_factory=list)

class BillOfMaterialsInformation(ObjectModel):
    charts: List[Chart] = ApiField(alias='charts', default_factory=list)
    name: str = ApiField(alias='name')
    version: str = ApiField(alias='version')

class Chart(ObjectModel):
    name: str = ApiField(alias='name')
    signature: str = ApiField(alias='signature')
    url: str = ApiField(alias='url')
    version: str = ApiField(alias='version')

class ChartDetails(ObjectModel):
    name: str = ApiField(alias='name')
    version: str = ApiField(alias='version')

class EdgeInstanceConnectionDetails(ObjectModel):
    activeMessageCount: int = ApiField(alias='activeMessageCount')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    expiredMessageCount: int = ApiField(alias='expiredMessageCount')
    failedMessageCount: int = ApiField(alias='failedMessageCount')
    lastConnectedDate: datetime = ApiField(alias='lastConnectedDate')
    lastDisconnectedDate: datetime = ApiField(alias='lastDisconnectedDate')
    timestamp: datetime = ApiField(alias='timestamp')

class EdgeInstanceDeleteResponse(ObjectModel):
    name: str = ApiField(alias='name')

class EdgeInstanceHealthDetails(ObjectModel):
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    installedCharts: List[NamespaceChartDetails] = ApiField(alias='installedCharts', default_factory=list)
    nodeStatus: List[NodeStatusDetails] = ApiField(alias='nodeStatus', default_factory=list)
    systemstatus: List[NamespaceStatusDetails] = ApiField(alias='systemstatus', default_factory=list)
    timestamp: datetime = ApiField(alias='timestamp')

class EdgeInstanceInformation(ObjectModel):
    address: str = ApiField(alias='address')
    clientId: str = ApiField(alias='clientId')
    companyId: UUID = ApiField(alias='companyId')
    deploymentDate: datetime = ApiField(alias='deploymentDate')
    edgeStatus: EdgeStatus = ApiField(alias='edgeStatus')
    edgeType: EdgeType = ApiField(alias='edgeType')
    encryptionKeyDeploymentDate: datetime = ApiField(alias='encryptionKeyDeploymentDate')
    encryptionKeyId: str = ApiField(alias='encryptionKeyId')
    environmentId: UUID = ApiField(alias='environmentId')
    id: UUID = ApiField(alias='id')
    integrationServicesCount: int = ApiField(alias='integrationServicesCount')
    kubernetesVersion: str = ApiField(alias='kubernetesVersion')
    lastSeenOnDate: datetime = ApiField(alias='lastSeenOnDate')
    modificationDate: datetime = ApiField(alias='modificationDate')
    name: str = ApiField(alias='name')
    pairingCodeId: UUID = ApiField(alias='pairingCodeId')
    productEntitlements: List[ProductEntitlement] = ApiField(alias='productEntitlements', default_factory=list)
    reconciliationFailed: bool = ApiField(alias='reconciliationFailed')
    statusDetails: EdgeInstanceStatusDetailsInformation = ApiField(alias='statusDetails')
    version: int = ApiField(alias='version')
    workerStatusDetails: List[EdgeWorkerStatusDetailsInformation] = ApiField(
        alias='workerStatusDetails',
        default_factory=list
    )

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
    age: int = ApiField(alias='age')
    cpuUsage: int = ApiField(alias='cpuUsage')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    edgeWorkerId: UUID = ApiField(alias='edgeWorkerId')
    host: str = ApiField(alias='host')
    memoryUsage: int = ApiField(alias='memoryUsage')
    port: int = ApiField(alias='port')
    services: List[WorkerServiceStatusDetails] = ApiField(alias='services', default_factory=list)
    status: str = ApiField(alias='status')
    timestamp: datetime = ApiField(alias='timestamp')

class EdgeWorkerInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    environmentId: UUID = ApiField(alias='environmentId')
    host: str = ApiField(alias='host')
    id: UUID = ApiField(alias='id')
    lastSeenOnDate: datetime = ApiField(alias='lastSeenOnDate')
    pairingCode: str = ApiField(alias='pairingCode')
    pairingPublicKey: str = ApiField(alias='pairingPublicKey')
    port: int = ApiField(alias='port')
    status: WorkerStatus = ApiField(alias='status')

class EdgeWorkerRequest(ObjectModel):
    edgeInstanceId: UUID = ApiField(alias='edgeInstanceId')
    host: str = ApiField(alias='host')
    port: int = ApiField(alias='port')

class EdgeWorkerStatusDetailsInformation(ObjectModel):
    edgeWorkerId: UUID = ApiField(alias='edgeWorkerId')
    healthDetails: List[EdgeWorkerHealthDetails] = ApiField(alias='healthDetails', default_factory=list)

class EdgeWorkersResponse(ObjectModel):
    edgeWorkers: List[EdgeWorkerInformation] = ApiField(alias='edgeWorkers', default_factory=list)

class EncryptionKeyInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    id: str = ApiField(alias='id')
    key: str = ApiField(alias='key')
    keyAlgorithm: KeyAlgorithm = ApiField(alias='keyAlgorithm')
    lastBackupDate: datetime = ApiField(alias='lastBackupDate')

class EncryptionKeysResponse(ObjectModel):
    encryptionKeys: List[EncryptionKeyInformation] = ApiField(alias='encryptionKeys', default_factory=list)

class ErrorInformation(ObjectModel):
    args: List[AnyValue] = ApiField(alias='args', default_factory=list)
    code: int = ApiField(alias='code')
    message: str = ApiField(alias='message')

class ErrorResponse(ObjectModel):
    errors: List[ErrorInformation] = ApiField(alias='errors', default_factory=list)

class NamespaceChartDetails(ObjectModel):
    charts: List[ChartDetails] = ApiField(alias='charts', default_factory=list)
    name: str = ApiField(alias='name')

class NamespaceStatusDetails(ObjectModel):
    name: str = ApiField(alias='name')
    pods: List[PodStatusDetails] = ApiField(alias='pods', default_factory=list)
    timestamp: datetime = ApiField(alias='timestamp')

class NodeCondition(ObjectModel):
    Status: str = ApiField(alias='Status')
    Type: str = ApiField(alias='Type')
    status: str = ApiField(alias='status')
    type: str = ApiField(alias='type')

class NodeInfo(ObjectModel):
    kubelet_version: str = ApiField(alias='kubelet_version')

class NodeStatusDetails(ObjectModel):
    conditions: List[NodeCondition] = ApiField(alias='conditions', default_factory=list)
    info: NodeInfo = ApiField(alias='info')

class PairingCodeInformation(ObjectModel):
    companyId: UUID = ApiField(alias='companyId')
    environmentId: UUID = ApiField(alias='environmentId')
    expirationDate: datetime = ApiField(alias='expirationDate')
    id: UUID = ApiField(alias='id')
    pairingCode: str = ApiField(alias='pairingCode')
    productEntitlements: List[ProductEntitlement] = ApiField(alias='productEntitlements', default_factory=list)
    reuseCount: int = ApiField(alias='reuseCount')

class PairingCodeRequest(ObjectModel):
    environmentId: UUID = ApiField(alias='environmentId')
    expirationDate: datetime = ApiField(alias='expirationDate')
    reuseCount: int = ApiField(alias='reuseCount')

class PodStatusDetails(ObjectModel):
    age: int = ApiField(alias='age')
    cpuUsage: int = ApiField(alias='cpuUsage')
    memoryUsage: int = ApiField(alias='memoryUsage')
    name: str = ApiField(alias='name')
    restartCount: int = ApiField(alias='restartCount')
    status: str = ApiField(alias='status')

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
PodStatusDetails.update_forward_refs()
WorkerServiceStatusDetails.update_forward_refs()
