from venafi.api.api_base import API, APIResponse


class _Jobs:
    def __init__(self, aperture_obj):
        self.NetworkDiscovery = self._NetworkDiscovery(aperture_obj)

    class _NetworkDiscovery:
        def __init__(self, aperture_obj):
            self._aperture_obj = aperture_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, aperture_obj=self._aperture_obj)

        class _Guid:
            def __init__(self, guid: str, aperture_obj):
                self._aperture_obj = aperture_obj
                self.Actions = self._Actions(guid=guid, aperture_obj=aperture_obj)

            class _Actions(API):
                def __init__(self, guid: str, aperture_obj):
                    super().__init__(
                        api_obj=aperture_obj,
                        url=f'/jobs/networkdiscovery/{guid}/actions'
                    )

                def post(self, job_action: str):
                    body = {
                        'jobAction': job_action
                    }

                    return APIResponse(
                        response=self._post(data=body),
                        expected_return_codes=[200],
                        api_source=self._api_source
                    )
