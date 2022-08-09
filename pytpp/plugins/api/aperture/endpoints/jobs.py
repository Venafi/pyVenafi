from pytpp.api.api_base import ResponseFactory
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse


class _Jobs:
    def __init__(self, api_obj):
        self.NetworkDiscovery = self._NetworkDiscovery(api_obj)

    class _NetworkDiscovery:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid:
            def __init__(self, guid: str, api_obj):
                self._api_obj = api_obj
                self.Actions = self._Actions(guid=guid, api_obj=api_obj)

            class _Actions(ApertureEndpoint):
                def __init__(self, guid: str, api_obj):
                    super().__init__(
                        api_obj=api_obj,
                        url=f'/jobs/networkdiscovery/{guid}/actions'
                    )

                def post(self, job_action: str):
                    body = {
                        'jobAction': job_action
                    }

                    return ResponseFactory(response_cls=ApertureResponse, response=self._post(data=body))
