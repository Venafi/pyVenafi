from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import discovery

class _Discovery(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Discovery')
        self.Import = self._Import(api_obj=api_obj, url=f'{self._url}/Import')

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

    class _Guid(WebSdkEndpoint):
        def delete(self):
            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._delete(), output_cls=Output)

    class _Import(WebSdkEndpoint):
        def post(self, endpoints: list[discovery.Endpoint], zone_name: str):
            body = {
                'zoneName' : zone_name,
                'endpoints': endpoints
            }

            class Output(WebSdkOutputModel):
                created_certificates: int = ApiField(alias='createdCertificates')
                created_instances: int = ApiField(alias='createdInstances')
                updated_certificates: int = ApiField(alias='updatedCertificates')
                updated_instances: int = ApiField(alias='updatedInstances')
                warnings: list[str] = ApiField(alias='warnings', default_factory=list)
                zone_name: str = ApiField(alias='zoneName')

            return generate_output(response=self._post(data=body), output_cls=Output)
