from apilibs.session import APERTURE_URL
from apilibs.session import Session


class _Users:
    def __init__(self, session):
        self.Authorize = self._Authorize()

    class _Authorize:
        def __init__(self):
            self._session = Session({'Content-Type': 'application/json', 'Referer': APERTURE_URL.rstrip('/api')})
            self._url = APERTURE_URL + '/users/authorize'
            self.response = None

        @property
        def token(self):
            if self.response.status_code != 200:
                raise AssertionError('Could not authorize user. Received {e}: {m}.'.format(e=self.response.status_code, m=self.response.reason))
            token = "VENAFI " + self.response.json().get('apiKey')
            return {
                'Authorization': token,
                'Content-Type': 'application/json',
                'Referer': APERTURE_URL.rstrip('/api')
            }

        def post(self, username, password):
            body = {
                "username": username,
                "password": password
            }

            self.response = self._session.post(url=self._url, data=body)
            return self
