from typing import List 
from venafi.api.api_base import API, APIResponse, json_response_property


class _Discovery:
    def __init__(self, websdk_obj):
        self._websdk_obj = websdk_obj
        self.Import = self._Import(websdk_obj=websdk_obj)

    def Guid(self, guid: str):
        return self._Guid(guid=guid, websdk_obj=self._websdk_obj)

    class _Guid(API):
        def __init__(self, guid: str, websdk_obj):
            super().__init__(api_obj=websdk_obj, url=f'/Discovery/{guid}')

        def delete(self):
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def success(self) -> bool:
                    return self._from_json('Success')

            return _Response(
                response=self._delete(),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Import(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Discovery/Import')

        def post(self, endpoints: list, zone_name: str):
            body = {
                'zoneName': zone_name,
                'endpoints': endpoints
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def created_certificates(self) -> int:
                    return self._from_json('createdCertificates')

                @property
                @json_response_property()
                def created_instances(self) -> int:
                    return self._from_json('createdInstances')

                @property
                @json_response_property()
                def updated_certificates(self) -> int:
                    return self._from_json('updatedCertificates')

                @property
                @json_response_property()
                def updated_instances(self) -> int:
                    return self._from_json('updatedInstances')

                @property
                @json_response_property()
                def warnings(self) -> List[str]:
                    return self._from_json('warnings')

                @property
                @json_response_property()
                def zone_name(self) -> str:
                    return self._from_json('zoneName')

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

