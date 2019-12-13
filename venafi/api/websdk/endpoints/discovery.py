from api.api_base import API, json_response_property
from properties.response_objects.client import Client


class _Discovery:
    def __init__(self, websdk_obj):
        self._websdk_obj = websdk_obj
        self.Import = self._Import(websdk_obj=websdk_obj)

    def Guid(self, guid: str):
        return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

    class _Guid(API):
        def __init__(self, guid: str, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Discovery/{guid}', valid_return_codes=[200])

        @property
        @json_response_property()
        def success(self):
            return self._from_json('Success')

        def delete(self):
            self.json_response = self._delete()
            return self

    class _Import(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Discovery/Import', valid_return_codes=[200])

        @property
        @json_response_property()
        def created_certificates(self):
            return self._from_json('createdCertificates')

        @property
        @json_response_property()
        def created_instances(self):
            return self._from_json('createdInstances')

        @property
        @json_response_property()
        def updated_certificates(self):
            return self._from_json('updatedCertificates')

        @property
        @json_response_property()
        def updated_instances(self):
            return self._from_json('updatedInstances')

        @property
        @json_response_property()
        def warnings(self):
            return self._from_json('warnings')

        @property
        @json_response_property()
        def zone_name(self):
            return self._from_json('zoneName')

        def post(self, endpoints: list, zone_name: str):
            body = {
                'zoneName': zone_name,
                'endpoints': endpoints
            }

            self.json_response = self._post(data=body)

            return self

