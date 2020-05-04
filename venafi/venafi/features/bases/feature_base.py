import inspect
import time
from venafi.logger import logger, LogTags
from venafi.properties.secret_store import Namespaces
from venafi.api.authenticate import Authenticate
from typing import List, Dict


def feature():
    def decorate(cls):
        for attr, fn in inspect.getmembers(cls, inspect.isroutine):
            # Only public methods are decorated.
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('_'):
                if type(cls.__dict__.get(fn.__name__)) in {staticmethod, classmethod}:
                    setattr(cls, attr, logger.wrap_func(
                        log_tag=LogTags.feature,
                        is_static_or_classmethod=True
                    )(getattr(cls, attr)))
                else:
                    setattr(cls, attr, logger.wrap_func(log_tag=LogTags.feature)(getattr(cls, attr)))
        return cls
    return decorate


@feature()
class FeatureBase:
    def __init__(self, auth: Authenticate):
        self._auth = auth

        self._log_not_implemented_warning = self.__log_not_implemented_warning if auth._suppress_not_implemented_warning else self.__no_op

    def _config_create(self, name: str, parent_folder_dn: str, config_class: str, attributes: dict = None):
        if attributes:
            attributes = self._name_value_list(attributes=attributes)

        dn = f'{parent_folder_dn}\\{name}'

        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ca = self._auth.websdk.Config.Create.post(object_dn=dn, class_name=config_class, name_attribute_list=attributes or [])

        result = ca.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return ca.object

    def _config_delete(self, object_dn, recursive: bool = False):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self._auth.websdk.Config.Delete.post(object_dn=object_dn, recursive=recursive).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    @staticmethod
    def _log_warning_message(msg: str):
        logger.log(msg=msg, log_tag=LogTags.critical, num_prev_callers=2)

    @staticmethod
    def __log_not_implemented_warning(api_type):
        logger.log(f'No implementation defined for this method using {api_type}.', log_tag=LogTags.feature,
                   num_prev_callers=2)

    @staticmethod
    def __no_op(*args, **kwargs):
        pass

    @staticmethod
    def _name_type_value(name: str, type: str, value):
        return {'Name': str(name), 'Type': str(type), 'Value': str(value)}

    @staticmethod
    def _name_value_list(attributes: Dict[str, List[str]], keep_list_values: bool = False):
        nvl = []
        for name, value in attributes.items():
            if value is None:
                continue
            elif isinstance(value, list):
                if keep_list_values is True:
                    nvl.append({'Name': str(name), 'Value': value})
                else:
                    for v in value:
                        nvl.append({'Name': str(name), 'Value': str(v)})
            elif not isinstance(value, dict):
                nvl.append({'Name': str(name), 'Value': str(value)})
        return nvl

    def _secret_store_delete(self, object_dn: str, namespace: str = Namespaces.config):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        owners = self._auth.websdk.SecretStore.LookupByOwner.post(namespace=namespace, owner=object_dn)
        result = owners.result
        if result.code != 0:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

        for vault_id in owners.vault_ids:
            result = self._auth.websdk.SecretStore.Delete.post(vault_id=vault_id).result
            if result.code != 0:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

    class _Timeout:
        def __init__(self, timeout):
            self.timeout = timeout
            self.max_time = timeout + time.time()

        def __enter__(self):
            logger.set_rule(
                log_tag=LogTags.feature,
                min_tag_value=LogTags.feature.value,
                why=f'Disabling all logs during timeout to reduce redundant logging.'
            )
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            logger.set_rule(
                log_tag=LogTags.feature,
                reset=True,
                why=f'Enabling all logs after timeout.'
            )
            return

        def is_expired(self, poll: float = 0.5):
            time.sleep(poll)
            return time.time() >= self.max_time


class _FeatureException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def log(self):
        logger.log(
            msg=self.__str__(),
            log_tag=LogTags.critical,
            num_prev_callers=2
        )


class FeatureError(_FeatureException):
    def __init__(self, msg):
        super().__init__(msg)

    class InvalidAPIPreference(_FeatureException):
        def __init__(self, api_pref):
            super().__init__(f'"{api_pref}" is not a valid API preference. Valid preferences are "websdk" and "aperture".')

    class InvalidFormat(_FeatureException):
        pass

    class InvalidResultCode(_FeatureException):
        def __init__(self, code: int, code_description: str = 'Unknown'):
            super().__init__(f'Expected a valid result code, but got "{code}": {code_description}.')

    class TimeoutError(_FeatureException):
        def __init__(self, method, expected_value, actual_value, timeout: int):
            super().__init__(f'{method.__name__} did not return {expected_value} in {timeout} seconds. Got {actual_value} instead.')

    class UnexpectedValue(_FeatureException):
        pass


class ApiPreferences:
    websdk = 'websdk'
    aperture = 'aperture'
