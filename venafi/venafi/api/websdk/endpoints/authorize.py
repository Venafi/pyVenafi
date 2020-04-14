import json
from venafi.logger import logger, LogLevels
from venafi.api.api_base import API, json_response_property


class _Authorize(API):
    def __init__(self, websdk_obj):
        super().__init__(
            api_obj=websdk_obj,
            url='/Authorize',
            valid_return_codes=[200]
        )

        self.OAuth = self._OAuth(websdk_obj=websdk_obj)
        self.Token = self._Token(websdk_obj=websdk_obj)

    @property
    @json_response_property()
    def token(self) -> str:
        return self._from_json('APIKey')

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        self._log_api_deprecated_warning(alternate_api=self.OAuth._url)
        body = {
            "Username": username,
            "Password": password
        }
        self._log_rest_call(
            method='POST',
            data=body,
            mask_values_with_key=[
                'Password'
            ],
            prev_frames=2
        )
        self.json_response = self._session.post(url=self._url, data=body)
        self._log_response(
            response=self.json_response,
            mask_values_with_key=[
                'APIKey'
            ],
            prev_frames=2
        )
        return self

    class _OAuth(API):
        def __init__(self, websdk_obj):
            super().__init__(
                api_obj=websdk_obj,
                url='/Authorize/OAuth',
                valid_return_codes=[200]
            )
            self._url = self._url.replace('vedsdk', 'vedauth')

        @property
        @json_response_property()
        def access_token(self) -> str:
            return self._from_json('access_token')

        @property
        @json_response_property()
        def expires(self) -> str:
            return self._from_json('expires')

        @property
        @json_response_property()
        def identity(self) -> str:
            return self._from_json('identity')

        @property
        @json_response_property()
        def refresh_token(self) -> str:
            return self._from_json('refresh_token')

        @property
        @json_response_property()
        def scope(self) -> str:
            return self._from_json('scope')

        @property
        @json_response_property()
        def token_type(self) -> str:
            return self._from_json('token_type')

        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password': password,
                'scope': scope,
                'username': username,
                'state': state
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
                    'access_token',
                    'refresh_token'
                ],
                prev_frames=2
            )
            return self

    class _Token(API):
        def __init__(self, websdk_obj):
            super().__init__(
                api_obj=websdk_obj,
                url='/Authorize/Token',
                valid_return_codes=[200]
            )
            self._url = self._url.replace('vedsdk', 'vedauth')

        @property
        @json_response_property()
        def access_token(self) -> str:
            return self._from_json('access_token')

        @property
        @json_response_property()
        def expires(self) -> str:
            return self._from_json('expires')

        @property
        @json_response_property()
        def refresh_token(self) -> str:
            return self._from_json('refresh_token')

        @property
        @json_response_property()
        def refresh_until(self) -> str:
            return self._from_json('refresh_until')

        @property
        @json_response_property()
        def scope(self) -> str:
            return self._from_json('scope')

        @property
        @json_response_property()
        def token_type(self) -> str:
            return self._from_json('token_type')

        def post(self, client_id: str, refresh_token: str):
            body = {
                'client_id': client_id,
                'refresh_token': refresh_token
            }

            self._log_rest_call(
                method='POST',
                data=body,
                mask_values_with_key=[
                    'refresh_token'
                ],
                prev_frames=2
            )
            self.json_response = self._session.post(url=self._url, data=body)
            self._log_response(
                response=self.json_response,
                mask_values_with_key=[
                    'access_token',
                    'refresh_token'
                ],
                prev_frames=2
            )
            return self
