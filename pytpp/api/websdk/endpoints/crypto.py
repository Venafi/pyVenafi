from typing import List
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _Crypto:
    def __init__(self, api_obj):
        self.AvailableKeys = self._AvailableKeys(api_obj=api_obj)
        self.DefaultKey = self._DefaultKey(api_obj=api_obj)

    class _AvailableKeys(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/AvailableKeys')

        def get(self):
            class Response(APIResponse):
                keynames: List[str] = ResponseField(alias='Keynames', default_factory=list)

            return ResponseFactory(response=self._get(), response_cls=Response)

    class _DefaultKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/DefaultKey')

        def get(self):
            class Response(APIResponse):
                default_key: str = ResponseField(alias='DefaultKey')

            return ResponseFactory(response=self._get(), response_cls=Response)
