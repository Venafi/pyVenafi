from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _Platform:
    def __init__(self, api_obj):
        self.Delete = self._Delete(api_obj=api_obj)

    class _Delete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Platform/Delete')

        def post(self, platform: str):
            body = {
                'Platform': platform
            }

            class Response(APIResponse):
                success: bool = ResponseField(alias='Success')

            return ResponseFactory(response=self._post(data=body), response_cls=Response)
