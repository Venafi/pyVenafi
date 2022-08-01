from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Engine(PayloadModel):
    dn: str = PayloadField(alias='Dn')
    display_name: str = PayloadField(alias='DisplayName')
    guid: str = PayloadField(alias='Guid')
    id: int = PayloadField(alias='Id')
    name: str = PayloadField(alias='Name')


class Services(PayloadModel):
    vplatform: 'Service' = PayloadField(alias='Vplatform')
    log_server: 'Service' = PayloadField(alias='LogServer')
    iis: 'Service' = PayloadField(alias='Iis')


class Service(PayloadModel):
    modules: list = PayloadField(alias='Modules')
    time_since_first_seen: datetime = PayloadField(alias='TimeSinceFirstSeen')
    time_since_last_seen: datetime = PayloadField(alias='TimeSinceLastSeen')
    status: str = PayloadField(alias='Status')


class SystemStatus(PayloadModel):
    engine_name: str = PayloadField(alias='EngineName')
    services: 'Services' = PayloadField(alias='Services')
    version: str = PayloadField(alias='Version')


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
    tasks_completed: 'List[Task]' = PayloadField(alias='TasksCompleted')
    tasks_pending: 'List[Task]' = PayloadField(alias='TasksPending')
    tasks_running: 'List[Task]' = PayloadField(alias='TasksRunning')


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
