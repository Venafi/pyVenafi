from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.rights import Rights


class _Rights:
    def __init__(self, websdk_obj):
        self.Add = self._Add(websdk_obj=websdk_obj)
        self.Get = self._Get(websdk_obj=websdk_obj)
        self.Refresh = self._Refresh(websdk_obj=websdk_obj)
        self.Remove = self._Remove(websdk_obj=websdk_obj)

    class _Add(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Rights/Add', valid_return_codes=[200])

        def post(self, subsystem: str, rights_object: str, universal_id: str, rights_value: str):
            body = {
                'Subsystem': subsystem,
                'RightsObject': rights_object,
                'UniversalID': universal_id,
                'RightsValue': rights_value
            }

            self.json_response = self._post(data=body)
            return self

    class _Get(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Rights/Get', valid_return_codes=[200])

        @property
        @json_response_property()
        def rights(self):
            return [Rights.Rights(rights) for rights in self._from_json('Rights')]

        def post(self, universal_id: str):
            body = {
                'UniversalID': universal_id
            }

            self.json_response = self._post(data=body)
            return self

    class _Refresh(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Rights/Refresh', valid_return_codes=[200])

        def get(self):
            self.json_response = self._get()
            return self

    class _Remove(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Rights/Remove', valid_return_codes=[200])

        def post(self, universal_id: str, subsystem: str = None, rights_object: str = None):
            body = {
                "Subsystem": subsystem,
                "RightsObject": rights_object,
                "UniversalID": universal_id
            }

            self.json_response = self._post(data=body)
            return self
