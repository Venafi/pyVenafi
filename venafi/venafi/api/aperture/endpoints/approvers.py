from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.identity import Identity


class _Approvers(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/approvers')

    def get(self, name_filter: str):
        params = {
            'filter': name_filter
        }
        
        class _Response(APIResponse):
            def __init__(self, response, api_source):
                super().__init__(
                    response=response, 
                    api_source=api_source
                )
            
            @property
            @json_response_property()
            def identities(self):
                return [Identity.Identity(i, api_type=self._api_source) for i in self._from_json()]
            
        return _Response(
            response=self._get(params=params),
            api_source=self._api_source
        )
