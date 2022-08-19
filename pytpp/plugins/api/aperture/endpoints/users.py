import logging
from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.tools.logger import api_logger


class _Users(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/users')
        self.Authorize = self._Authorize(api_obj=self._api_obj, url=f'{self._url}/authorize')
        self.Current = self._Current(api_obj=self._api_obj, url=f'{self._url}/current')

    class _Authorize(ApertureEndpoint):
        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": password
            }

            class Output(ApertureOutputModel):
                token: str = ApiField(alias='apiKey')

            api_logger.debug(f'Authenticating to Aperture as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = generate_output(output_cls=Output, response=self._post(data=body))
            api_logger.debug(f'Authenticated as "{username}"!')
            return response

    class _Current(ApertureEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Logout = self._Logout(api_obj=self._api_obj, url=f'{self._url}/logout')

        class _Logout(ApertureEndpoint):
            def post(self):
                body = {}

                response = generate_output(output_cls=ApertureOutputModel, response=self._post(data=body))
                # Set this to None to avoid erroneous re-authentication.
                self._api_obj._token = None
                return response
