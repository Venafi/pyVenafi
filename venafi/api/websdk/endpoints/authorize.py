from logger import logger, LogLevels
from api.session import WEBSDK_URL
from api.session import Session


class _Authorize:
    def __init__(self):
        self._session = Session({'Content-Type': 'application/json'})
        self._url = WEBSDK_URL + '/Authorize'
        self._response = None
        self._username = None

    @property
    def token(self):
        if self._response.status_code != 200:
            raise AssertionError('Could not authorize user. Received {e}: {m}.'.format(e=self._response.status_code, m=self._response.reason))
        token = self._response.json()['APIKey']
        logger.log(msg=f'{self._username} authenticated.', level=LogLevels.api)
        return {
            'X-Venafi-API-Key': token,
            'Content-Type': 'application/json'
        }

    def post(self, username, password):
        self._username = username
        logger.log(msg=f'Authenticating {username}.', level=LogLevels.api)

        body = {
            "Username": username,
            "Password": password
        }

        self._response = self._session.post(url=self._url, data=body)
        return self
