from apilibs.session import Session
from requests import Response
from tools.logger.logger import Logger
from tools.logger.log_resources import LogLevels


def response_property():
    def pre_validation(func):
        def wrap(self, *args, **kwargs):
            if not self._validated:
                self._validate()
            return func(self, *args, **kwargs)
        return wrap
    return pre_validation


class API:
    def __init__(self, session, api_type, url, valid_return_codes):
        """
        :type session: Session
        """
        self._session = session
        self._api_type = api_type
        self._url = url
        self._valid_return_codes = valid_return_codes

        self._response = None
        self._validated = False
        self.logger = Logger(LogLevels.api)

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._validated = False
        self._response = value

    def _validate(self):
        self._validated = True

        if not isinstance(self.response, Response):
            raise TypeError("Expected response object, but got %s." % type(self.response))

        if self.response.status_code not in self._valid_return_codes:
            raise InvalidResponseError("Received %s, but expected one of %s. Error message is: %s" % (self.response.status_code, str(self._valid_return_codes), self.response.text))

        self.logger.log('Response to %s is valid. Got %s.' %(self._url, self.response.status_code))


class InvalidResponseError(Exception):
    pass
