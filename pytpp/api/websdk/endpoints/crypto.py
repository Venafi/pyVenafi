from typing import List
from pytpp.api.api_base import WebSdkEndpoint, WebSdkResponse, ResponseFactory, ResponseField


class _Crypto:
    def __init__(self, api_obj):
        self.AvailableKeys = self._AvailableKeys(api_obj=api_obj)
        self.DefaultKey = self._DefaultKey(api_obj=api_obj)

    class _AvailableKeys(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/AvailableKeys')

        def get(self):
            class Response(WebSdkResponse):
                keynames: List[str] = ResponseField(alias='Keynames', default_factory=list)

            return ResponseFactory(response=self._get(), response_cls=Response)

    class _DefaultKey(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/DefaultKey')

        def get(self):
            class Response(WebSdkResponse):
                default_key: str = ResponseField(alias='DefaultKey')

            return ResponseFactory(response=self._get(), response_cls=Response)
