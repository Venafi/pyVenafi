from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property


class _Crypto:
    def __init__(self, websdk_obj):
        self.AvailableKeys = self._AvailableKeys(websdk_obj=websdk_obj)
        self.DefaultKey = self._DefaultKey(websdk_obj=websdk_obj)

    class _AvailableKeys(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Crypto/AvailableKeys')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def keynames(self) -> List[str]:
                    return self._from_json('Keynames')

            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _DefaultKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Crypto/DefaultKey')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def default_key(self) -> str:
                    return self._from_json('DefaultKey')

            return _Response(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )
