from pytpp.plugins.api.api_base import API, APIResponse, json_response_property


class _Users:
    def __init__(self, api_obj):
        self.Authorize = self._Authorize(api_obj=api_obj)

    class _Authorize(API):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url='/users/authorize'
            )

        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": password
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def token(self) -> dict:
                    return self._from_json('apiKey')

            return _Response(
                response=self._post(data=body),
                api_source=self._api_source)
