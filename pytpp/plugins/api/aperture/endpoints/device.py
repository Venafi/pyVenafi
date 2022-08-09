from pytpp.api.api_base import ResponseField, ResponseFactory
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.plugins.properties.response_objects.dataclasses import device
from typing import List


class _Device(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/device'
        )

        self.BulkOperations = self._BulkOperations(api_obj)
        self.GetStatus = self._GetStatus(api_obj)

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

        class Response(ApertureResponse):
            total_count: int = ResponseField(key='totalCount')
            devices_list_items: List[device.Device] = ResponseField(alias='devicesListItems', default_factory=list)

        return Response(response_cls=Response, response=self._post(data=body))

    class _GetStatus(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url=f'/device/GetStatus'
            )

        def get(self, device_guid: str):
            params = {
                'deviceGuid': device_guid
            }

            class Response(ApertureResponse):
                is_out_of_compliance: bool = ResponseField(alias='isOutOfCompliance')
                discovery_stage: int = ResponseField(alias='discoveryStage')
                discovery_status: str = ResponseField(alias='discoveryStatus')

            return Response(response_cls=Response, response=self._get(params=params))

    class _BulkOperations:
        def __init__(self, api_obj):
            self._api_obj = api_obj
            self.SetAgentlessDiscoveryToDo = self._SetAgentlessDiscoveryToDo(api_obj=self._api_obj)
            self.ResetFailedAuthAttempts = self._ResetFailedAuthAttempts(api_obj=self._api_obj)

        class _SetAgentlessDiscoveryToDo(ApertureEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url=f'/device/bulkOperations/SetAgentlessDiscoveryToDo')

            def post(self, device_guids: List[str]):
                return ResponseFactory(response_cls=ApertureResponse, response=self._post(data=device_guids))

        class _ResetFailedAuthAttempts(ApertureEndpoint):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url=f'/device/bulkOperations/resetFailedAuthAttempts')

            def post(self, device_guids: List[str]):
                return ResponseFactory(response_cls=ApertureResponse, response=self._post(data=device_guids))
