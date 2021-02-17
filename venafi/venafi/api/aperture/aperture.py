from venafi.logger import logger, LogTags
from venafi.api.session import Session
from venafi.api.aperture.endpoints.application_integration import _ApplicationIntegration
from venafi.api.aperture.endpoints.certificates import _Certificates
from venafi.api.aperture.endpoints.configobjects import _ConfigObjects
from venafi.api.aperture.endpoints.certificatedashboard import _CertificateDashboard
from venafi.api.aperture.endpoints.discovery import _Discovery
from venafi.api.aperture.endpoints.jobs import _Jobs
from venafi.api.aperture.endpoints.users import _Users
from venafi.api.aperture.endpoints.version import _Version


class Aperture:
    """
    Initializes an Aperture session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """
    @logger.wrap_func(log_tag=LogTags.feature, mask_input_regexes=['password', 'token'])
    def __init__(self, host: str, username: str, password: str, token: str = None, cookie: str = None):
        """
        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            token: Either an Authorization Token created by Aperture or an OAuth Access Bearer Token.
            cookie: Older versions of Aperture require this.
        """
        # region Instance Variables
        self._host = host
        self._username = username
        self._password = password

        # This is used by the endpoints to avoid redundancy.
        self._base_url = f'https://{host}/aperture/api'
        # endregion Instance Variables

        # region Authentication
        # This is used by the endpoints to authorize the API writes.
        self._session = Session(headers={
            'Content-Type': 'application/json',
            'Referer': self._base_url.rstrip('/api')
        })

        # Authorize the Aperture session and store the API token.
        self.Users = _Users(self)

        # Update the authorization header to include the API Key token.
        if not token:
            response = self.Users.Authorize.post(username=username, password=password)
            token = f'VENAFI {response.token}'
            cookie =''
            for c in response.json_response.cookies:
                cookie = f'{c.name}={c.value}'
        self._token = token
        self._cookie = cookie
        self._session.headers.update({
            'Authorization': f'{token}',
            'Cookie': cookie
        })
        # endregion Authentication

        # region Initialize All Aperture Endpoints
        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.ApplicationIntegration = _ApplicationIntegration(self)
        self.Certificates = _Certificates(self)
        self.ConfigObjects = _ConfigObjects(self)
        self.CertificateDashboard = _CertificateDashboard(self)
        self.Discovery = _Discovery(self)
        self.Jobs = _Jobs(self)
        self.Version = _Version(self)
        # endregion Initialize All Aperture Endpoints

    def re_authenticate(self, token: str = None):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            token: OAuth token created via WebSDK.
        """
        self.__init__(host=self._host, username=self._username, password=self._password, token=token)
