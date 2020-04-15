from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.config import Config


class _ConfigObjects:
    def __init__(self, aperture_obj):
        self.Policies = self._Policies(aperture_obj)

    class _Policies(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='/configobjects/policies')

        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def object(self):
                    return Config.Object(self._from_json(), self._api_source)

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )
