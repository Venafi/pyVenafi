from logger import logger, LogLevels
from api.api_base import API, response_property


class _Authorize(API):
    def __init__(self, websdk_obj):
        super().__init__(
            api_obj=websdk_obj,
            url='/Authorize',
            valid_return_codes=[200]
        )
        self._username = None

    @property
    @response_property()
    def token(self):
        if self._response.status_code != 200:
            raise AssertionError('Could not authorize user {u} to WebSDK. Received {e}: {m}.'.format(
                u=self._username, e=self._response.status_code, m=self._response.reason))
        token = self._response.json()['APIKey']
        logger.log(msg=f'{self._username} authenticated to WebSDK.', level=LogLevels.api)
        return {'X-Venafi-API-Key': token}

    def post(self, username, password):
        self._username = username
        logger.log(msg=f'Authenticating {username}.', level=LogLevels.api)

        body = {
            "Username": username,
            "Password": password
        }

        self._response = self._post(data=body)
        return self
