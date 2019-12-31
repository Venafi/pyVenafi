from venafi.logger import logger, LogLevels
from venafi.api.session import Session
from venafi.api.aperture.endpoints.users import _Users
from venafi.api.aperture.endpoints.configobjects import _ConfigObjects


@logger.wrap(LogLevels.feature)
class Aperture:
    """
    Initializes an Aperture session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """
    def __init__(self, host: str, username: str, password: str):
        """
        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            certificate: Certificate
        """
        self.host = host
        self.username = username
        self.password = password

        # This is used by the endpoints to avoid redundancy.
        self.base_url = f'https://{host}/aperture/api'

        # This is used by the endpoints to authorize the API writes.
        self.session = Session(headers={
            'Content-Type': 'application/json',
            'Referer': self.base_url.rstrip('/api')
        })

        # Authorize the Aperture session and store the API token.
        self.Users = _Users(self)

        # Update the authorization header to include the API Key token.
        token = self.Users.Authorize.post(username=username, password=password).token
        self.session.headers.update(token)

        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.ConfigObjects = _ConfigObjects(aperture_obj=self)

    def re_authenticate(self):
        """
        Performs a re-authentication using the same parameters used to authorize initially.
        """
        self.__init__(host=self.host, username=self.username, password=self.password)
