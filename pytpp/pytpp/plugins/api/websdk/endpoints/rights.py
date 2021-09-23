from pytpp.api.api_base import API, APIResponse, json_response_property
from pytpp.properties.response_objects.rights import Rights


class _Rights:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Get = self._Get(api_obj=api_obj)
        self.Refresh = self._Refresh(api_obj=api_obj)
        self.Remove = self._Remove(api_obj=api_obj)

    class _Add(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Add')

        def post(self, subsystem: str, rights_object: str, universal_id: str, rights_value: str):
            body = {
                'Subsystem': subsystem,
                'RightsObject': rights_object,
                'UniversalID': universal_id,
                'RightsValue': rights_value
            }

            return APIResponse(response=self._post(data=body))

    class _Get(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Get')

        def post(self, universal_id: str):
            body = {
                'UniversalID': universal_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @json_response_property()
                def rights(self):
                    return [Rights.Rights(rights) for rights in self._from_json('Rights')]

            return _Response(response=self._post(data=body))

    class _Refresh(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Refresh')

        def get(self):
            return APIResponse(response=self._get())

    class _Remove(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Remove')

        def post(self, universal_id: str, subsystem: str = None, rights_object: str = None):
            body = {
                "Subsystem": subsystem,
                "RightsObject": rights_object,
                "UniversalID": universal_id
            }

            return APIResponse(response=self._post(data=body))
