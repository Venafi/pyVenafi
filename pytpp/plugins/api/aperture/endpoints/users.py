import logging
from pytpp.plugins.api.api_base import API, APIResponse, api_response_property
from pytpp.tools.logger import api_logger


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
                def __init__(self, r, api_source):
                    super().__init__(response=r, api_source=api_source)

                @property
                @api_response_property()
                def token(self) -> dict:
                    return self._from_json('apiKey')

            api_logger.debug(f'Authenticating to Aperture as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated as "{username}"!')
            return _Response(response, api_source=self._api_source)
