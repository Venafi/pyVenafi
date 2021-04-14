from typing import List, Dict
from venafi.plugins.api.api_base import API, APIResponse, json_response_property
from venafi.plugins.properties.certificate_inventory import Field, Filter
from venafi.plugins.properties.response_objects.certificate_inventory import CertificateDetails


class _Certificates:
    def __init__(self, api_obj):
        self.Filters = self._Filters(api_obj=api_obj)

    class _Filters:
        def __init__(self, api_obj):
            self.Apply = self._Apply(api_obj=api_obj)

        class _Apply(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='certificates/filters/apply')

            def post(self, fields: List[str] = None, filters: Dict[str, List] = None, is_sort_ascending: bool = True,
                     limit: int = 100, offset: int = 0, sort_field: str = 'Name'):
                fields = fields or [
                        Field.allowed_app_type,
                        Field.aperture_status,
                        Field.dn,
                        Field.error_details,
                        Field.id,
                        Field.installations,
                        Field.is_rename_allowed,
                        Field.key_size,
                        Field.name,
                        Field.risks,
                        Field.single_click_actions,
                        Field.status_details,
                        Field.tls_endpoints,
                        Field.valid_to,
                    ]
                filters = filters or {
                    Filter.status: ["Managed"]
                }
                body = {
                    'fields': fields,
                    'filters': filters,
                    'isSortAscending': is_sort_ascending,
                    'limit': limit,
                    'offset': offset,
                    'sortField': sort_field
                }

                class _Response(APIResponse):
                    def __init__(self, response, api_source):
                        super().__init__(response=response, api_source=api_source)
                        
                    @property
                    @json_response_property()
                    def certificates(self):
                        return [CertificateDetails(cert) for cert in self._from_json()]

                return _Response(response=self._post(data=body), api_source=self._api_source)
