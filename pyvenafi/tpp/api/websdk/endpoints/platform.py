from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)

class _Platform(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Platform')
        self.Delete = self._Delete(api_obj=self._api_obj, url=f'{self._url}/Delete')

    class _Delete(WebSdkEndpoint):
        def post(self, platform: str):
            body = {
                'Platform': platform
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)
