from pytpp.api.api_base import generate_output
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel


class _Jobs(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/jobs')
        self.NetworkDiscovery = self._NetworkDiscovery(api_obj=self._api_obj, url=f'{self._url}/networkdiscovery')

    class _NetworkDiscovery(ApertureEndpoint):
        def Guid(self, guid: str):
            return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(ApertureEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.Actions = self._Actions(api_obj=self._api_obj, url=f'{self._url}/actions')

            class _Actions(ApertureEndpoint):
                def post(self, job_action: str):
                    body = {
                        'jobAction': job_action
                    }

                    return generate_output(output_cls=ApertureOutputModel, response=self._post(data=body))
