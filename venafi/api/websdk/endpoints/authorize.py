from api.api_base import API, response_property


class _Authorize(API):
    def __init__(self, websdk_obj):
        super().__init__(
            api_obj=websdk_obj,
            url='/Authorize',
            valid_return_codes=[200]
        )

    @property
    @response_property()
    def token(self):
        token = self._response.json()['APIKey']
        return {'X-Venafi-API-Key': token}

    def post(self, username, password):
        body = {
            "Username": username,
            "Password": password
        }

        self._response = self._post(data=body)
        return self
