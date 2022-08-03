from datetime import datetime
from typing import List

from properties.response_objects.dataclasses import system_status
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _SystemStatus(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SystemStatus')
        self.Upgrade = self._Upgrade(api_obj=api_obj)
        self.Version = self._Version(api_obj=api_obj)

    def get(self):
        class Response(APIResponse):
            engines: List[system_status.SystemStatus] = ResponseField(default_factory=list)

        return ResponseFactory(response_cls=Response, response=self._get(), root_field='engines')

    class _Upgrade:
        def __init__(self, api_obj):
            self.Engine = self._Engine(api_obj=api_obj)
            self.Engines = self._Engines(api_obj=api_obj)
            self.History = self._History(api_obj=api_obj)
            self.Status = self._Status(api_obj=api_obj)
            self.Summary = self._Summary(api_obj=api_obj)

        class _Engine(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engine')

            def get(self, guid: str, engine_id: str, upgrade_id: str = None):
                params = {
                    'guid'     : guid,
                    'Id'       : engine_id,
                    'UpgradeId': upgrade_id
                }

                class Response(APIResponse):
                    engine: system_status.Engine = ResponseField(alias='Engine')

                    status: str = ResponseField(alias='Status')
                    upgrade_start_time: datetime = ResponseField(alias='UpgradeStartTime')

                    upgrade_stop_time: datetime = ResponseField(alias='UpgradeStopTime')

                    tasks_completed: List[system_status.Task] = ResponseField(default_factory=list, alias='TasksCompleted') 
                    tasks_pending: List[system_status.Task] = ResponseField(default_factory=list, alias='TasksPending') 
                    tasks_running: List[system_status.Task] = ResponseField(default_factory=list, alias='TasksRunning') 

                return ResponseFactory(response_cls=Response, response=self._get(params=params))

        class _Engines(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engines')

            def get(self, upgrade_id: int = None):
                params = {
                    'UpgradeId': upgrade_id
                }

                class Response(APIResponse):
                    engines: List[system_status.UpgradeStatus] = ResponseField(default_factory=list, alias='Engines') 

                return ResponseFactory(response_cls=Response, response=self._get(params=params))

        class _History(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/History')

            def get(self):
                class Response(APIResponse):
                    upgrade_history: List[system_status.UpgradeInfo] = ResponseField(default_factory=list, alias='UpgradeHistory') 

                return ResponseFactory(response_cls=Response, response=self._get())

        class _Status(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Status')

            def get(self):
                class Response(APIResponse):
                    upgrade_in_progress: bool = ResponseField(alias='UpgradeInProgress')

                return ResponseFactory(response_cls=Response, response=self._get())

        class _Summary(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Summary')

            def get(self):
                class Response(APIResponse):
                    upgrade_summary: system_status.UpgradeSummary = ResponseField(alias='UpgradeSummary')

                return ResponseFactory(response_cls=Response, response=self._get())

    class _Version(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SystemStatus/Version')

        def get(self):
            class Response(APIResponse):
                version: str = ResponseField(alias='Version')

            return ResponseFactory(response=self._get(), response_cls=Response)
