from api.session import Session
from api.aperture.endpoints.users import _Users
from api.aperture.endpoints.configobjects import _ConfigObjects


class Aperture:
    def __init__(self, host: str, username=None, password=None, certificate=None):
        self.host = host
        self.username = username
        self.password = password
        self.certificate = certificate

        self.base_url = f'https://{host}/aperture/api'
        self.session = Session(headers={
            'Content-Type': 'application/json',
            'Referer': self.base_url.rstrip('/api')
        })
        self.Users = _Users(self)
        if username and password:
            token = self.Users.Authorize.post(username=username, password=password).token
            self.session.headers.update(token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        self.ConfigObjects = _ConfigObjects(aperture_obj=self)

    def re_authenticate(self):
        self.__init__(host=self.host, username=self.username, password=self.password, certificate=self.certificate)
