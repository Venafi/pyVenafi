from pytpp.api.api_base import WebSdkEndpoint, WebSdkResponse, ResponseFactory


class _Revoke:
    def __init__(self, api_obj):
        self.Token = self._Token(api_obj=api_obj)

    class _Token(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Revoke/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            response = ResponseFactory(response_cls=WebSdkResponse, response=self._get())
            # Set this to None to avoid erroneous re-authentication.
            self._api_obj._token = None
            return response
