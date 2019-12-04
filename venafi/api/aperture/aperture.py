from api.session import Session, APERTURE_URL
from api.aperture.endpoints.users import _Users
from api.aperture.endpoints.configobjects import _ConfigObjects


class Aperture:
    def __init__(self, username=None, password=None, certificate=None, session=None):
        self.Users = _Users(None)

        if session:
            self.session = session
        elif username and password:
            token = self.Users.Authorize.post(username=username, password=password).token
            self.session = Session(headers=token)
        elif certificate:
            raise NotImplementedError('Certificate authentication not available.')

        api_type = self.__class__.__name__.lower()
        self.Users.__init__(self.session)
        self.ConfigObjects = _ConfigObjects(session=self.session, api_type=api_type)
