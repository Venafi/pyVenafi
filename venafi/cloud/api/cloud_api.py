from typing import Optional, Union
from packaging.version import Version, parse as parse_version
from venafi.cloud.api.session import Session
from venafi.cloud.api.endpoints.edgemanagement_service import _pairingcodes

_CLOUD_API_VERSION: Optional[Version] = None


class CloudApi:
    def __init__(self, server: str, api_key: str, proxies: dict = None, verify_ssl: bool = False,
                 connection_timeout: float = None, read_timeout: float = None):
        self._api_key = api_key
        self._proxies = proxies
        self._verify_ssl = verify_ssl
        self._connection_timeout = connection_timeout
        self._read_timeout = read_timeout
        self._scheme = 'https'

        # region Authentication
        self._base_url = f'{self._scheme}://{server}'
        self._app_url = self._base_url
        self._session = Session(
            headers={
                'Content-Type': 'application/json',
                'tppl-api-key': api_key
            },
            proxies=self._proxies,
            verify_ssl=verify_ssl,
            connection_timeout=connection_timeout,
            read_timeout=read_timeout
        )
        # endregion Authentication

        # region Endpoints
        self.pairingcodes = _pairingcodes(self)
        # endregion Endpoints

    @property
    def version(self):
        global _CLOUD_API_VERSION
        if _CLOUD_API_VERSION:
            return _CLOUD_API_VERSION
        _CLOUD_API_VERSION = ...  # TODO
        return _CLOUD_API_VERSION
