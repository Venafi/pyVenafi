from venafi.api.api_base import API, json_response_property


class _Users:
    def __init__(self, aperture_obj):
        self.Authorize = self._Authorize(aperture_obj=aperture_obj)

    class _Authorize(API):
        def __init__(self, aperture_obj):
            super().__init__(
                api_obj=aperture_obj,
                url='/users/authorize',
                valid_return_codes=[200]
            )

        @property
        @json_response_property()
        def token(self) -> dict:
            return self._from_json('apiKey')

        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": password
            }
            self._log_rest_call(
                method='POST',
                data=body,
                mask_values_with_key=[
                    'password'
                ],
                prev_frames=2
            )
            self.json_response = self._session.post(url=self._url, data=body)
            self._log_response(
                response=self.json_response,
                mask_values_with_key=[
                    'apiKey'
                ],
                prev_frames=2
            )
            return self
