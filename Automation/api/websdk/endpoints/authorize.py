from api.session import WEBSDK_URL
from api.session import Session


class _Authorize:
    def __init__(self):
        self._session = Session({'Content-Type': 'application/json'})
        self._url = WEBSDK_URL + '/Authorize'
        self.response = None

    @property
    def token(self):
        if self.response.status_code != 200:
            raise AssertionError('Could not authorize user. Received {e}: {m}.'.format(e=self.response.status_code, m=self.response.reason))
        token = self.response.json().get('APIKey')
        return {
            'X-Venafi-API-Key': token,
            'Content-Type': 'application/json'
        }

    def post(self, username, password):
        body = {
            "Username": username,
            "Password": password
        }

        self.response = self._session.post(url=self._url, data=body)
        return self
