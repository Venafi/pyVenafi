from abc import abstractmethod
from tools.logger.logger import Logger
from tools.logger.log_resources import LogLevels
from apilibs.authenticator import Authenticate


class FeatureBase:
    def __init__(self, auth_obj):
        """
        :type auth_obj: Authenticate
        """
        self._logger = Logger(LogLevels.feature)
        self.auth = auth_obj

    @abstractmethod
    def load(self, *args, **kwargs):
        pass



class FeatureError(Exception):
    @classmethod
    def invalid_api_preference(cls, api_ref):
        return cls('"%s" is not a valid API preference. Valid preferences are "websdk" and "aperture".' % api_ref)

    @classmethod
    def not_implemented(cls, api_type):
        return cls('No implementation defined for this method using %s.' % api_type)
