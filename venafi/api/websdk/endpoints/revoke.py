from api.api_base import API


class _Revoke:
    def __init__(self, websdk_obj):
        self.Token = self._Token(websdk_obj=websdk_obj)

    class _Token(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Revoke/Token', valid_return_codes=[200])
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            self.json_response = self._get()
            return self
