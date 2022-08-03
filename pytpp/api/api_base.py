import re
import json
import time
from pydantic.fields import Undefined
from requests import Response, HTTPError
from pydantic import BaseModel, root_validator, Field
from pytpp.tools.logger import api_logger, json_pickler
from typing import Any, Optional, Union, Protocol, TYPE_CHECKING, Type, TypeVar
if TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny, NoArgAnyCallable
    from pytpp.api.session import Session


T_ = TypeVar('T_')


def api_response_property(return_on_204: type = None):
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
        @api_response_property()
        def value1(self) -> str:
            return self._from_json(key='Value1')

        # 204 could be returned by TPP, so just send an empty response
        # of the same object type as the expected response.
        @property
        @api_response_property(on_204=list)
        def value2(self) -> list:
            return self._from_json(key='Value2')

    Args:
        return_on_204: type

    Returns: Key of response content returned by TPP.

    """

    def pre_validation(func):
        def wrap(self: APIResponse, *args, **kwargs):
            if not self._validated:
                self._validate()
            if return_on_204 and self.api_response.status_code == 204:
                if callable(return_on_204):
                    return return_on_204()
                else:
                    return return_on_204
            return func(self, *args, **kwargs)

        return wrap

    return pre_validation


class APISource(Protocol):
    _host: str
    _username: str
    _password: str
    _token: str
    _base_url: str
    _session: 'Session'

    def re_authenticate(self): ...


class API:
    """
    This is the backbone of all API definitions. It performs all requests,
    validations, logging, re-authentication, and holds the raw response. This
    class MUST be inherited by all API definitions.
    """

    def __init__(self, api_obj, url: str):
        """
        Args:
            api_obj: This is passed down from the API type object (eg. WebSDK, etc.) and
                represents that type. This type is REQUIRED because it contains the
                authenticated sessions, base URL, and re-authentication methods. It is
                through these properties this class is able to send and receive requests
                to TPP.
            url: This is the URL extension from the base URL.
        """
        self._api_obj: 'APISource' = api_obj
        if not url.startswith('/'):
            url = '/' + url
        self._url = self._api_obj._base_url + url
        self._retries = 3
        self.retry_interval = 0.5

    @property
    def retries(self):
        return self._retries + 1  # The first time isn't a "retry".

    @property
    def _session(self) -> 'Session':
        return self._api_obj._session

    def _should_re_authenticate(self, response: 'Response'):
        return response.status_code == 401 and self._api_obj._token is not None

    @staticmethod
    def _rerun_transaction_required(response: Response):
        """
        Uses a regular expression to search the response text for an indication that the transaction was deadlocked
        and needs to be reran.

        Args:
            response: The raw response object.

        Returns:
            Returns ``True`` if the API key expired. Otherwise ``False``.
        """
        return response.status_code == 500 and bool(re.match('.*rerun the transaction.*', response.text,
                                                             flags=re.IGNORECASE))

    def _delete(self, params: dict = None):
        """
        Performs a DELETE method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='DELETE', data=params)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.delete(url=self._url, params=params)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _get(self, params: dict = None):
        """
        Performs a GET method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            params: A dictionary of URL parameters to append to the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='GET', data=params)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.get(url=self._url, params=params)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _post(self, data: Union[list, dict]):
        """
        Performs a POST method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='POST', data=data)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.post(url=self._url, data=data)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _put(self, data: Union[list, dict]):
        """
        Performs a PUT method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='PUT', data=data)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.put(url=self._url, data=data)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _re_authenticate(self):
        """
        The current API token expired and the session needs to be re-authenticated.
        """
        api_logger.debug(
            f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            stacklevel=2
        )
        self._api_obj.re_authenticate()

    def _log_api_deprecated_warning(self, alternate_api: str = None):
        msg = f'API DEPRECATION WARNING: {self._url} is no longer supported by Venafi.'
        if alternate_api:
            msg += f'\nUse {alternate_api} instead.'
        api_logger.warning(msg, stacklevel=2)

    def _log_rest_call(self, method: str, data: dict = None):
        """
        Logs the URL and any additional data. This enforces consistency in logging across all API calls.
        """
        if data:
            payload = json_pickler.dumps(data)
            api_logger.debug(
                f'{method}\nURL: {self._url}\nBODY: {payload}',
                stacklevel=2
            )
        else:
            api_logger.debug(
                msg=f'{method}\nURL: {self._url}',
                stacklevel=2
            )

    def _log_response(self, response: Response):
        """
        Logs the URL, response code, and the content returned by TPP.
        This enforces consistency in logging across all API calls.
        """
        try:
            pretty_json = json_pickler.dumps(response.json())
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        api_logger.debug(
            msg=f'URL: "{self._url}"\nRESPONSE CODE: {response.status_code}\nCONTENT: {pretty_json}',
            stacklevel=2
        )


def ResponseField(
        default: Any = None,
        *,
        default_factory: 'Optional[NoArgAnyCallable]' = None,
        alias: str = None,
        title: str = None,
        description: str = None,
        exclude: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None,
        include: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None,
        const: bool = None,
        gt: float = None,
        ge: float = None,
        lt: float = None,
        le: float = None,
        multiple_of: float = None,
        max_digits: int = None,
        decimal_places: int = None,
        min_items: int = None,
        max_items: int = None,
        unique_items: bool = None,
        min_length: int = None,
        max_length: int = None,
        allow_mutation: bool = True,
        regex: str = None,
        discriminator: str = None,
        repr: bool = True,
        **extra: Any,
) -> Any:
    """

    Returns:
        object:
    """
    if callable(default_factory):
        default = Undefined
    return Field(
        default=default,
        default_factory=default_factory,
        alias=alias,
        title=title,
        description=description,
        exclude=exclude,
        include=include,
        const=const,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        multiple_of=multiple_of,
        max_digits=max_digits,
        decimal_places=decimal_places,
        min_items=min_items,
        max_items=max_items,
        unique_items=unique_items,
        min_length=min_length,
        max_length=max_length,
        allow_mutation=allow_mutation,
        regex=regex,
        discriminator=discriminator,
        repr=repr,
        **extra
    )


def ResponseFactory(response: Response, response_cls: Type[T_], root_field: str = None) -> T_:
    """
    Args:
        response: Response instance returned by the ``requests`` call to the server.
        response_cls: Custom APIResponse class.
        root_field: In the case that the returned JSON is an array of objects, then the ``root_field``
            is used to assign that value.

    Returns:
        An instance of ``response_cls``.
    """
    try:
        result = response.json()
    except:
        result = {}
    if not isinstance(result, dict):
        if not root_field:
            raise AttributeError('Unable to assign ')
        result = {
            str(root_field): result
        }
    response_inst = response_cls(api_response=response, **result)
    try:
        response.raise_for_status()
        if isinstance(result, dict) and (error_key := getattr(response_inst, 'error', 'Unknown')) in result.keys():
            raise InvalidResponseError('An error occurred: "%s"' % result[error_key], response=response)
        return response_inst
    except HTTPError as error:
        if isinstance(result, dict) and (error_msg := getattr(response_inst, 'error', None)) is not None:
            raise InvalidResponseError(f'An error occurred: "{error_msg}"', response=response) from error
        raise InvalidResponseError(str(error), response=response)


class APIResponse(BaseModel):
    api_response: Response
    error: str = ResponseField(default=None, alias='Error')

    class Config:
        arbitrary_types_allowed = True

    @root_validator(pre=True, allow_reuse=True)
    def _case_insensitive_validator(cls, values: dict):
        new_values = {}
        lowered_values = {k.lower(): v for k, v in values.items()}
        for fk, fv in cls.__fields__.items():
            try:
                if fk.lower() not in lowered_values:
                    continue
                new_value = lowered_values.get(fk.lower())
                if (converter := fv.field_info.extra.get('converter')) is not None:
                    new_value = converter(new_value)
                new_values[fv.alias] = new_value
            except KeyError:
                raise KeyError(f'"{fk}" not found in the response.')
        return new_values

    def assert_valid_response(self):
        """
        Use this method when no response property is available after an API call or to simply
        throw an error if the return code is invalid. This simply asserts that a valid response
        status code was returned by TPP.
        """
        self.api_response.raise_for_status()

    def is_valid_response(self):
        """
        Returns ``True`` when the response is valid, meaning a valid return code was returned by
        TPP, otherwise ``False``.
        """
        try:
            self.api_response.raise_for_status()
            return True
        except:
            return False


# class APIResponse:
#     def __init__(self, response: Response):
#         self._api_response = response
#         self._validated = False
#
#     @property
#     def api_response(self):
#         return self._api_response
#
#     @api_response.setter
#     def api_response(self, value):
#         # When set, a new raw response is stored and hasn't been validated, so invalidate.
#         self._validated = False
#         self._api_response = value
#
#     def assert_valid_response(self):
#         """
#         Use this method when no response property is available after an API call or to simply
#         throw an error if the return code is invalid. This simply asserts that a valid response
#         status code was returned by TPP.
#         """
#         if not self._validated:
#             self._validate()
#
#     def is_valid_response(self):
#         """
#         Returns ``True`` when the response is valid, meaning a valid return code was returned by
#         TPP, otherwise ``False``.
#         """
#         try:
#             self._validate()
#             return True
#         except:
#             return False
#
#     def _from_json(self, key: str = None, error_key: str = None, return_on_error: type = None):
#         """
#         Returns the particular key within the response dictionary. If no key is provided, then
#         the full response is returned as a dictionary.
#
#         If ``key`` is provided, then it is searched in the response content. It is not case
#         sensitive. If ``key`` is not found, an error is thrown and logged.
#
#         TPP often returns a key with an error message. When an ``error_key`` is provided and an
#         error message is returned an error is thrown and logged with the message provided by TPP.
#
#         Args:
#             key: Key within the top level of the response content.
#             error_key: Error key within the top level of the response content.
#             return_on_error: If an error occurs in retrieving content or accessing a key, this
#                 type will be returned instead of throwing an error.
#
#         Returns:
#             If a key is provided, returns the response content at that key. Otherwise, the full
#             response content.
#         """
#         try:
#             result = self.api_response.json()
#         except json.decoder.JSONDecodeError:
#             if return_on_error:
#                 return return_on_error()
#             raise InvalidResponseError(f'{self.api_response.url} return no content. '
#                                        f'Got status code {self.api_response.status_code}.')
#         if error_key and error_key in result.keys():
#             raise InvalidResponseError('An error occurred: "%s"' % result[error_key])
#         if not key:
#             return result
#         try:
#             return result[key]
#         except KeyError:
#             # Try avoiding case-sensitive typos and search by lower-case comparison.
#             for k in result.keys():
#                 if key.lower() == k.lower():
#                     return result[k]
#
#         if return_on_error:
#             return return_on_error()
#         raise KeyError(f'{key} was not returned by TPP.')
#
#     def _validate(self):
#         """
#         Validates the current response property by validating that there are expected return codes
#         and that the actual return code is one of the valid return codes. If the return code is
#         invalid, an error is thrown and logged.
#         """
#         self._validated = True
#         try:
#             self.api_response.raise_for_status()
#         except HTTPError as err:
#             error_msg = self.api_response.text or self.api_response.reason or 'No error message found.'
#             body = json_pickler.dumps(
#                 json.loads(err.request.body)
#             ) if err.request.body else ''
#             error_msg = '\n'.join(err.args) + f"\nERROR: {error_msg}\nCONTENT: {body}"
#             raise InvalidResponseError(error_msg)


class InvalidResponseError(Exception):
    def __init__(self, msg: str, response: Response):
        self.response = response
        super().__init__(msg)
