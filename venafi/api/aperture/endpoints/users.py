from logger import logger, LogLevels
from api.session import APERTURE_URL
from api.session import Session


class _Users:
    def __init__(self, aperture_obj):
        self.Authorize = self._Authorize()

    class _Authorize:
        def __init__(self):
            self._session = Session({'Content-Type': 'application/json', 'Referer': APERTURE_URL.rstrip('/api')})
            self._url = APERTURE_URL + '/users/authorize'
            self._response = None
            self._username = None

        @property
        def token(self):
            if self._response.status_code != 200:
                raise AssertionError('Could not authorize user. Received {e}: {m}.'.format(e=self._response.status_code, m=self._response.reason))
            token = "VENAFI " + self._response.json()['apiKey']
            logger.log(msg=f'{self._username} authenticated.', level=LogLevels.api)
            return {
                'Authorization': token,
                'Content-Type': 'application/json',
                'Referer': APERTURE_URL.rstrip('/api')
            }

        def post(self, username, password):
            self._username = username
            logger.log(msg=f'Authenticating {username}.', level=LogLevels.api)

            body = {
                "username": username,
                "password": password
            }

            self._response = self._session.post(url=self._url, data=body)
            return self
