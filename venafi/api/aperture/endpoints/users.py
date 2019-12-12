from api.api_base import API, response_property
from logger import logger, LogLevels
import json


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

        @property
        @response_property()
        def token(self):
            logger.log('Aperture API Key retrieved.', level=LogLevels.api)
            token = "VENAFI " + self._response.json()['apiKey']
            return {'Authorization': token}

        def post(self, username, password):
            """
            This POST method is written differently in order to effectively omit the password from being logged.
            """
            body = {
                "username": username,
                "password": '********'
            }

            payload = json.dumps(body, indent=4)
            logger.log(f'URL: {self._url}\nPARAMETERS: {payload}', level=LogLevels.api)

            body['password'] = password
            self.response = self._session.post(url=self._url, data=body)

            return self
