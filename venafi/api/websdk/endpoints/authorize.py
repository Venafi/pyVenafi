import json
from logger import logger, LogLevels
from api.api_base import API, response_property


class _Authorize(API):
    def __init__(self, websdk_obj):
        super().__init__(
            api_obj=websdk_obj,
            url='/Authorize',
            valid_return_codes=[200]
        )

    @property
    @response_property()
    def token(self):
        logger.log('WebSDK API Key retrieved.', level=LogLevels.api)
        token = self._response.json()['APIKey']
        return {'X-Venafi-API-Key': token}

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        body = {
            "Username": username,
            "Password": '********'
        }

        payload = json.dumps(body, indent=4)
        logger.log(f'URL: {self._url}\nPARAMETERS: {payload}', level=LogLevels.api)

        body['Password'] = password
        self.response = self._session.post(url=self._url, data=body)

        return self
