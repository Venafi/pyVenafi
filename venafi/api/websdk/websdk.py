from api.session import Session
from api.websdk.endpoints.authorize import _Authorize
from api.websdk.endpoints.identity import _Identity
from api.websdk.endpoints.config import _Config
from api.websdk.endpoints.credentials import _Credentials
from api.websdk.endpoints.certificates import _Certificates
from api.websdk.endpoints.secret_store import _SecretStore


class WebSDK:
    Authorize = _Authorize()

    def __init__(self, username=None, password=None, certificate=None, session=None):
        self.username = username
        self.password = password
        self.certificate = certificate

        if session:
            self.session = session
        elif username and password:
            token = self.Authorize.post(username=username, password=password).token
            self.session = Session(headers=token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        api_type = self.__class__.__name__.lower()
        self.Identity = _Identity(self)
        self.Config = _Config(self)
        self.Credentials = _Credentials(self)
        self.Certificates = _Certificates(self)
        self.SecretStore = _SecretStore(self)

    def re_authenticate(self):
        self.__init__(username=self.username, password=self.password, certificate=self.certificate)