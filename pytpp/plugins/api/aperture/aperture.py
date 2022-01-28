from pytpp.tools.logger import logger, LogTags
from pytpp.api.session import Session
from pytpp.plugins.api.aperture.endpoints.application_integration import _ApplicationIntegration
from pytpp.plugins.api.aperture.endpoints.approvers import _Approvers
from pytpp.plugins.api.aperture.endpoints.certificates import _Certificates
from pytpp.plugins.api.aperture.endpoints.configobjects import _ConfigObjects
from pytpp.plugins.api.aperture.endpoints.certificatedashboard import _CertificateDashboard
from pytpp.plugins.api.aperture.endpoints.device import _Device
from pytpp.plugins.api.aperture.endpoints.discovery import _Discovery
from pytpp.plugins.api.aperture.endpoints.jobs import _Jobs
from pytpp.plugins.api.aperture.endpoints.sshdashboard import _SshDashboard
from pytpp.plugins.api.aperture.endpoints.users import _Users
from pytpp.plugins.api.aperture.endpoints.version import _Version


class Aperture:
    """
    Initializes an Aperture session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """
    @logger.wrap_func(log_tag=LogTags.api, mask_input_regexes=['password', 'token'])
    def __init__(self, host: str, username: str, password: str, token: str = None, cookie: str = None,
                 proxies: dict = None):
        """
        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            token: Either an Authorization Token created by Aperture or an OAuth Access Bearer Token.
            cookie: Older versions of Aperture require this.
            proxies: An OrderedDict used by the python Requests library.
        """
        # region Instance Variables
        self._host = host
        self._username = username
        self._password = password
        self._proxies = proxies

        # This is used by the endpoints to avoid redundancy.
        self._base_url = f'https://{host}/aperture/api'
        # endregion Instance Variables

        # region Authentication
        # This is used by the endpoints to authorize the API writes.
        self._session = Session(
            headers={
                'Content-Type': 'application/json',
                'Referer': self._base_url.rstrip('/api')
            },
            proxies=proxies
        )

        # Authorize the Aperture session and store the API token.
        self.Users = _Users(self)

        # Update the authorization header to include the API Key token.
        if not token:
            response = self.Users.Authorize.post(username=username, password=password)
            token = f'VENAFI {response.token}'
            cookie =''
            for c in response.api_response.cookies:
                cookie = f'{c.name}={c.value}'
        self._token = token
        self._cookie = cookie
        self._session.update_headers({
            'Authorization': token,
            'Cookie': cookie
        })
        # endregion Authentication

        # region Initialize All Aperture Endpoints
        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.ApplicationIntegration = _ApplicationIntegration(self)
        self.Approvers = _Approvers(self)
        self.Certificates = _Certificates(self)
        self.ConfigObjects = _ConfigObjects(self)
        self.CertificateDashboard = _CertificateDashboard(self)
        self.Device = _Device(self)
        self.Discovery = _Discovery(self)
        self.Jobs = _Jobs(self)
        self.SshDashboard = _SshDashboard(self)
        self.Version = _Version(self)
        # endregion Initialize All Aperture Endpoints

    def re_authenticate(self, token: str = None):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            token: OAuth token created via WebSDK.
        """
        self.__init__(host=self._host, username=self._username, password=self._password, token=token,
                      proxies=self._proxies)
