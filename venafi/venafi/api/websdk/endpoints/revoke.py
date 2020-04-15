from venafi.api.api_base import API, APIResponse


class _Revoke:
    def __init__(self, websdk_obj):
        self.Token = self._Token(websdk_obj=websdk_obj)

    class _Token(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Revoke/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            self._log_api_deprecated_warning()

            return APIResponse(
                response=self._get(),
                expected_return_codes=[200],
                api_source=self._api_source
            )
