from typing import List

from pytpp.api.api_base import json_response_property
from pytpp.plugins.api.api_base import API, APIResponse
from pytpp.plugins.properties.response_objects.device import Device


class _Device(API):
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

        class _Response(APIResponse):
            def __init__(self, response, api_source):
                super().__init__(response=response, api_source=api_source)

            @property
            @json_response_property()
            def total_count(self):
                return int(self._from_json(key='totalCount'))

            @property
            @json_response_property()
            def devices_list_items(self):
                return [Device(device) for device in self._from_json(key='devicesListItems')]

        return _Response(response=self._post(data=body), api_source=self._api_source)

    class _GetStatus(API):
        def __init__(self, api_obj):
            super().__init__(
                api_obj=api_obj,
                url=f'/device/GetStatus'
            )

        def get(self, device_guid: str):
            params = {
                'deviceGuid': device_guid
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def is_out_of_compliance(self):
                    return bool(self._from_json(key='isOutOfCompliance'))

                @property
                @json_response_property()
                def discovery_stage(self):
                    return int(self._from_json(key='discoveryStage'))

                @property
                @json_response_property()
                def discovery_status(self):
                    return self._from_json(key='discoveryStatus')

            return _Response(response=self._get(params=params), api_source=self._api_source)

    class _BulkOperations:
        def __init__(self, api_obj):
            self._api_obj = api_obj
            self.SetAgentlessDiscoveryToDo = self._SetAgentlessDiscoveryToDo(api_obj=self._api_obj)
            self.ResetFailedAuthAttempts = self._ResetFailedAuthAttempts(api_obj=self._api_obj)

        class _SetAgentlessDiscoveryToDo(API):
            def __init__(self, api_obj):
                super().__init__(
                    api_obj=api_obj,
                    url=f'/device/bulkOperations/SetAgentlessDiscoveryToDo'
                )

            def post(self, device_guids: List[str]):
                return APIResponse(response=self._post(data=device_guids), api_source=self._api_source)

        class _ResetFailedAuthAttempts(API):
            def __init__(self, api_obj):
                super().__init__(
                    api_obj=api_obj,
                    url=f'/device/bulkOperations/resetFailedAuthAttempts'
                )

            def post(self, device_guids: List[str]):
                return APIResponse(response=self._post(data=device_guids), api_source=self._api_source)
