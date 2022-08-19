from pytpp.api.api_base import generate_output, ApiField, WebSdkEndpoint, WebSdkOutputModel
from pytpp.plugins.api.websdk.models import rights
from typing import List


class _Rights(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Rights')
        self.Add = self._Add(api_obj=self._api_obj, url=f'{self._url}/Add')
        self.Get = self._Get(api_obj=self._api_obj, url=f'{self._url}/Get')
        self.Refresh = self._Refresh(api_obj=self._api_obj, url=f'{self._url}/Refresh')
        self.Remove = self._Remove(api_obj=self._api_obj, url=f'{self._url}/Remove')

    class _Add(WebSdkEndpoint):
        def post(self, subsystem: str, rights_object: str, universal_id: str, rights_value: str):
            body = {
                'Subsystem'   : subsystem,
                'RightsObject': rights_object,
                'UniversalID' : universal_id,
                'RightsValue' : rights_value
            }

            return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

    class _Get(WebSdkEndpoint):
        def post(self, universal_id: str):
            body = {
                'UniversalID': universal_id
            }

            class Output(WebSdkOutputModel):
                rights: List[rights.Rights] = ApiField(alias='Rights', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Refresh(WebSdkEndpoint):
        def get(self):
            return generate_output(output_cls=WebSdkOutputModel, response=self._get())

    class _Remove(WebSdkEndpoint):
        def post(self, universal_id: str, subsystem: str = None, rights_object: str = None):
            body = {
                "Subsystem"   : subsystem,
                "RightsObject": rights_object,
                "UniversalID" : universal_id
            }

            return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))
