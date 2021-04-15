from typing import List
from pytpp.tools.helpers.date_converter import from_date_string


class SystemStatus:
    class Engine:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.dn = response_object.get('DN')  # type: str
            self.display_name = response_object.get('DisplayName')  # type: str
            self.guid = response_object.get('Guid')  # type: str
            self.id = response_object.get('Id')  # type: int
            self.name = response_object.get('Name')  # type: str

    class Services:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.vplatform = SystemStatus.Service(response_object.get('vPlatform'))
            self.log_server = SystemStatus.Service(response_object.get('logServer'))
            self.iis = SystemStatus.Service(response_object.get('iis'))

    class Service:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.modules = response_object.get('modules')  # type: list
            self.time_since_first_seen = from_date_string(response_object.get('timeSinceFirstSeen'),
                                                          duration_format=True)
            self.time_since_last_seen = from_date_string(response_object.get('timeSinceLastSeen'), duration_format=True)
            self.status = response_object.get('Status')  # type: str

    class SystemStatus:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.engine_name = response_object.get('engineName')  # type: str
            self.services = SystemStatus.Services(response_object.get('services'))
            self.version = response_object.get('version')  # type: str

    class Task:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.display_name = response_object.get('DisplayName')  # type: str
            self.name = response_object.get('Name')  # type: str
            self.start_time = from_date_string(response_object.get('StartTime'))
            self.stop_time = from_date_string(response_object.get('StopTime'))
            self.warning_count = response_object.get('WarningCount')  # type: int

    class UpgradeInfo:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.id = response_object.get('Id')  # type: str
            self.start_time = from_date_string(response_object.get('StartTime'))
            self.versions = response_object.get('Versions')  # type: List[str]

    class UpgradeStatus:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.engine = SystemStatus.Engine(response_object.get('Engine'))
            self.status = response_object.get('Status')  # type: str
            self.upgrade_start_time = from_date_string(response_object.get('UpgradeStartTime'))
            self.upgrade_stop_time = from_date_string(response_object.get('UpgradeStopTime'))
            self.tasks_completed = [SystemStatus.Task(t) for t in response_object.get('TasksCompleted', [])]
            self.tasks_pending = [SystemStatus.Task(t) for t in response_object.get('TasksPending', [])]
            self.tasks_running = [SystemStatus.Task(t) for t in response_object.get('TasksRunning', [])]

    class UpgradeSummary:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.status = response_object.get('Status')  # type: str
            self.upgrade_start_time = from_date_string(response_object.get('UpgradeStartTime'))
            self.upgrade_stop_time = from_date_string(response_object.get('UpgradeStopTime'))
            self.completed_tasks = response_object.get('CompletedTasks')  # type: int
            self.target_version = response_object.get('TargetVersion')  # type: str
            self.engines_complete = response_object.get('EnginesComplete')  # type: int
            self.engines_running = response_object.get('EnginesRunning')  # type: int
            self.engines_blocked = response_object.get('EnginesBlocked')  # type: int
            self.engines_in_error = response_object.get('EnginesInError')  # type: int
            self.engines_pending_install = response_object.get('EnginesPendingInstall')  # type: int
