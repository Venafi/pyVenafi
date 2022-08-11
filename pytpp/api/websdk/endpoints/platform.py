from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Platform:
    def __init__(self, api_obj):
        self.Delete = self._Delete(api_obj=api_obj)

    class _Delete(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Platform/Delete')

        def post(self, platform: str):
            body = {
                'Platform': platform
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output=Output)
