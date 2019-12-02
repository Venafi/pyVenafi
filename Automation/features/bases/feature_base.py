import inspect
import jsonpickle
from logger import logger
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
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('__'):
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
