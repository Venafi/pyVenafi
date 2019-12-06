import re
import json
from api.session import Session
from requests import Response
from logger import logger, LogLevels


def response_property():
    def pre_validation(func):
        def wrap(self, *args, **kwargs):
            if not self._validated:
                    self._validate()
            return func(self, *args, **kwargs)
        return wrap
    return pre_validation


class API:
    def __init__(self, api_obj, url, valid_return_codes):
        self._api_obj = api_obj
        self._session = api_obj.session  # type: Session
        self._api_type = api_obj.__class__.__name__.lower()
        self._url = self._api_obj.base_url + url
        self._valid_return_codes = valid_return_codes

        self._response = Response()
        self._validated = False

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._validated = False
        self._response = value

    def json_response(self, key: str = None, error_key: str = None):
        result = self.response.json()
        if error_key and error_key in result.keys():
            raise InvalidResponseError('An error occurred: "%s"' % result[error_key])
        value = result if not key else result[key]
        return value

    def _is_api_key_valid(self, response=None):
        if self._api_type == 'websdk':
             invalid_api_message_match = bool(re.match('.*API key.*is not valid.*', response.text))
        elif self._api_type == 'aperture':
            invalid_api_message_match = bool(re.match('.*The authorization header is incorrect.*', response.text))
        else:
            invalid_api_message_match = False

        return response.status_code == 401 and invalid_api_message_match

    def _delete(self):
        result = self._api_obj.session.delete(url=self._url)
        if self._is_api_key_valid(response=result):
            logger.log(
                msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
                level=LogLevels.api
            )
            self._api_obj.re_authenticate()
            return self._delete()
        logger.log(self._url, level=LogLevels.api, prev_frames=2)
        return result

    def _get(self, params:dict = None):
        result = self._api_obj.session.get(url=self._url, params=params)
        if self._is_api_key_valid(response=result):
            logger.log(
                msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
                level=LogLevels.api
            )
            self._api_obj.re_authenticate()
            return self._get(params=params)
        if params:
            pretty_params = json.dumps(params, indent=4)
            logger.log(f'{self._url}: {pretty_params}', level=LogLevels.api, prev_frames=2)
        else:
            logger.log(self._url, level=LogLevels.api, prev_frames=2)
        return result

    def _post(self, data):
        result = self._api_obj.session.post(url=self._url, data=data)
        if self._is_api_key_valid(response=result):
            logger.log(
                msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
                level=LogLevels.api
            )
            self._api_obj.re_authenticate()
            result = self._api_obj.session.post(url=self._url, data=data)
        payload = json.dumps(data, indent=4)
        logger.log(f'{self._url}: {payload}', level=LogLevels.api, prev_frames=2)
        return result

    def _put(self, data):
        payload = json.dumps(data, indent=4)
        result = self._api_obj.session.put(url=self._url, data=data)
        if self._is_api_key_valid(response=result):
            logger.log(
                msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
                level=LogLevels.api
            )
            self._api_obj.re_authenticate()
            return self._put(data)
        logger.log(f'{self._url}: {payload}', level=LogLevels.api, prev_frames=2)
        return result

    def _validate(self):
        self._validated = True

        if not self._valid_return_codes:
            raise ValueError('No valid return codes were provided, so the response to %s cannot be validated.' % self._url)

        if not isinstance(self.response, Response):
            raise TypeError("Expected response object, but got %s." % type(self.response))

        if self.response.status_code not in self._valid_return_codes:
            raise InvalidResponseError("Received %s, but expected one of %s. Error message is: %s" % (
                self.response.status_code, str(self._valid_return_codes), json.dumps(self.response.text, indent=4)))

        pretty_json = json.dumps(self.response.json(), indent=4)
        logger.log(
            msg=f'Response to {self._url} is valid. Got {self.response.status_code}: {pretty_json}',
            level=LogLevels.api
        )


class InvalidResponseError(Exception):
    pass
