from pytpp.plugins.api.api_base import API, APIResponse, api_response_property
from pytpp.plugins.properties.response_objects.config import Config


class _ConfigObjects:
    def __init__(self, api_obj):
        self.Policies = self._Policies(api_obj)

    class _Policies(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/configobjects/policies')

        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @api_response_property()
                def object(self):
                    return Config.Object(self._from_json(), self._api_source)

            return _Response(response=self._post(data=body), api_source=self._api_source)
