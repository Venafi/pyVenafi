from abc import ABCMeta, abstractmethod
from tools.logger.logger import Logger, LogLevels
from apilibs.authenticate import Authenticate


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

    def read_attributes(self):
        pass


class FeatureError:
    class InvalidAPIPreference(Exception):
        def __init__(self, api_pref):
            super.__init__('"%s" is not a valid API preference. Valid preferences are "websdk" and "aperture".' % api_pref)


class ApiPreferences:
    websdk = 'websdk'
    aperture = 'aperture'
