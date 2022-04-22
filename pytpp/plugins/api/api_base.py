from pytpp.api.api_base import *
del globals()['API']  # We want to rename this and inherit it.
del globals()['APIResponse']  # We want to rename this and inherit it.
from pytpp.api.api_base import API as _API, APIResponse as _APIResponse
import re
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from requests import Response


class API(_API):
    """
    This is the backbone of all API definitions. It performs all requests,
    validations, logging, re-authentication, and holds the raw response. This
    class MUST be inherited by all API definitions.
    """
    def __init__(self, api_obj, url: str):
        """
        Args:
            api_obj: This is passed down from the API type object (eg. WebSDK, etc.) and
                represents that type. This type is REQUIRED because it contains the
                authenticated sessions, base URL, and re-authentication methods. It is
                through these properties this class is able to send and receive requests
                to TPP.
            url: This is the URL extension from the base URL.
        """
        super().__init__(api_obj=api_obj, url=url)
        self._api_source = api_obj.__class__.__name__.lower()

    def _is_api_key_invalid(self, response: 'Response'):
        """
        Uses a regular expression to search the response text for an indication that the API key
        is expired.

        Args:
            response: The raw response object.

        Returns:
            Returns True if the API key expired. Otherwise False.

        """
        if self._api_source == 'websdk':
            invalid_api_message_match = bool(re.match('.*API key.*is not valid.*', response.text))
        elif self._api_source == 'aperture':
            invalid_api_message_match = bool(re.match('.*The authorization header is incorrect.*', response.text))
        else:
            invalid_api_message_match = False

        return response.status_code == 401 and invalid_api_message_match


class APIResponse(_APIResponse):
    def __init__(self, response: Response, api_source: str):
        super().__init__(response=response)
        self._api_source = api_source
