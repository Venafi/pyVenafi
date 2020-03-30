from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.system_status import SystemStatus
from venafi.tools.helpers.date_converter import from_date_string


class _SystemStatus(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/SystemStatus', valid_return_codes=[200])
        self.Upgrade = self._Upgrade(websdk_obj=websdk_obj)
        self.Version = self._Version(websdk_obj=websdk_obj)

    @property
    @json_response_property()
    def engine_name(self) -> str:
        return self.json_response('engineName')

    @property
    @json_response_property()
    def services(self):
        return SystemStatus.Services(self.json_response('services'))

    @property
    @json_response_property()
    def version(self) -> str:
        return self.json_response('version')

    def get(self):
        self.json_response = self._get()
        return self

    class _Upgrade:
        def __init__(self, websdk_obj):
            self.Engine = self._Engine(websdk_obj=websdk_obj)
            self.Engines = self._Engines(websdk_obj=websdk_obj)
            self.History = self._History(websdk_obj=websdk_obj)
            self.Status = self._Status(websdk_obj=websdk_obj)
            self.Summary = self._Summary(websdk_obj=websdk_obj)

        class _Engine(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Engine', valid_return_codes=[200])

            @property
            @json_response_property()
            def engine(self):
                return SystemStatus.Engine(self._from_json(key='Engine'))

            @property
            @json_response_property()
            def status(self) -> str:
                return self._from_json(key='Status')
            
            @property
            @json_response_property()
            def upgrade_start_time(self):
                return from_date_string(self._from_json(key='UpgradeStartTime'))
            
            @property
            @json_response_property()
            def upgrade_stop_time(self):
                return from_date_string(self._from_json(key='UpgradeStopTime'))
            
            @property
            @json_response_property()
            def tasks_completed(self):
                return [SystemStatus.Task(task) for task in self._from_json(key='TasksCompleted')]

            @property
            @json_response_property()
            def tasks_pending(self):
                return [SystemStatus.Task(task) for task in self._from_json(key='TasksPending')]

            @property
            @json_response_property()
            def tasks_running(self):
                return [SystemStatus.Task(task) for task in self._from_json(key='TasksRunning')]

            def get(self, guid: str, engine_id: str, upgrade_id: str = None):
                params = {
                    'guid': guid,
                    'Id': engine_id,
                    'UpgradeId': upgrade_id
                }

                self.json_response = self._get(params=params)
                return self

        class _Engines(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Engines', valid_return_codes=[200])

            @property
            @json_response_property()
            def engines(self):
                return [SystemStatus.Status(engine) for engine in self._from_json(key='Engines')]

            def get(self, upgrade_id: int = None):
                params = {
                    'UpgradeId': upgrade_id
                }

                self.json_response = self._get(params=params)
                return self

        class _History(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/History', valid_return_codes=[200])

            @property
            @json_response_property()
            def upgrade_history(self):
                return [SystemStatus.UpgradeInfo(info) for info in self._from_json(key='UpgradeHistory')]

            def get(self):
                self.json_response = self._get()
                return self

        class _Status(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Status', valid_return_codes=[200])

            @property
            @json_response_property()
            def upgrade_in_progress(self) -> bool:
                return self._from_json(key='UpgradeInProgress')

            def get(self):
                self.json_response = self._get()
                return self

        class _Summary(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Summary', valid_return_codes=[200])

            @property
            @json_response_property()
            def upgrade_summary(self):
                return SystemStatus.UpgradeSummary(self._from_json(key='UpgradeSummary'))

            def get(self):
                self.json_response = self._get()
                return self

    class _Version(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SystemStatus/Version', valid_return_codes=[200])

        @property
        @json_response_property()
        def version(self) -> str:
            return self.json_response('Version')

        def get(self):
            self.json_response = self._get()
            return self
