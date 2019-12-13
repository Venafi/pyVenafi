from api.api_base import API, json_response_property


class _Crypto:
    def __init__(self, websdk_obj):
        self.AvailableKeys = self._AvailableKeys(websdk_obj=websdk_obj)
        self.DefaultKey = self._DefaultKey(websdk_obj=websdk_obj)

    class _AvailableKeys(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Crypto/AvailableKeys', valid_return_codes=[200])

        @property
        @json_response_property()
        def keynames(self):
            return self._from_json('Keynames')

        def get(self):
            self.json_response = self._get()
            return self

    class _DefaultKey(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Crypto/DefaultKey', valid_return_codes=[200])

        @property
        @json_response_property()
        def default_key(self):
            return self._from_json('DefaultKey')

        def get(self):
            self.json_response = self._get()
            return self
