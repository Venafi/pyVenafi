from pytpp.api.api_base import ApiField, generate_output
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.models import device
from typing import List


class _Device(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url=f'/device')

        self.BulkOperations = self._BulkOperations(api_obj=self._api_obj, url=f'{self._url}/bulkOperations')
        self.GetStatus = self._GetStatus(api_obj=self._api_obj, url=f'{self._url}/GetStatus')

    def post(self, ssh_type: str = "", job: str = "", custom_field_name: str = "",
             custom_field_value: List[str] = None, common_name: List[str] = None, properties: List[str] = None,
             environment: List[str] = None, folder: List[str] = None, status: List[str] = None,
             include_sub_folders: bool = False, offset: int = 0, limit: int = 20):
        body = {
            "Type"             : ssh_type,
            "Job"              : job,
            "CustomFieldName"  : custom_field_value,
            "CustomFieldValue" : custom_field_name or [],
            "CommonName"       : common_name or [],
            "Properties"       : properties or [],
            "Environment"      : environment or [],
            "Folder"           : folder or [],
            "Status"           : status or [],
            "IncludeSubfolders": include_sub_folders,
            "Offset"           : offset,
            "Limit"            : limit
        }

        class Output(ApertureOutputModel):
            total_count: int = ApiField(key='totalCount')
            devices_list_items: List[device.Device] = ApiField(alias='devicesListItems', default_factory=list)

        return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetStatus(ApertureEndpoint):
        def get(self, device_guid: str):
            params = {
                'deviceGuid': device_guid
            }

            class Output(ApertureOutputModel):
                is_out_of_compliance: bool = ApiField(alias='isOutOfCompliance')
                discovery_stage: int = ApiField(alias='discoveryStage')
                discovery_status: str = ApiField(alias='discoveryStatus')

            return generate_output(output_cls=Output, response=self._get(params=params))

    class _BulkOperations(ApertureEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.SetAgentlessDiscoveryToDo = self._SetAgentlessDiscoveryToDo(api_obj=self._api_obj, url=f'{self._url}/SetAgentlessDiscoveryToDo')
            self.ResetFailedAuthAttempts = self._ResetFailedAuthAttempts(api_obj=self._api_obj, url=f'{self._url}/resetFailedAuthAttempts')

        class _SetAgentlessDiscoveryToDo(ApertureEndpoint):
            def post(self, device_guids: List[str]):
                return generate_output(output_cls=ApertureOutputModel, response=self._post(data=device_guids))

        class _ResetFailedAuthAttempts(ApertureEndpoint):
            def post(self, device_guids: List[str]):
                return generate_output(output_cls=ApertureOutputModel, response=self._post(data=device_guids))
