import json
from venafi.logger import logger, LogLevels
from venafi.api.api_base import API, json_response_property


class _Authorize(API):
    def __init__(self, websdk_obj):
        super().__init__(
            api_obj=websdk_obj,
            url='/Authorize',
            valid_return_codes=[200]
        )

    @property
    @json_response_property()
    def token(self) -> dict:
        logger.log('WebSDK API Key retrieved.', level=LogLevels.low.level)
        token = self.json_response.json()['APIKey']
        return {'X-Venafi-API-Key': token}

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        body = {
            "Username": username,
            "Password": password
        }

        self.json_response = self._post(data=body)
        return self
