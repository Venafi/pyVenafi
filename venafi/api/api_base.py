import re
import json
from venafi.api.session import Session
from requests import Response
from venafi.logger import logger, LogLevels


def json_response_property(return_on_204: type = None):
    """
    This function serves as a decorator for all API response objects. Each
    response property must be validated before returning the object. This
    function depends upon the API class.

    The ``on_204`` parameter suggests what data type is expected to be
    returned when the response status code is valid, but has no content.
    Since there is no content to return, an empty object representing that
    object will be returned instead. For example,

    .. code-block:: python

        # No 204 should ever be returned, so just validate the response
        # status codes and return the object on 200.
        @property
        @json_response_property()
        def value1(self) -> str:
            return self._from_json(key='Value1')

        # 204 could be returned by TPP, so just send an empty response
        # of the same object type as the expected response.
        @property
        @json_response_property(on_204=list)
        def value2(self) -> list:
            return self._from_json(key='Value2')

    Args:
        return_on_204: type

    Returns: Key of response content returned by TPP.

    """
    def pre_validation(func):
        def wrap(self, *args, **kwargs):
            if not self._validated:
                self._validate()
            if return_on_204 and self.json_response.status_code == 204:
                if callable(return_on_204):
                    return return_on_204()
                else:
                    return return_on_204
            return func(self, *args, **kwargs)
        return wrap
    return pre_validation


class API:
    """
    This is the backbone of all API definitions. It performs all requests,
    validations, logging, re-authentication, and holds the raw response. This
    class MUST be inherited by all API definitions.
    """
    def __init__(self, api_obj, url: str, valid_return_codes: list):
        """
        Args:
            api_obj: This is passed down from the API type object (eg. WebSDK, etc.) and
                represents that type. This type is REQUIRED because it contains the
                authenticated sessions, base URL, and re-authentication methods. It is
                through these properties this class is able to send and receive requests
                to TPP.
            url: This is the URL extension from the base URL.
            valid_return_codes: A list of valid status codes, such as [200, 204].
        """
        self._api_obj = api_obj  # type:
        self._session = api_obj._session  # type: Session
        self._api_type = api_obj.__class__.__name__.lower()
        self._url = self._api_obj._base_url + url
        self._valid_return_codes = valid_return_codes

        self._json_response = Response()
        self._validated = False

    @property
    def json_response(self):
        return self._json_response

    @json_response.setter
    def json_response(self, value):
        # When set, a new raw response is stored and hasn't been validated, so invalidate.
        self._validated = False
        self._json_response = value

    def assert_valid_response(self):
        """
        Use this method when no response property is available after an API call or to simply
        throw an error if the return code is invalid. This simply asserts that a valid response
        status code was returned by TPP.
        """
        if not self._validated:
            self._validate()

    def is_valid_response(self):
        """
        Returns ``True`` when the response is valid, meaning a valid return code was returned by
        TPP, otherwise ``False``.
        """
        try:
            self._validate()
            return True
        except InvalidResponseError:
            return False

    def _from_json(self, key: str = None, error_key: str = None, return_on_error: type = None):
        """
        Returns the particular key within the response dictionary. If no key is provided, then
        the full response is returned as a dictionary.

        If ``key`` is provided, then it is searched in the response content. It is not case
        sensitive. If ``key`` is not found, an error is thrown and logged.

        TPP often returns a key with an error message. When an ``error_key`` is provided and an
        error message is returned an error is thrown and logged with the message provided by TPP.

        Args:
            key: Key within the top level of the response content.
            error_key: Error key within the top level of the response content.
            return_on_error: If an error occurs in retrieving content or accessing a key, this
                type will be returned instead of throwing an error.

        Returns:
            If a key is provided, returns the response content at that key. Otherwise, the full
            response content.
        """
        try:
            result = self.json_response.json()
        except json.decoder.JSONDecodeError as e:
            if return_on_error:
                return return_on_error()
            raise InvalidResponseError(f'{self.json_response.url} return no content. '
                                       f'Got status code {self.json_response.status_code}.')
        if error_key and error_key in result.keys():
            raise InvalidResponseError('An error occurred: "%s"' % result[error_key])
        if not key:
            return result
        for k in result.keys():
            if key.lower() == k.lower():
                return result[k]

        if return_on_error:
            return return_on_error()
        raise KeyError(f'{key} was not returned by TPP.')

    def _is_api_key_invalid(self, response: Response):
        """
        Uses a regular expression to search the response text for an indication that the API key
        is expired.

        Args:
            response: The raw response object.

        Returns:
            Returns True if the API key expired. Otherwise False.

        """
        if self._api_type == 'websdk':
            invalid_api_message_match = bool(re.match('.*API key.*is not valid.*', response.text))
        elif self._api_type == 'aperture':
            invalid_api_message_match = bool(re.match('.*The authorization header is incorrect.*', response.text))
        else:
            invalid_api_message_match = False

        return response.status_code == 401 and invalid_api_message_match

    def _delete(self):
        """
        Performs a DELETE method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate using the re-authentication method provided
        by ``api_obj``. Otherwise, the raw response is returned.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call()
        response = self._session.delete(url=self._url)
        self._log_response(response=response)
        if self._is_api_key_invalid(response=response):
            self._re_authenticate()
            return self._delete()
        return response

    def _get(self, params:dict = None):
        """
        Performs a GET method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate using the re-authentication method provided
        by ``api_obj``. Otherwise, the raw response is returned.

        Args:
            params: A dictionary of URL parameters to append to the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(data=params)
        response = self._session.get(url=self._url, params=params)
        self._log_response(response=response)
        if self._is_api_key_invalid(response=response):
            self._re_authenticate()
            return self._get(params=params)
        return response

    def _post(self, data: dict):
        """
        Performs a POST method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate using the re-authentication method provided
        by ``api_obj``. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(data=data)
        response = self._session.post(url=self._url, data=data)
        self._log_response(response=response)
        if self._is_api_key_invalid(response=response):
            self._re_authenticate()
            return self._post(data=data)
        return response

    def _put(self, data: dict):
        """
        Performs a POST method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate using the re-authentication method provided
        by ``api_obj``. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(data=data)
        response = self._session.put(url=self._url, data=data)
        self._log_response(response=response)
        if self._is_api_key_invalid(response=response):
            self._re_authenticate()
            return self._put(data)
        return response

    def _validate(self):
        """
        Validates the current response property by validating that there are expected return codes
        and that the actual return code is one of the valid return codes. If the return code is
        invalid, an error is thrown and logged.
        """
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
        """
        The current API token expired and the session needs to be re-authenticated.
        """
        logger.log(
            msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            level=LogLevels.low.level
        )
        self._api_obj.re_authenticate()
        self._session = self._api_obj._session

    def _log_rest_call(self, data: dict = None):
        """
        Logs the URL and any additional data. This enforces consistency in logging across all API calls.
        """
        if data:
            payload = json.dumps(data, indent=4)
            logger.log(f'URL: {self._url}\nPARAMETERS: {payload}', level=LogLevels.low.level, prev_frames=3)
        else:
            logger.log(f'URL: {self._url}', level=LogLevels.low.level, prev_frames=3)

    def _log_response(self, response: Response):
        """
        Logs the URL, response code, and the content returned by TPP.
        This enforces consistency in logging across all API calls.
        """
        try:
            pretty_json = json.dumps(response.json(), indent=4)
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        logger.log(
            msg=f'URL: "{self._url}"\nRESPONSE CODE: {response.status_code}\nCONTENT: {pretty_json}',
            level=LogLevels.low.level,
            prev_frames=3
        )


class InvalidResponseError(Exception):
    pass
