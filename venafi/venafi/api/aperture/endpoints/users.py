from venafi.api.api_base import API, APIResponse, json_response_property


class _Users:
    def __init__(self, aperture_obj):
        self.Authorize = self._Authorize(aperture_obj=aperture_obj)

    class _Authorize(API):
        def __init__(self, aperture_obj):
            super().__init__(
                api_obj=aperture_obj,
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
            self._log_rest_call(
                method='POST',
                data=body,
                mask_values_with_key=[
                    'password'
                ],
                prev_frames=2
            )
            r = self._post(data=body)
            self._log_response(
                response=r,
                mask_values_with_key=[
                    'apiKey'
                ],
                prev_frames=2
            )

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def token(self) -> dict:
                    return self._from_json('apiKey')

            return _Response(
                response=r,
                expected_return_codes=[200],
                api_source=self._api_source
            )
