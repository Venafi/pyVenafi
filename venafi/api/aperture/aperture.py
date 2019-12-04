from api.session import Session, APERTURE_URL
from api.aperture.endpoints.users import _Users
from api.aperture.endpoints.configobjects import _ConfigObjects


class Aperture:
    def __init__(self, username=None, password=None, certificate=None, session=None):
        self.Users = _Users(None)

        self.username = username
        self.password = password
        self.certificate = certificate

        if session:
            self.session = session
        elif username and password:
            token = self.Users.Authorize.post(username=username, password=password).token
            self.session = Session(headers=token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        self.Users.__init__(aperture_obj=self)
        self.ConfigObjects = _ConfigObjects(aperture_obj=self)

    def re_authenticate(self):
        self.__init__(username=self.username, password=self.password, certificate=self.certificate)
