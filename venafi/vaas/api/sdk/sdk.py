from typing import Optional, Union
from packaging.version import Version, parse as parse_version
from venafi.vaas.api.session import Session
from venafi.vaas.api.sdk.endpoints.edge_management import _PairingCodes

_SDK_VERSION: Optional[Version] = None


class Sdk:
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
        self.pairingCodes = _PairingCodes(self)
        # endregion Endpoints

    @property
    def version(self):
        global _SDK_VERSION
        if _SDK_VERSION:
            return _SDK_VERSION
        _SDK_VERSION = ...  # TODO
        return _SDK_VERSION

    def re_authenticate(self):
        pass
