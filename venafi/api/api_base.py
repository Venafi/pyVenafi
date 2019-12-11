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
        self._log_rest_call()
        response = self._api_obj.session.delete(url=self._url)
        self._log_response(response=response)
        if self._is_api_key_valid(response=response):
            self._re_authenticate()
            return self._delete()
        return response

    def _get(self, params:dict = None):
        self._log_rest_call(data=params)
        response = self._api_obj.session.get(url=self._url, params=params)
        self._log_response(response=response)
        if self._is_api_key_valid(response=response):
            self._re_authenticate()
            return self._get(params=params)
        return response

    def _post(self, data: dict):
        self._log_rest_call(data=data)
        response = self._api_obj.session.post(url=self._url, data=data)
        self._log_response(response=response)
        if self._is_api_key_valid(response=response):
            self._re_authenticate()
            result = self._api_obj.session.post(url=self._url, data=data)
        return response

    def _put(self, data: dict):
        self._log_rest_call(data=data)
        response = self._api_obj.session.put(url=self._url, data=data)
        self._log_response(response=response)
        if self._is_api_key_valid(response=response):
            self._re_authenticate()
            return self._put(data)
        return response

    def _validate(self):
        self._validated = True

        if not self._valid_return_codes:
            raise ValueError('No valid return codes were provided, so the response to %s cannot be validated.' % self._url)

        if not isinstance(self.response, Response):
            raise TypeError("Expected response object, but got %s." % type(self.response))

        if self.response.status_code not in self._valid_return_codes:
            error_msg = self.response.text or self.response.reason or 'No error message found.'
            raise InvalidResponseError("Received %s, but expected one of %s. Error message is: %s" % (
                self.response.status_code, str(self._valid_return_codes), json.dumps(error_msg, indent=4)))

    def _re_authenticate(self):
        logger.log(
            msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            level=LogLevels.api
        )
        self._api_obj.re_authenticate()

    def _log_rest_call(self, data: dict = None):
        if data:
            payload = json.dumps(data, indent=4)
            logger.log(f'{self._url}: {payload}', level=LogLevels.api, prev_frames=3)
        else:
            logger.log(self._url, level=LogLevels.api, prev_frames=3)

    def _log_response(self, response: Response):
        try:
            pretty_json = json.dumps(response.json(), indent=4)
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        logger.log(
            msg=f'Response to {self._url} is {response.status_code}: {pretty_json}',
            level=LogLevels.api,
            prev_frames=3
        )


class InvalidResponseError(Exception):
    pass
