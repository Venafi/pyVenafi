from api.websdk.websdk import WebSDK
from api.aperture.aperture import Aperture


class Authenticate:
    def __init__(self, host: str, username=None, password=None, certificate=None, preference='websdk'):
        self.websdk = WebSDK(host=host, username=username, password=password)
        self.aperture = Aperture(host=host, username=username, password=password)
        if preference not in {'websdk', 'aperture'}:
            raise ValueError('Invalid preference. Must be one of "websdk" or "aperture".')
        self.preference = preference.lower()

        self._username = username
        self._password = password
        self._certificate = certificate

    def re_authenticate(self):
        self.__init__(username=self._username, password=self._password, certificate=self._certificate,
                      preference=self.preference)


class AuthenticationError(Exception):
    pass
