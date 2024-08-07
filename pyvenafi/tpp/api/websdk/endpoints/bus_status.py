from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import bus_status

class _BusStatus(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/BusStatus')
        self.GetStatus = self._GetStatus(api_obj=self._api_obj, url=f'{self._url}/GetStatus')
        self.GetMeshDnsName = self._GetMeshDnsName(api_obj=self._api_obj, url=f'{self._url}/GetMeshDnsName')
        self.SetMeshDnsName = self._SetMeshDnsName(api_obj=self._api_obj, url=f'{self._url}/SetMeshDnsName')

    class _GetStatus(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Status')
                status: bus_status.Status = ApiField(alias='Status')

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetMeshDnsName(WebSdkEndpoint):
        def post(self, engine: str):
            body = {
                "Engine": engine,
            }

            class Output(WebSdkOutputModel):
                dns_name: str = ApiField(alias='DnsName')
                mesh_dns_name: str = ApiField(alias='MeshDnsName')
                success: bool = ApiField(alias='Success')
                status: bus_status.Status = ApiField(alias='Status')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SetMeshDnsName(WebSdkEndpoint):
        def post(self, engine: str, mesh_dns_name: str):
            body = {
                "Engined"    : engine,
                "MeshDnsName": mesh_dns_name,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                status: bus_status.Status = ApiField(alias='Status')

            return generate_output(output_cls=Output, response=self._post(data=body))
