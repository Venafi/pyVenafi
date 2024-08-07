from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)

class _ServerStatus(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/ServerStatus')
        self.Idle = self._Idle(api_obj=self._api_obj, url=f'{self._url}/Idle')
        self.Active = self._Active(api_obj=self._api_obj, url=f'{self._url}/Active')

    class _Idle(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                pass

            return generate_output(output_cls=Output, response=self._get())

    class _Active(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                pass

            return generate_output(output_cls=Output, response=self._get())
