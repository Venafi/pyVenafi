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
        if session:
            self.session = session
        elif username and password:
            token = self.Authorize.post(username=username, password=password).token
            self.session = Session(headers=token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        api_type = self.__class__.__name__.lower()
        self.Identity = _Identity(self.session, api_type)
        self.Config = _Config(self.session, api_type)
        self.Credentials = _Credentials(self.session, api_type)
        self.Certificates = _Certificates(self.session, api_type)
        self.SecretStore = _SecretStore(self.session, api_type)
