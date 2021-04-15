from pytpp.api.api_base import API, APIResponse, json_response_property


class _Authorize(API):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url='/Authorize'
        )

        self.OAuth = self._OAuth(api_obj=api_obj)
        self.Token = self._Token(api_obj=api_obj)

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        self._log_api_deprecated_warning(alternate_api=self.OAuth._url)
        body = {
            "Username": username,
            "Password": password
        }

        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @json_response_property()
            def token(self) -> str:
                return self._from_json('APIKey')

        return _Response(
            response=self._post(data=body, mask_input_regexes=['Password'], mask_output_regexes=['APIKey']))

    class _OAuth(API):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url='/Authorize/OAuth'
            )
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password': password,
                'scope': scope,
                'username': username,
                'state': state
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

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

            return _Response(
                response=self._post(data=body, mask_input_regexes=['password'], mask_output_regexes=['*token*']))

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url='/Authorize/Token'
            )
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, refresh_token: str):
            body = {
                'client_id': client_id,
                'refresh_token': refresh_token
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

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

            return _Response(
                response=self._post(data=body, mask_input_regexes=['token'], mask_output_regexes=['*token*']))
