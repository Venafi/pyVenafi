from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.config import Config


class _ConfigObjects:
    def __init__(self, aperture_obj):
        self.Policies = self._Policies(aperture_obj)

    class _Policies(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/configobjects/policies', valid_return_codes=[200])

        @property
        @json_response_property()
        def object(self):
            return Config.Object(self._from_json(), self._api_type)

        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            self.json_response = self._post(data=body)
            return self
