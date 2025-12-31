import json
import re
import time
from datetime import datetime
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Union,
    Protocol,
    TYPE_CHECKING,
    Type,
    TypeVar,
    get_origin,
    get_args,
    Literal,
)

from pydantic import (
    BaseModel,
    Field, model_validator, ConfigDict, types,
)
from pydantic import create_model
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.fields import PydanticUndefined, FieldInfo
from requests import (
    Response,
    HTTPError,
)

from pyvenafi.logger import (
    api_logger,
    json_pickler,
)
from pyvenafi.tpp import DN

if TYPE_CHECKING:
    from pydantic.typing import (
        AbstractSetIntStr,
        MappingIntStrAny,
        NoArgAnyCallable,
    )

T_ = TypeVar('T_')

class ApiModelMetaclass(ModelMetaclass):
    def __new__(mcs, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(getattr(base, '__annotations__', {}))
        for field in annotations:
            if not field.startswith('__') and get_origin(annotations[field]) is not Union:
                annotations[field] = Union[annotations[field], Any]
        namespaces['__annotations__'] = annotations
        return super().__new__(mcs, name, bases, namespaces, **kwargs)

# region Endpoint Definitions
class ApiSource(Protocol):
    _host: str
    _username: str
    _password: str
    _api_key: str
    _base_url: str
    _app_url: str
    _scheme: str
    _session: 'Session'

    def re_authenticate(self): ...

class ApiEndpoint(object):
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
        self._api_obj: 'CloudApi' = api_obj
        url = url.strip('/')
        if url.startswith(self._api_obj._base_url):
            self._url = url
        else:
            self._url = f'{self._api_obj._app_url}/{url}'
        self._retries = 3
        self.retry_interval = 0.5

    @property
    def retries(self):
        return self._retries + 1  # The first time isn't a "retry".

    @property
    def _session(self) -> 'Session':
        return self._api_obj._session

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
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _patch(self, data: Union[list, dict]):
        """
        Performs a PUT method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='PATCH', data=data)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.patch(url=self._url, data=data)
                self._log_response(response=response)
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
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

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
            payload = json_pickler.dumps(self._session._sanitize(data))
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

class CloudApiEndpoint(ApiEndpoint):
    ...

# endregion Endpoint Definitions


# region Model And Field Definitions
def ApiField(
    default: Any = None,
    *,
    default_factory: 'Optional[NoArgAnyCallable]' = None,
    alias: str = None,
    alias_priority: int = None,
    allow_inf_nan: bool = None,
    coerce_numbers_to_str: bool = None,
    decimal_places: int = None,
    deprecated: bool = None,
    description: str = None,
    discriminator: str | types.Discriminator = None,
    examples: list[Any] = None,
    exclude: bool = None,
    fail_fast: bool = None,
    field_title_generator: Callable[[str, FieldInfo], str] = None,
    frozen: bool = None,
    ge: float = None,
    gt: float = None,
    init: bool = None,
    init_var: bool = None,
    kw_only: bool = None,
    le: float = None,
    lt: float = None,
    max_digits: int = None,
    max_length: int = None,
    min_length: int = None,
    multiple_of: float = None,
    pattern: str = None,
    repr: bool = None,
    serialization_alias: str = None,
    strict: bool = None,
    title: str = None,
    union_mode: Literal['smart', 'left_to_right'] = PydanticUndefined,
    validate_default: bool = None,
    validation_alias: str = None,
    converter: Callable[[Any], Any] = None,
    **json_schema_extra: Any
) -> Any:
    if converter is not None and callable(converter):
        json_schema_extra['converter'] = converter
    kwargs = dict(
        alias=alias,
        alias_priority=alias_priority,
        allow_inf_nan=allow_inf_nan,
        coerce_numbers_to_str=coerce_numbers_to_str,
        decimal_places=decimal_places,
        deprecated=deprecated,
        description=description,
        discriminator=discriminator,
        examples=examples,
        exclude=exclude,
        fail_fast=fail_fast,
        field_title_generator=field_title_generator,
        frozen=frozen,
        ge=ge,
        gt=gt,
        init=init,
        init_var=init_var,
        kw_only=kw_only,
        le=le,
        lt=lt,
        max_digits=max_digits,
        max_length=max_length,
        min_length=min_length,
        multiple_of=multiple_of,
        pattern=pattern,
        repr=repr,
        serialization_alias=serialization_alias,
        strict=strict,
        title=title,
        union_mode=union_mode,
        validate_default=validate_default,
        validation_alias=validation_alias,
        json_schema_extra=json_schema_extra,
    )
    if callable(default_factory):
        return Field(
            default_factory=default_factory,
            **kwargs,
        )
    else:
        return Field(
            default=default,
            **kwargs,
        )


# region Output Models
def generate_output(
    response: Response, output_cls: Type[T_], root_field: str = None,
    rc_mapping: Dict[int, str] = None
) -> T_:
    """
    Args:
        response: Response instance returned by the ``requests`` call to the server.
        output_cls: Custom APIResponse class.
        root_field: In the case that the returned JSON is an array of objects, then the ``root_field``
            is used to assign that value.
        rc_mapping: Used to map return codes to root_fields.

    Returns:
        An instance of ``response_cls``.
    """
    try:
        result = response.json()
    except:
        result = {}
    if not isinstance(result, dict):
        result = {
            str(root_field): result
        } if root_field else {}
    elif root_field:
        result = {
            str(root_field): result,
            **result
        }
    elif rc_mapping and (field := rc_mapping.get(response.status_code)) is not None:
        result = {
            str(field): result,
            **result
        }
    response_inst = output_cls(api_response=response, **result)
    try:
        response.raise_for_status()
        if isinstance(result, dict) and (error_key := getattr(response_inst, 'error', 'Unknown')) in result.keys():
            # There is an error message, but the status is a valid status, so just log the error instead.
            api_logger.error('An error occurred: "%s"' % result[error_key], response=response)
        return response_inst
    except HTTPError as error:
        if isinstance(result, dict) and (error_msg := getattr(response_inst, 'error', None)) is not None:
            raise InvalidResponseError(f'An error occurred: "{error_msg}"', response=response) from error
        raise InvalidResponseError(str(error), response=response)

class ObjectModel(BaseModel, metaclass=ApiModelMetaclass):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_by_name=True,
        json_encoders={
            DN: lambda x: str(x)
        }
    )

    @model_validator(mode='before')
    @classmethod
    def _case_insensitive_validator(cls, values: dict):
        new_values = {}
        lowered_values = {k.lower(): v for k, v in values.items()}
        for fk, fv in cls.model_fields.items():
            new_key = fk
            if fk in values:
                new_value = values[fk]
            elif fv.alias is not None and fv.alias.lower() in lowered_values:
                new_key = fv.alias
                new_value = lowered_values[fv.alias.lower()]
            else:
                continue
            type_args = get_args(fv.annotation)
            if not type_args:
                type_args = (fv.annotation,)
            if datetime in type_args and isinstance(new_value, str) and '/Date' in new_value:
                new_value = re.sub(r'\D', '', new_value)
            elif DN in type_args:
                new_value = DN(new_value)
            if (converter := fv.json_schema_extra.get('converter')) is not None:
                new_value = converter(new_value)
            new_values[new_key] = new_value
        return new_values

    def with_extra_properties(self, **kwargs) -> 'ObjectModel':
        d = self.__dict__
        d.update(kwargs)
        return create_model(
            f'New{self.__class__.__name__}',
            __base__=self.__class__,  # noqa
            __module__=self.__module__,
            **d
        )()

class RootOutputModel(ObjectModel):
    api_response: Response = ApiField(alias='api_response', exclude=True)

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

class CloudApiOutputModel(RootOutputModel):
    error: str = ApiField(alias='Error')

# endregion Output Models


class InvalidResponseError(Exception):
    def __init__(self, msg: str, response: Response):
        self.response = response
        super().__init__(msg, response)
# endregion Response Definitions
