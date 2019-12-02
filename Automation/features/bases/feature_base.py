import inspect
import jsonpickle
from logger import logger
from enums.secret_store import Namespaces
from apilibs.authenticate import Authenticate

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)


def __feature_decorator(func):
    def __wrapper(self, *args, **kwargs):
        # Before the function is called.
        try:
            params = dict(inspect.signature(func).bind(self, *args, **kwargs).arguments)
        except TypeError as e:
            raise TypeError(e)

        if 'self' in params.keys():
            del params['self']
        before_string = 'Called ' + func.__qualname__
        if params:
            before_string += '\nArguments:\n' + jsonpickle.dumps(params, max_depth=2)
        self._logger.log_method(func_obj=func, msg=before_string, reference_lastlineno=False)

        result = func(self, *args, **kwargs)

        # After the function returns.
        after_string = f'{func.__qualname__} returned.'
        if result is not None:
            ret_vals = jsonpickle.dumps(result, max_depth=2)
            after_string += f'\nReturn Values: {ret_vals}'
        self._logger.log_method(func_obj=func, msg=after_string, reference_lastlineno=True)

        return result
    return __wrapper


def feature():
    def decorate(cls):
        for attr, fn in inspect.getmembers(cls, inspect.isroutine):
            # Only public methods are decorated.
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('_'):
                setattr(cls, attr, __feature_decorator(getattr(cls, attr)))
        return cls
    return decorate


@feature()
class FeatureBase:
    def __init__(self, auth: Authenticate):
        self._logger = logger.feature_logger
        self.auth = auth

    def _log_not_implemented_warning(self, api_type):
        self._logger.log('No implementation defined for this method using %s.' % api_type, prev_frames=2)

    def _name_value_attributes(self, attributes: dict):
        return [{'Name': str(key), 'Value': str(value)}for key, value in attributes.items()]

    def _config_create(self, name: str, container: str, config_class: str, attributes: dict = None):
        if attributes:
            attributes = self._name_value_attributes(attributes=attributes)

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


class FeatureError:
    class InvalidAPIPreference(Exception):
        def __init__(self, api_pref):
            super().__init__(f'"{api_pref}" is not a valid API preference. Valid preferences are "websdk" and "aperture".')

    class InvalidResultCode(Exception):
        def __init__(self, code: int, code_description: str = 'Unknown'):
            super().__init__(f'Expected a valid result code, but got "{code}": {code_description}.')


class ApiPreferences:
    websdk = 'websdk'
    aperture = 'aperture'
