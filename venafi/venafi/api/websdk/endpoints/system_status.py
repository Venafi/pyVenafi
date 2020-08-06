from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.system_status import SystemStatus
from venafi.tools.helpers.date_converter import from_date_string

class _SystemStatus(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/SystemStatus')
        self.Upgrade = self._Upgrade(websdk_obj=websdk_obj)
        self.Version = self._Version(websdk_obj=websdk_obj)

    def get(self):
        class _Response(APIResponse):
            def __init__(self, response, expected_return_codes, api_source):
                super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

            @property
            @json_response_property()
            def engines(self):
                return [SystemStatus.SystemStatus(status) for status in self._from_json()]

        return _Response(
            response=self._get(),
            expected_return_codes=[200],
            api_source=self._api_source
        )

    class _Upgrade:
        def __init__(self, websdk_obj):
            self.Engine = self._Engine(websdk_obj=websdk_obj)
            self.Engines = self._Engines(websdk_obj=websdk_obj)
            self.History = self._History(websdk_obj=websdk_obj)
            self.Status = self._Status(websdk_obj=websdk_obj)
            self.Summary = self._Summary(websdk_obj=websdk_obj)

        class _Engine(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Engine')

            def get(self, guid: str, engine_id: str, upgrade_id: str = None):
                params = {
                    'guid': guid,
                    'Id': engine_id,
                    'UpgradeId': upgrade_id
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

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

                return _Response(
                    response=self._get(params=params),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Engines(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Engines')

            def get(self, upgrade_id: int = None):
                params = {
                    'UpgradeId': upgrade_id
                }

                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def engines(self):
                        return [SystemStatus.UpgradeStatus(engine) for engine in self._from_json(key='Engines')]

                return _Response(
                    response=self._get(params=params),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _History(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/History')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def upgrade_history(self):
                        return [SystemStatus.UpgradeInfo(info) for info in self._from_json(key='UpgradeHistory')]

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Status(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Status')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def upgrade_in_progress(self) -> bool:
                        return self._from_json(key='UpgradeInProgress')

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

        class _Summary(API):
            def __init__(self, websdk_obj):
                super().__init__(api_obj=websdk_obj, url='/SystemStatus/Upgrade/Summary')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, expected_return_codes, api_source):
                        super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                    @property
                    @json_response_property()
                    def upgrade_summary(self):
                        return SystemStatus.UpgradeSummary(self._from_json(key='UpgradeSummary'))

                return _Response(
                    response=self._get(),
                    expected_return_codes=[200],
                    api_source=self._api_source
                )

    class _Version(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SystemStatus/Version')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def version(self) -> str:
                    return self._from_json('Version')

            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )
