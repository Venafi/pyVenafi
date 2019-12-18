import re
import json
from venafi.api.session import Session
from requests import Response
from venafi.logger import logger, LogLevels


def json_response_property(on_204=None):
    def pre_validation(func):
        def wrap(self, *args, **kwargs):
            if not self._validated:
                    self._validate()
            if on_204 and self.response.status_code == 204:
                if callable(on_204):
                    return on_204()
                else:
                    return on_204
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

        self._json_response = Response()
        self._validated = False

    @property
    def json_response(self):
        return self._json_response

    @json_response.setter
    def json_response(self, value):
        self._validated = False
        self._json_response = value

    def assert_valid_response(self):
        if not self._validated:
            self._validate()

    def _from_json(self, key: str = None, error_key: str = None):
        result = self.json_response.json()
        if error_key and error_key in result.keys():
            raise InvalidResponseError('An error occurred: "%s"' % result[error_key])
        if not key:
            return result
        for k in result.keys():
            if key.lower() == k.lower():
                return result[k]

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
            return self._post(data=data)
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

        if not isinstance(self.json_response, Response):
            raise TypeError("Expected response object, but got %s." % type(self.json_response))

        if self.json_response.status_code not in self._valid_return_codes:
            error_msg = self.json_response.text or self.json_response.reason or 'No error message found.'
            raise InvalidResponseError("Received %s, but expected one of %s. Error message is: %s" % (
                self.json_response.status_code, str(self._valid_return_codes), error_msg))

    def _re_authenticate(self):
        logger.log(
            msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            level=LogLevels.api
        )
        self._api_obj.re_authenticate()

    def _log_rest_call(self, data: dict = None):
        if data:
            payload = json.dumps(data, indent=4)
            logger.log(f'URL: {self._url}\nPARAMETERS: {payload}', level=LogLevels.api, prev_frames=3)
        else:
            logger.log(f'URL: {self._url}', level=LogLevels.api, prev_frames=3)

    def _log_response(self, response: Response):
        try:
            pretty_json = json.dumps(response.json(), indent=4)
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        logger.log(
            msg=f'URL: "{self._url}"\nRESPONSE CODE: {response.status_code}\nCONTENT: {pretty_json}',
            level=LogLevels.api,
            prev_frames=3
        )


class InvalidResponseError(Exception):
    pass
