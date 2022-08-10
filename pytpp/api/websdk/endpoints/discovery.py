from typing import List 
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Discovery:
    def __init__(self, api_obj):
        self._api_obj = api_obj
        self.Import = self._Import(api_obj=api_obj)

    def Guid(self, guid: str):
        return self._Guid(guid=guid, api_obj=self._api_obj)

    class _Guid(WebSdkEndpoint):
        def __init__(self, guid: str, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Discovery/{guid}')

        def delete(self):
            class Response(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._delete(), response_cls=Response)

    class _Import(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Discovery/Import')

        def post(self, endpoints: list, zone_name: str):
            body = {
                'zoneName': zone_name,
                'endpoints': endpoints
            }

            class Response(WebSdkOutputModel):
                created_certificates: int = ApiField(alias='createdCertificates')
                created_instances: int = ApiField(alias='createdInstances')
                updated_certificates: int = ApiField(alias='updatedCertificates')
                updated_instances: int = ApiField(alias='updatedInstances')
                warnings: List[str] = ApiField(alias='warnings')
                zone_name: str = ApiField(alias='zoneName')

            return generate_output(response=self._post(data=body), response_cls=Response)

