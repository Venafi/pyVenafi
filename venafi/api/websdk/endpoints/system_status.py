from api.api_base import API, response_property
from properties.response_objects.system_status import SystemStatus


class _SystemStatus(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/SystemStatus', valid_return_codes=[200])
        self.Version = self._Version(websdk_obj=websdk_obj)

    @property
    @response_property()
    def engine_name(self):
        return self.json_response('engineName')  # type: str

    @property
    @response_property()
    def services(self):
        return SystemStatus.Services(self.json_response('services'))

    @property
    @response_property()
    def version(self) -> str:
        return self.json_response('version')  # type: str

    def get(self):
        self.response = self._get()
        return self

    class _Version(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/SystemStatus/Version', valid_return_codes=[200])

        @property
        @response_property()
        def version(self) -> str:
            return self.json_response('Version')

        def get(self):
            self.response = self._get()
            return self
