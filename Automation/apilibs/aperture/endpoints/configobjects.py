import json
from apilibs.base import API, response_property
from apilibs.session import APERTURE_URL
from objects.response_objects.config import Config


class _ConfigObjects:
    def __init__(self, session, api_type):
        self.Policies = self._Policies(session, api_type)

    class _Policies(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=APERTURE_URL + '/configobjects/policies',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            obj = Config.Object(result, self._api_type)
            if not obj.dn:
                raise ValueError('Could not create policy.')
            return obj

        def post(self, name, container):
            body = json.dumps({
                "DN": container + "\\" + name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self
