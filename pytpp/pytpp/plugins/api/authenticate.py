from pytpp.plugins.api.aperture.aperture import Aperture
from pytpp.plugins.api.websdk.endpoints.rights import _Rights
from pytpp.api.authenticate import Authenticate as _OriginalAuthenticate
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.plugins.api.websdk.websdk import WebSDK


class Authenticate(_OriginalAuthenticate):
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

    websdk: 'WebSDK'

    def __init__(self, *args, preference='websdk', aperture_token: str = None, **kwargs):
        """
        Authenticates the given user to WebSDK and Aperture. The only supported method for authentication at
        this time is with a username and password.

        For WebSDK, either an OAuth bearer token can be obtained, which requires both an Application ID and scope
        to be supplied, or the X-Venafi-API-Key can be obtained, which has been deprecated since TPP version 20.1.

        Using the OAuth authentication method requires an API Application Integration to be created that
        defines the maximum possible scope and the users/groups that are authorized to use that scope. That
        can be accomplished through Aperture. The ``scope`` parameter simply has to define the subset of
        allowed scopes defined by that application.

        If authenticating with OAuth, then the access token will be passed to Aperture. Otherwise, a separate
        authorization token will be created by Aperture.

        ..note:: It is highly recommended to use OAuth as it creates a single token that is utilized by both
        WebSDK and Aperture (as opposed to two tokens) and narrows the scope of the authenticated user.

        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            preference: Either 'websdk' or 'aperture'
            application_id: Application ID of the OAuth API Application Integration. Must supply ``scope``.
            scope: Scope of the OAuth API Application Integration to be used. Must supply ``application_id``.
            aperture_token: Either the Authorization Token created by Aperture or an OAuth Access Bearer Token
            websdk_token: Either the X-Venafi-API-Key or an OAuth Access Bearer Token
            suppress_not_implemented_warning: If `True` then features not exercising one of the API types will
                not log a warning stating so. This can greatly reduce the amount of logs and should be rarely
                used. To enable the warnings, set this to `False`.
            version: Version of the TPP server.
        """
        super().__init__(*args, **kwargs)

        # Extend WebSDK API
        self.websdk.Rights = _Rights(self.websdk)

        # Set up Aperture API
        if self.websdk._oauth is not None and not aperture_token:
            self.aperture = Aperture(
                host=self.host,
                username=self.username,
                password=self.password,
                token=self.websdk._token,
                proxies=self._proxies
            )
        else:
            self.aperture = Aperture(
                host=self.host,
                username=self.username,
                password=self.password,
                token=aperture_token,
                proxies=self._proxies
            )
        self.preference = preference.lower()
        if self.preference not in {'websdk', 'aperture'}:
            raise ValueError('Invalid preference. Must be one of "websdk" or "aperture".')

    def re_authenticate(self, host: str = None, username: str = None, password: str = None, preference=None,
                        application_id: str = None, scope: str = None, proxies: dict = None):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            host: Hostname or IP Address
            username: Username
            password: Password
            preference: 'websdk' or 'aperture'
            application_id: Application ID applicable to OAuth. Must supply ``scope``.
            scope: Scope within the Application. Must supply ``application_id``.
            proxies: An OrderedDict used by the python Requests library.
        """
        if any([host, username, password, application_id, scope]):
            self.__init__(
                host=host or self._host,
                username=username or self._username,
                password=password or self._password,
                preference=preference or self.preference,
                application_id=application_id or self._application_id,
                scope=scope or self._scope,
                version=str(self._tpp_version),
                proxies=self._proxies
            )
        else:
            if preference:
                self.preference = preference
            self.websdk.re_authenticate()
            if self.websdk._oauth is not None:
                self.aperture.re_authenticate(token=self.websdk._token)
            else:
                self.aperture.re_authenticate()
