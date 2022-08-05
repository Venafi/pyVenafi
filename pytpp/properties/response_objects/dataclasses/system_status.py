from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Engine(PayloadModel):
    dn: str = PayloadField(alias='Dn')
    display_name: str = PayloadField(alias='DisplayName')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    name: str = PayloadField(alias='Name')


class IisService(PayloadModel):
    modules: List[str] = PayloadField(alias='modules')
    time_since_first_seen: datetime = PayloadField(alias='timeSinceFirstSeen')
    time_since_last_seen: datetime = PayloadField(alias='timeSinceLastSeen')
    status: str = PayloadField(alias='status')


class LogServerService(IisService): ...  # This is currently the same.


class vPlatformService(PayloadModel):
    configured_latency: int = PayloadField(alias='configuredLatency')
    configured_mode: str = PayloadField(alias='configuredMode')
    configured_work: int = PayloadField(alias='configuredWork')
    current_latency: int = PayloadField(alias='currentLatency')
    current_mode: str = PayloadField(alias='currentMode')
    current_work: int = PayloadField(alias='currentWork')
    modules: List[str] = PayloadField(alias='modules')
    status: str = PayloadField(alias='status')
    time_since_first_seen: datetime = PayloadField(alias='timeSinceFirstSeen')
    time_since_last_seen: datetime = PayloadField(alias='timeSinceLastSeen')


class Services(PayloadModel):
    vplatform: vPlatformService = PayloadField(alias='Vplatform')
    log_server: LogServerService = PayloadField(alias='LogServer')
    iis: IisService = PayloadField(alias='Iis')


class SystemStatus(PayloadModel):
    engine_dn: str = PayloadField(alias='engineDn')
    engine_name: str = PayloadField(alias='engineName')
    services: Services = PayloadField(alias='services')
    version: str = PayloadField(alias='version')


class Task(PayloadModel):
    display_name: str = PayloadField(alias='DisplayName')
    name: str = PayloadField(alias='Name')
    start_time: datetime = PayloadField(alias='StartTime')
    stop_time: datetime = PayloadField(alias='StopTime')
    warning_count: int = PayloadField(alias='WarningCount')


class UpgradeInfo(PayloadModel):
    id: str = PayloadField(alias='Id')
    start_time: datetime = PayloadField(alias='StartTime')
    versions: List[str] = PayloadField(alias='Versions')


class UpgradeStatus(PayloadModel):
    engine: 'Engine' = PayloadField(alias='Engine')
    status: str = PayloadField(alias='Status')
    upgrade_start_time: datetime = PayloadField(alias='UpgradeStartTime')
    upgrade_stop_time: datetime = PayloadField(alias='UpgradeStopTime')
    tasks_completed: List[Task] = PayloadField(alias='TasksCompleted')
    tasks_pending: List[Task] = PayloadField(alias='TasksPending')
    tasks_running: List[Task] = PayloadField(alias='TasksRunning')


class UpgradeSummary(PayloadModel):
    status: str = PayloadField(alias='Status')
    upgrade_start_time: datetime = PayloadField(alias='UpgradeStartTime')
    upgrade_stop_time: datetime = PayloadField(alias='UpgradeStopTime')
    completed_tasks: int = PayloadField(alias='CompletedTasks')
    target_version: str = PayloadField(alias='TargetVersion')
    engines_complete: int = PayloadField(alias='EnginesComplete')
    engines_running: int = PayloadField(alias='EnginesRunning')
    engines_blocked: int = PayloadField(alias='EnginesBlocked')
    engines_in_error: int = PayloadField(alias='EnginesInError')
    engines_pending_install: int = PayloadField(alias='EnginesPendingInstall')
