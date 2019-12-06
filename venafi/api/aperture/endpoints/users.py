from api.api_base import API, response_property


class _Users:
    def __init__(self, aperture_obj):
        self.Authorize = self._Authorize(aperture_obj=aperture_obj)

    class _Authorize(API):
        def __init__(self, aperture_obj):
            super().__init__(
                api_obj=aperture_obj,
                url='/users/authorize',
                valid_return_codes=[200]
            )

        @property
        def token(self):
            token = "VENAFI " + self._response.json()['apiKey']
            return {'Authorization': token}

        def post(self, username, password):
            body = {
                "username": username,
                "password": password
            }

            self._response = self._post(data=body)
            return self
