from venafi.logger import logger, LogLevels
from venafi.api.session import Session
from venafi.api.aperture.endpoints.application_integration import _ApplicationIntegration
from venafi.api.aperture.endpoints.configobjects import _ConfigObjects
from venafi.api.aperture.endpoints.certificatedashboard import _CertificateDashboard
from venafi.api.aperture.endpoints.users import _Users


class Aperture:
    """
    Initializes an Aperture session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """
    @logger.wrap(LogLevels.medium.level, masked_variables=['password', 'token'])
    def __init__(self, host: str, username: str, password: str, token: str = None):
        """
        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            token: Either an Authorization Token created by Aperture or an OAuth Access Bearer Token.
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
            token = self.Users.Authorize.post(username=username, password=password).token
            token = f'VENAFI {token}'
        self._token = token
        self._session.headers.update({
            'Authorization': f'{token}'
        })
        # endregion Authentication

        # region Initialize All Aperture Endpoints
        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.ApplicationIntegration = _ApplicationIntegration(aperture_obj=self)
        self.ConfigObjects = _ConfigObjects(aperture_obj=self)
        self.CertificateDashboard = _CertificateDashboard(aperture_obj=self)
        # endregion Initialize All Aperture Endpoints

    def re_authenticate(self, token: str = None):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            token: OAuth token created via WebSDK.
        """
        self.__init__(host=self._host, username=self._username, password=self._password, token=token)
