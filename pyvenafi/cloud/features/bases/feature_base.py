import logging
import time
import os
from typing import TYPE_CHECKING
from pyvenafi.logger import logger, features_logger


if TYPE_CHECKING:
    from pyvenafi.cloud.api.authenticate import Authenticate


def feature(name: str):
    def decorate(cls):
        if int(os.getenv('PYVAAS_DOC_IN_PROGRESS', 0)):
            return cls
        setattr(cls, '__feature__', name)
        return features_logger.wrap_class(
            level=logging.DEBUG,
            exclude='_.*'
        )(cls)

    return decorate


class FeatureBase:
    def __init__(self, api: 'Authenticate'):
        self._api = api

    @staticmethod
    def _log_warning_message(msg: str):
        features_logger.warning(msg, stacklevel=2)

    @staticmethod
    def __no_op(*args, **kwargs):
        pass

    class _Timeout:
        def __init__(self, timeout):
            self.timeout = timeout
            self.max_time = timeout + time.time()
            self._cm = logger.suppressed(999)

        def __enter__(self):
            self._cm.__enter__()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self._cm.__exit__(exc_type, exc_val, exc_tb)
            return

        def is_expired(self, poll: float = 0.5):
            if time.time() >= self.max_time:
                return True
            if poll:
                time.sleep(poll)

        @staticmethod
        def poll(seconds: float):
            time.sleep(seconds)
