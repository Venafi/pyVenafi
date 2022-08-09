import logging
from pytpp.api.api_base import ResponseFactory, ResponseField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.tools.logger import api_logger


class _Users:
    def __init__(self, api_obj):
        self.Authorize = self._Authorize(api_obj=api_obj)
        self.Current = self._Current(api_obj=api_obj)

    class _Authorize(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/users/authorize')

        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": password
            }

            class Response(ApertureResponse):
                token: str = ResponseField(alias='apiKey')

            api_logger.debug(f'Authenticating to Aperture as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = ResponseFactory(response_cls=Response, response=self._post(data=body))
            api_logger.debug(f'Authenticated as "{username}"!')
            return response

    class _Current:
        def __init__(self, api_obj):
            self.Logout = self._Logout(api_obj=api_obj)

        class _Logout(ApertureEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/users/current/logout')

            def post(self):
                body = {}

                response = ResponseFactory(response_cls=ApertureResponse, response=self._post(data=body))
                # Set this to None to avoid erroneous re-authentication.
                self._api_obj._token = None
                return response
