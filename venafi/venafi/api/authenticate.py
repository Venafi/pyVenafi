from venafi.api.websdk.websdk import WebSDK
from venafi.api.aperture.aperture import Aperture


class Authenticate:
    """
    Authenticates WebSDK and Aperture API sessions.

    Username/password authentication is the only authentication method supported. Certificate
    authentication will be supported soon.

    A `preference` parameter is available to persuade the Features to utilized the preferred API type
    when possible. If ``preference='aperture'``, then all Features will attempt to use Aperture APIs
    when available to accomplish a task. If no Aperture API is defined, then the Feature will default
    to WebSDK and log a message that Aperture could not be used. It should be noted that more support
    is provided by WebSDK, which is the default.
    """
    def __init__(self, host: str, username: str, password: str, preference='websdk'):
        """
        Args:
            host: Hostname or IP Address
            username: Username
            password: Password
            preference: 'websdk' or 'aperture'
        """
        self.websdk = WebSDK(host=host, username=username, password=password)
        self.aperture = Aperture(host=host, username=username, password=password)
        self.preference = preference.lower()
        if self.preference not in {'websdk', 'aperture'}:
            raise ValueError('Invalid preference. Must be one of "websdk" or "aperture".')

        self._host = host
        self._username = username
        self._password = password

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def re_authenticate(self, host: str = None, username: str = None, password: str = None, preference=None):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            host: Hostname or IP Address
            username: Username
            password: Password
            preference: 'websdk' or 'aperture'
        """
        if host or username or password:
            self.__init__(
                host=host or self._host,
                username=username or self._username,
                password=password or self._password,
                preference=preference or self.preference
            )
        else:
            if preference:
                self.preference = preference
            self.websdk.re_authenticate()
            self.aperture.re_authenticate()
