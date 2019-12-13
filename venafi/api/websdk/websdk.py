from api.session import Session
from api.websdk.endpoints.authorize import _Authorize
from api.websdk.endpoints.certificates import _Certificates
from api.websdk.endpoints.client import _Client
from api.websdk.endpoints.config import _Config
from api.websdk.endpoints.config_schema import _ConfigSchema
from api.websdk.endpoints.credentials import _Credentials
from api.websdk.endpoints.crypto import _Crypto
from api.websdk.endpoints.discovery import _Discovery
from api.websdk.endpoints.identity import _Identity
from api.websdk.endpoints.log import _Log
from api.websdk.endpoints.metadata import _Metadata
from api.websdk.endpoints.permissions import _Permissions
from api.websdk.endpoints.processing_engines import _ProcessingEngines
from api.websdk.endpoints.secret_store import _SecretStore


class WebSDK:
    def __init__(self, host: str, username=None, password=None, certificate=None):
        self.host = host
        self.username = username
        self.password = password
        self.certificate = certificate

        self.base_url = f'https://{host}/vedsdk'
        self.session = Session(headers={'Content-Type': 'application/json'})
        self.Authorize = _Authorize(self)
        if username and password:
            token = self.Authorize.post(username=username, password=password).token
            self.session.headers.update(token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        self.Certificates = _Certificates(self)
        self.Client = _Client(self)
        self.Config = _Config(self)
        self.ConfigSchema = _ConfigSchema(self)
        self.Credentials = _Credentials(self)
        self.Crypto = _Crypto(self)
        self.Discovery = _Discovery(self)
        self.Identity = _Identity(self)
        self.Log = _Log(self)
        self.Metadata = _Metadata(self)
        self.Permissions = _Permissions(self)
        self.ProcessingEngines = _ProcessingEngines(self)
        self.SecretStore = _SecretStore(self)

    def re_authenticate(self):
        self.__init__(host=self.host, username=self.username, password=self.password, certificate=self.certificate)