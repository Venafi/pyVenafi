from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List


class Engine(PayloadModel):
    dn: str = PayloadField(alias='Dn', default=None)
    display_name: str = PayloadField(alias='DisplayName', default=None)
    guid: str = PayloadField(alias='Guid', default=None)
    id: int = PayloadField(alias='Id', default=None)
    name: str = PayloadField(alias='Name', default=None)


class Services(PayloadModel):
    vplatform: 'Service' = PayloadField(alias='Vplatform', default=None)
    log_server: 'Service' = PayloadField(alias='LogServer', default=None)
    iis: 'Service' = PayloadField(alias='Iis', default=None)


class Service(PayloadModel):
    modules: list = PayloadField(alias='Modules', default=None)
    time_since_first_seen: datetime = PayloadField(alias='TimeSinceFirstSeen', default=None)
    time_since_last_seen: datetime = PayloadField(alias='TimeSinceLastSeen', default=None)
    status: str = PayloadField(alias='Status', default=None)


class SystemStatus(PayloadModel):
    engine_name: str = PayloadField(alias='EngineName', default=None)
    services: 'Services' = PayloadField(alias='Services', default=None)
    version: str = PayloadField(alias='Version', default=None)


class Task(PayloadModel):
    display_name: str = PayloadField(alias='DisplayName', default=None)
    name: str = PayloadField(alias='Name', default=None)
    start_time: datetime = PayloadField(alias='StartTime', default=None)
    stop_time: datetime = PayloadField(alias='StopTime', default=None)
    warning_count: int = PayloadField(alias='WarningCount', default=None)


class UpgradeInfo(PayloadModel):
    id: str = PayloadField(alias='Id', default=None)
    start_time: datetime = PayloadField(alias='StartTime', default=None)
    versions: List[str] = PayloadField(alias='Versions', default=None)


class UpgradeStatus(PayloadModel):
    engine: 'Engine' = PayloadField(alias='Engine', default=None)
    status: str = PayloadField(alias='Status', default=None)
    upgrade_start_time: datetime = PayloadField(alias='UpgradeStartTime', default=None)
    upgrade_stop_time: datetime = PayloadField(alias='UpgradeStopTime', default=None)
    tasks_completed: 'List[Task]' = PayloadField(alias='TasksCompleted', default=None)
    tasks_pending: 'List[Task]' = PayloadField(alias='TasksPending', default=None)
    tasks_running: 'List[Task]' = PayloadField(alias='TasksRunning', default=None)


class UpgradeSummary(PayloadModel):
    status: str = PayloadField(alias='Status', default=None)
    upgrade_start_time: datetime = PayloadField(alias='UpgradeStartTime', default=None)
    upgrade_stop_time: datetime = PayloadField(alias='UpgradeStopTime', default=None)
    completed_tasks: int = PayloadField(alias='CompletedTasks', default=None)
    target_version: str = PayloadField(alias='TargetVersion', default=None)
    engines_complete: int = PayloadField(alias='EnginesComplete', default=None)
    engines_running: int = PayloadField(alias='EnginesRunning', default=None)
    engines_blocked: int = PayloadField(alias='EnginesBlocked', default=None)
    engines_in_error: int = PayloadField(alias='EnginesInError', default=None)
    engines_pending_install: int = PayloadField(alias='EnginesPendingInstall', default=None)
