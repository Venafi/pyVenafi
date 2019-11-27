import inspect
import jsonpickle
from abc import ABCMeta, abstractmethod
from tools.logger.logger import Logger, LogLevels
from apilibs.authenticate import Authenticate

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)


def _feature_decorator(func):
    def _wrapper(self, *args, **kwargs):
        # Before the function is called.
        params = dict(inspect.signature(func).bind(self, *args, **kwargs).arguments)
        if 'self' in params.keys():
            del params['self']
        before_string = 'Called ' + func.__qualname__
        if params:
            before_string += '\nArguments:\n' + jsonpickle.dumps(params, max_depth=2)
        self._logger.log_method(func_obj=func, msg=before_string)

        result = func(self, *args, **kwargs)

        # After the function returns.
        after_string = f'{func.__qualname__} returned.'
        if result is not None:
            ret_vals = jsonpickle.dumps(result, max_depth=2)
            after_string += f'\nReturn Values: {ret_vals}'
        self._logger.log_method(func_obj=func, msg=after_string)
    return _wrapper


def feature():
    def decorate(cls):
        for attr, fn in inspect.getmembers(cls, inspect.isroutine):
            # Only public methods are decorated.
            if callable(getattr(cls, attr)) and not fn.__name__.startswith('_'):
                setattr(cls, attr, _feature_decorator(getattr(cls, attr)))
        return cls
    return decorate


@feature()
class FeatureBase(metaclass=ABCMeta):
    def __init__(self, auth: Authenticate):
        self._logger = Logger(LogLevels.feature)
        self.auth = auth

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _log_not_implemented_warning(self, api_type):
        self._logger.log('No implementation defined for this method using %s.' % api_type, prev_frames=2)


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
