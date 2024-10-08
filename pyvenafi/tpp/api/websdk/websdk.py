from __future__ import annotations

from typing import (
    Optional,
    Union,
)

from packaging.version import (
    parse as parse_version,
    Version,
)

from pyvenafi.tpp.api.session import Session
from pyvenafi.tpp.api.websdk.endpoints.authorize import _Authorize
from pyvenafi.tpp.api.websdk.endpoints.bus_status import _BusStatus
from pyvenafi.tpp.api.websdk.endpoints.certificates import _Certificates
from pyvenafi.tpp.api.websdk.endpoints.client import _Client
from pyvenafi.tpp.api.websdk.endpoints.codesign import _Codesign
from pyvenafi.tpp.api.websdk.endpoints.config import _Config
from pyvenafi.tpp.api.websdk.endpoints.config_schema import _ConfigSchema
from pyvenafi.tpp.api.websdk.endpoints.credentials import _Credentials
from pyvenafi.tpp.api.websdk.endpoints.crypto import _Crypto
from pyvenafi.tpp.api.websdk.endpoints.discovery import _Discovery
from pyvenafi.tpp.api.websdk.endpoints.flow import _Flow
from pyvenafi.tpp.api.websdk.endpoints.hsm_api import _HSMAPI
from pyvenafi.tpp.api.websdk.endpoints.identity import _Identity
from pyvenafi.tpp.api.websdk.endpoints.log import _Log
from pyvenafi.tpp.api.websdk.endpoints.metadata import _Metadata
from pyvenafi.tpp.api.websdk.endpoints.oauth import _Oauth
from pyvenafi.tpp.api.websdk.endpoints.permissions import _Permissions
from pyvenafi.tpp.api.websdk.endpoints.pki import _PKI
from pyvenafi.tpp.api.websdk.endpoints.platform import _Platform
from pyvenafi.tpp.api.websdk.endpoints.preferences import _Preferences
from pyvenafi.tpp.api.websdk.endpoints.processing_engines import _ProcessingEngines
from pyvenafi.tpp.api.websdk.endpoints.recycle_bin import _RecycleBin
from pyvenafi.tpp.api.websdk.endpoints.revoke import _Revoke
from pyvenafi.tpp.api.websdk.endpoints.secret_store import _SecretStore
from pyvenafi.tpp.api.websdk.endpoints.server_status import _ServerStatus
from pyvenafi.tpp.api.websdk.endpoints.ssh import _SSH
from pyvenafi.tpp.api.websdk.endpoints.ssh_certificates import _SSHCertificates
from pyvenafi.tpp.api.websdk.endpoints.stats import _Stats
from pyvenafi.tpp.api.websdk.endpoints.system_status import _SystemStatus
from pyvenafi.tpp.api.websdk.endpoints.teams import _Teams
from pyvenafi.tpp.api.websdk.endpoints.workflow import _Workflow
from pyvenafi.tpp.api.websdk.endpoints.x509_certificate_store import _X509CertificateStore
from pyvenafi.tpp.api.websdk.enums.oauth import Scope

_TPP_VERSION: Optional[Version] = None

