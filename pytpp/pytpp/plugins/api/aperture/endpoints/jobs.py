from pytpp.plugins.api.api_base import API, APIResponse


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

            class _Actions(API):
                def __init__(self, guid: str, api_obj):
                    super().__init__(
                        api_obj=api_obj,
                        url=f'/jobs/networkdiscovery/{guid}/actions'
                    )

                def post(self, job_action: str):
                    body = {
                        'jobAction': job_action
                    }

                    return APIResponse(response=self._post(data=body), api_source=self._api_source)
