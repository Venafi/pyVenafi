from pytpp.api.api_base import generate_output, ApiField, WebSdkEndpoint, WebSdkOutputModel
from pytpp.plugins.api.websdk.outputs import rights
from typing import List


class _Rights:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Get = self._Get(api_obj=api_obj)
        self.Refresh = self._Refresh(api_obj=api_obj)
        self.Remove = self._Remove(api_obj=api_obj)

    class _Add(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Add')

        def post(self, subsystem: str, rights_object: str, universal_id: str, rights_value: str):
            body = {
                'Subsystem': subsystem,
                'RightsObject': rights_object,
                'UniversalID': universal_id,
                'RightsValue': rights_value
            }

            return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

    class _Get(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Get')

        def post(self, universal_id: str):
            body = {
                'UniversalID': universal_id
            }

            class Response(WebSdkOutputModel):
                rights: List[rights.Rights] = ApiField(alias='Rights')

            return generate_output(output_cls=Response, response=self._post(data=body))

    class _Refresh(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Refresh')

        def get(self):
            return generate_output(output_cls=WebSdkOutputModel, response=self._get())

    class _Remove(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Rights/Remove')

        def post(self, universal_id: str, subsystem: str = None, rights_object: str = None):
            body = {
                "Subsystem": subsystem,
                "RightsObject": rights_object,
                "UniversalID": universal_id
            }

            return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))