class WebSDK:
    """
    Initializes a WebSDK session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """

    def __init__(
        self, host: str, username: str, password: str, token: str = None, application_id: str = None,
        scope: Union[Scope, str] = None, refresh_token: str = None, proxies: dict = None,
        certificate_path: str = None, key_file_path: str = None, verify_ssl: bool = False,
        connection_timeout: float = None, read_timeout: float = None
    ):
        """
        Authenticates the given user to WebSDK. The only supported method for authentication at this time
        is with a username and password. Either an OAuth bearer token can be obtained, which requires
        both an Application ID and scope to be supplied, or the X-Venafi-API-Key can be obtained, which has
        been deprecated since TPP version 20.1.

        Using the OAuth authentication method requires an API Application Integration to be created that
        defines the maximum possible scope and the users/groups that are authorized to use that scope. That
        can be accomplished through Aperture. The ``scope`` parameter simply has to define the subset of
        allowed scopes defined by that application.

        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            token: OAuth Access Bearer Token
            application_id: Application ID of the OAuth API Application Integration. Must supply ``scope``.
            scope: Scope of the OAuth API Application Integration to be used. Must supply ``application_id``.
            proxies: An OrderedDict used by the python Requests library.
            certificate_path: Absolute path to the public certificate file.
            key_file_path: Absolute path to the private key file.
            verify_ssl: If ``True``, verify the SSL certificate of the target endpoints.
            connection_timeout: Timeout in seconds to establish a connection to the API service.
            read_timeout: Timeout in seconds between each byte received from the server.
        """
        # region Instance Variables
        self._host: str = host
        self._username: str = username
        self._password: str = password
        self._application_id: str = application_id
        self._scope: str = scope.to_string() if isinstance(scope, Scope) else scope
        self._token: str = token
        self._proxies: dict = proxies
        self._certificate_path: str = certificate_path
        self._key_file_path: str = key_file_path
        self._verify_ssl: bool = verify_ssl
        self._connection_timeout: float = connection_timeout
        self._read_timeout: float = read_timeout
        self._refresh_token: str = refresh_token

        # This is used by the endpoints to avoid redundancy.
        self._scheme = 'https'
        self._base_url = f'{self._scheme}://{host}'
        self._app_url = f'{self._base_url}/vedsdk'
        # endregion Instance Variables

        # region Authentication
        self._session = Session(
            headers={
                'Content-Type': 'application/json'
            },
            proxies=self._proxies,
            certificate_path=certificate_path,
            key_file_path=key_file_path,
            verify_ssl=verify_ssl,
            connection_timeout=connection_timeout,
            read_timeout=read_timeout
        )

        # Authorize the WebSDK session and store the API token.
        self.Authorize = _Authorize(self)
        self._authenticate()
        # endregion Authentication

        # region Initialize All WebSDK Endpoints
        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.BusStatus = _BusStatus(self)
        self.Certificates = _Certificates(self)
        self.Client = _Client(self)
        self.Codesign = _Codesign(self)
        self.Config = _Config(self)
        self.ConfigSchema = _ConfigSchema(self)
        self.Credentials = _Credentials(self)
        self.Crypto = _Crypto(self)
        self.Discovery = _Discovery(self)
        self.Flow = _Flow(self)
        self.HSMAPI = _HSMAPI(self)
        self.Identity = _Identity(self)
        self.Log = _Log(self)
        self.Metadata = _Metadata(self)
        self.Oauth = _Oauth(self)
        self.Permissions = _Permissions(self)
        self.PKI = _PKI(self)
        self.Platform = _Platform(self)
        self.Preferences = _Preferences(self)
        self.ProcessingEngines = _ProcessingEngines(self)
        self.RecycleBin = _RecycleBin(self)
        self.Revoke = _Revoke(self)
        self.SecretStore = _SecretStore(self)
        self.ServerStatus = _ServerStatus(self)
        self.SSH = _SSH(self)
        self.SSHCertificates = _SSHCertificates(self)
        self.Stats = _Stats(self)
        self.SystemStatus = _SystemStatus(self)
        self.Teams = _Teams(self)
        self.Workflow = _Workflow(self)
        self.X509CertificateStore = _X509CertificateStore(self)
        # endregion Initialize All WebSDK Endpoints

        # region Set TPP Version
        self._session.tpp_version = Version(f'{self.tpp_version.major}.{self.tpp_version.minor}')
        # endregion Set TPP Version

    @property
    def tpp_version(self):
        global _TPP_VERSION
        if _TPP_VERSION:
            return _TPP_VERSION
        _TPP_VERSION = parse_version(self.SystemStatus.Version.get().version)
        return _TPP_VERSION

    def _authenticate(self):
        if self._refresh_token:
            oauth = self.Authorize.Token.post(
                client_id=self._application_id,
                refresh_token=self._refresh_token
            )
            self._token = f'Bearer {oauth.access_token}'
            self._refresh_token = oauth.refresh_token
        elif not self._token:
            if self._application_id:
                if not self._scope:
                    raise ValueError(
                        f'OAuth authentication requires both an Application ID and a scope. '
                        f'The scope was not defined.'
                    )
                if self._certificate_path and self._key_file_path:
                    oauth = self.Authorize.Certificate.post(
                        client_id=self._application_id,
                        scope=self._scope
                    )
                else:
                    oauth = self.Authorize.OAuth.post(
                        username=self._username,
                        password=self._password,
                        client_id=self._application_id,
                        scope=self._scope
                    )
                self._token = f'Bearer {oauth.access_token}'
                self._refresh_token = oauth.refresh_token
            else:
                # Deprecated since TPP Version 20.1
                self._token = self.Authorize.post(username=self._username, password=self._password).token

        if self._token.endswith('=='):
            authorization_header = {
                'Authorization': self._token
            }
        else:
            authorization_header = {
                'X-Venafi-API-Key': self._token
            }
        self._session.update_headers(authorization_header)

    def re_authenticate(self):
        """
        Performs a re-authentication using the same parameters used to authorize initially.
        """
        self._token = None
        self._authenticate()
