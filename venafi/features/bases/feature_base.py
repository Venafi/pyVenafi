import inspect
import jsonpickle
import time
from venafi.logger import logger, LogLevels
from venafi.properties.secret_store import Namespaces
from venafi.api.authenticate import Authenticate
import os

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)


def __feature_decorator(func):
    def __wrapper(self, *args, **kwargs):
        # Before the function is called.
        try:
            params = dict(inspect.signature(func).bind(self, *args, **kwargs).arguments)
        except TypeError as e:
            logger.log(
                msg='\n'.join(e.args),
                level=LogLevels.critical,
                prev_frames=2
            )
            raise TypeError(e)

        if 'self' in params.keys():
            del params['self']
        before_string = 'Called ' + func.__qualname__
        if params:
            before_string += '\nArguments:\n' + jsonpickle.dumps(params, max_depth=2)
        logger.log_method(func_obj=func, msg=before_string, level=LogLevels.feature, reference_lastlineno=False)

        result = func(self, *args, **kwargs)

        # After the function returns.
        after_string = f'{func.__qualname__} returned.'
        if result is not None:
            ret_vals = jsonpickle.dumps(result, max_depth=2)
            after_string += f'\nReturn Values: {ret_vals}'
        logger.log_method(func_obj=func, msg=after_string, level=LogLevels.feature, reference_lastlineno=True)

        return result
    return __wrapper


def feature():
    def decorate(cls):
        if int(os.getenv('VENAFI_PY_DOC_IN_PROGRESS', 0)):
            return cls
        for attr, fn in inspect.getmembers(cls, inspect.isroutine):
            # Only public methods are decorated.
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('_'):
                setattr(cls, attr, __feature_decorator(getattr(cls, attr)))
        return cls
    return decorate


@feature()
class FeatureBase:
    def __init__(self, auth: Authenticate):
        self.auth = auth

    # def read_attribute(self, object_dn: str, attiribute_name: str, attribute_value: str, timeout: int = 10):
    #     def get_attribute():
    #         values = self.auth.websdk.Config.ReadDn.post(object_dn=object_dn, attiribute_name=attiribute_name).values
    #         found = any([True for value in values if str(value).lower() == attribute_value.lower()])
    #         if found:
    #             return True
    #     self._wait_for_method(method=get_attribute, return_value=True, timeout=timeout)

    def _config_create(self, name: str, container: str, config_class: str, attributes: dict = None):
        if attributes:
            attributes = self._name_value_list(attributes=attributes)

        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ca = self.auth.websdk.Config.Create.post(object_dn=dn, class_name=config_class, name_attribute_list=attributes or [])

        result = ca.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return ca.object

    def _config_delete(self, object_dn, recursive: bool = False):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Config.Delete.post(object_dn=object_dn, recursive=recursive).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    @staticmethod
    def _log_not_implemented_warning(api_type):
        logger.log(f'No implementation defined for this method using {api_type}.', level=LogLevels.feature, prev_frames=2)

    @staticmethod
    def _name_type_value(name: str, type: str, value):
        return {'Name': str(name), 'Type': str(type), 'Value': str(value)}

    @staticmethod
    def _name_value_list(attributes: dict):
        nvl = []
        for name, value in attributes.items():
            if not isinstance(value, dict) or not isinstance(value, list):
                value = str(value)
            nvl.append({'Name': str(name), 'Value': value})
        return nvl

    def _secret_store_delete_by_dn(self, object_dn: str, namespace: str = Namespaces.config):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        owners = self.auth.websdk.SecretStore.LookupByOwner.post(namespace=namespace, owner=object_dn)
        result = owners.result
        if result.code != 0:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

        for vault_id in owners.vault_ids:
            result = self.auth.websdk.SecretStore.Delete.post(vault_id=vault_id).result
            if result.code != 0:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

    @staticmethod
    def _wait_for_method(method, return_value, timeout: int = 10):
        maxtime = time.time() + timeout
        interval = 0.5

        logger.disable_all_logging(
            level=LogLevels.feature,
            why=f'Running {method.__name__} method with a timeout of {timeout} seconds at {interval} second intervals. '
                f'Expected output value is "{return_value}".',
            func_obj=method
        )

        actual_value = None
        while time.time() < maxtime:
            actual_value = method()
            if actual_value == return_value:
                lapse = int(timeout - (maxtime - time.time()))
                logger.enable_all_logging(
                    level=LogLevels.feature,
                    why=f'{method.__name__} returned "{actual_value}" after {lapse} seconds.',
                    func_obj=method,
                    reference_lastlineno=True
                )
                return
            time.sleep(interval)

        raise TimeoutError(f'{method.__name__} did not return {return_value} in {timeout} seconds. Got {actual_value} instead.')


class _FeatureException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

    def log(self):
        logger.log(
            msg=self.__str__(),
            level=LogLevels.critical,
            prev_frames=2
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


class ApiPreferences:
    websdk = 'websdk'
    aperture = 'aperture'
