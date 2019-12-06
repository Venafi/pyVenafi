from logger import logger, LogLevels
from api.api_base import API, response_property


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
            self._username = None

        @property
        def token(self):
            if self._response.status_code != 200:
                raise AssertionError('Could not authorize user {u} to Aperture API. Received {e}: {m}.'.format(
                    u=self._username, e=self._response.status_code, m=self._response.reason))
            token = "VENAFI " + self._response.json()['apiKey']
            logger.log(msg=f'{self._username} authenticated to Aperture API.', level=LogLevels.api)
            return {'Authorization': token}

        def post(self, username, password):
            self._username = username
            logger.log(msg=f'Authenticating {username}.', level=LogLevels.api)

            body = {
                "username": username,
                "password": password
            }

            self._response = self._post(data=body)
            return self
