from pytpp.tools.logger import logger


class FeatureException(Exception):
    def log(self):
        logger.error(
            msg=self.__str__(),
            num_prev_callers=2
        )

class FeatureTimeoutError(FeatureException):
    def __init__(self, method, expected_value, actual_value, timeout: int):
        super().__init__(
            f'{method.__name__} did not return {expected_value} in {timeout} seconds. Got {actual_value} instead.')

class InvalidFormat(FeatureException): ...

class InvalidResultCode(FeatureException):
    def __init__(self, code: int, code_description: str = 'Unknown'):
        super().__init__(f'Expected a valid result code, but got "{code}": {code_description}.')

class ObjectDoesNotExist(FeatureException): ...

class UnexpectedValue(FeatureException): ...
