from datetime import datetime
from typing import List
from pytpp.api.websdk.outputs import system_status
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _SystemStatus(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SystemStatus')
        self.Upgrade = self._Upgrade(api_obj=api_obj)
        self.Version = self._Version(api_obj=api_obj)

    def get(self):
        class Output(WebSdkOutputModel):
            engines: List[system_status.SystemStatus] = ApiField(default_factory=list)

        return generate_output(output_cls=Output, response=self._get(), root_field='engines')

    class _Upgrade:
        def __init__(self, api_obj):
            self.Engine = self._Engine(api_obj=api_obj)
            self.Engines = self._Engines(api_obj=api_obj)
            self.History = self._History(api_obj=api_obj)
            self.Status = self._Status(api_obj=api_obj)
            self.Summary = self._Summary(api_obj=api_obj)

        class _Engine(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engine')

            def get(self, guid: str, engine_id: str, upgrade_id: str = None):
                params = {
                    'guid'     : guid,
                    'Id'       : engine_id,
                    'UpgradeId': upgrade_id
                }

                class Output(WebSdkOutputModel):
                    engine: system_status.Engine = ApiField(alias='Engine')
                    status: str = ApiField(alias='Status')
                    upgrade_start_time: datetime = ApiField(alias='UpgradeStartTime')
                    upgrade_stop_time: datetime = ApiField(alias='UpgradeStopTime')
                    tasks_completed: List[system_status.Task] = ApiField(default_factory=list, alias='TasksCompleted')
                    tasks_pending: List[system_status.Task] = ApiField(default_factory=list, alias='TasksPending')
                    tasks_running: List[system_status.Task] = ApiField(default_factory=list, alias='TasksRunning')

                return generate_output(output_cls=Output, response=self._get(params=params))

        class _Engines(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Engines')

            def get(self, upgrade_id: int = None):
                params = {
                    'UpgradeId': upgrade_id
                }

                class Output(WebSdkOutputModel):
                    engines: List[system_status.UpgradeStatus] = ApiField(default_factory=list, alias='Engines')

                return generate_output(output_cls=Output, response=self._get(params=params))

        class _History(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/History')

            def get(self):
                class Output(WebSdkOutputModel):
                    upgrade_history: List[system_status.UpgradeInfo] = ApiField(default_factory=list, alias='UpgradeHistory')

                return generate_output(output_cls=Output, response=self._get())

        class _Status(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Status')

            def get(self):
                class Output(WebSdkOutputModel):
                    upgrade_in_progress: bool = ApiField(alias='UpgradeInProgress')

                return generate_output(output_cls=Output, response=self._get())

        class _Summary(WebSdkEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SystemStatus/Upgrade/Summary')

            def get(self):
                class Output(WebSdkOutputModel):
                    upgrade_summary: system_status.UpgradeSummary = ApiField(alias='UpgradeSummary')

                return generate_output(output_cls=Output, response=self._get())

    class _Version(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SystemStatus/Version')

        def get(self):
            class Output(WebSdkOutputModel):
                version: str = ApiField(alias='Version')

            return generate_output(response=self._get(), output_cls=Output)
