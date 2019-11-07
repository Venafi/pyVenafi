from apilibs.websdk.websdk import WebSDK
from apilibs.aperture.aperture import Aperture


class Authenticate:
    def __init__(self, username=None, password=None, certificate=None, preference='websdk'):
        self.websdk = WebSDK(username=username, password=password)
        self.aperture = Aperture(username=username, password=password)

        if preference not in {'websdk', 'aperture'}:
            raise ValueError('Invalid preference. Must be one of "websdk" or "aperture".')
        self.preference = preference.lower()


class AuthenticationError(Exception):
    pass
