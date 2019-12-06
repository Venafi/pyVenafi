from api.api_base import API, response_property
from objects.response_objects.config import Config


class _ConfigObjects:
    def __init__(self, aperture_obj):
        self.Policies = self._Policies(aperture_obj)

    class _Policies(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/configobjects/policies', valid_return_codes=[200])

        @property
        @response_property()
        def object(self):
            result = self.json_response()
            obj = Config.Object(result, self._api_type)
            if not obj.dn:
                raise ValueError('Could not create policy.')
            return obj

        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            self.response = self._post(data=body)

            return self
