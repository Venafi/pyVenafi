from typing import List
from venafi.tools.helpers.date_converter import from_date_string


class SystemStatus:
    class Engine:
        def __init__(self, engine_dict: dict):
            if not isinstance(engine_dict, dict):
                engine_dict = {}
                
            self.dn = engine_dict.get('DN')  # type: str
            self.display_name = engine_dict.get('DisplayName')  # type: str
            self.guid = engine_dict.get('Guid')  # type: str
            self.id = engine_dict.get('Id')  # type: int
            self.name = engine_dict.get('Name')  # type: str
    
    class Services:
        def __init__(self, serv_dict: dict):
            if not isinstance(serv_dict, dict):
                serv_dict = {}

            self.vplatform = SystemStatus.Service(serv_dict.get('vPlatform'))
            self.log_server = SystemStatus.Service(serv_dict.get('logServer'))
            self.iis = SystemStatus.Service(serv_dict.get('iis'))

    class Service:
        def __init__(self, vplat_dict: dict):
            if not isinstance(vplat_dict, dict):
                vplat_dict = {}

            self.modules = vplat_dict.get('modules')  # type: list
            self.time_since_first_seen = from_date_string(vplat_dict.get('timeSinceFirstSeen'))
            self.time_since_last_seen = from_date_string(vplat_dict.get('timeSinceLastSeen'))
            self.status = vplat_dict.get('Status')  # type: str

    class Status:
        def __init__(self, status_dict: dict):
            if not isinstance(status_dict, dict):
                status_dict = {}

            self.engine = SystemStatus.Engine(status_dict.get('Engine'))
            self.status = status_dict.get('Status')  # type: str
            self.upgrade_start_time = from_date_string(status_dict.get('UpgradeStartTime'))
            self.upgrade_stop_time = from_date_string(status_dict.get('UpgradeStopTime'))
            self.tasks_completed = SystemStatus.Task(status_dict.get('TasksCompleted'))
            self.tasks_pending = SystemStatus.Task(status_dict.get('TasksPending'))
            self.tasks_running = SystemStatus.Task(status_dict.get('TasksRunning'))

    class Task:
        def __init__(self, task_dict: dict):
            if not isinstance(task_dict, dict):
                task_dict = {}
                
            self.display_name = task_dict.get('DisplayName')  # type: str
            self.name = task_dict.get('Name')  # type: str
            self.start_time = from_date_string(task_dict.get('StartTime'))
            self.stop_time = from_date_string(task_dict.get('StopTime'))
            self.warning_count = task_dict.get('WarningCount')  # type: int

    class UpgradeInfo:
        def __init__(self, upgrade_info_dict: dict):
            if not isinstance(upgrade_info_dict, dict):
                upgrade_info_dict = {}

            self.id = upgrade_info_dict.get('Id')  # type: str
            self.start_time = from_date_string(upgrade_info_dict.get('StartTime'))
            self.versions = upgrade_info_dict.get('Versions')  # type: List[str]

    class UpgradeSummary:
        def __init__(self, summary_dict: dict):
            if not isinstance(summary_dict, dict):
                summary_dict = {}

            self.status = summary_dict.get('Status')  # type: str
            self.upgrade_start_time = from_date_string(summary_dict.get('UpgradeStartTime'))
            self.upgrade_stop_time = from_date_string(summary_dict.get('UpgradeStopTime'))
            self.completed_tasks = summary_dict.get('CompletedTasks')  # type: int
            self.target_version = summary_dict.get('TargetVersion')  # type: str
            self.engines_complete = summary_dict.get('EnginesComplete')  # type: int
            self.engines_running = summary_dict.get('EnginesRunning')  # type: int
            self.engines_blocked = summary_dict.get('EnginesBlocked')  # type: int
            self.engines_in_error = summary_dict.get('EnginesInError')  # type: int
            self.engines_pending_install = summary_dict.get('EnginesPendingInstall')  # type: int
