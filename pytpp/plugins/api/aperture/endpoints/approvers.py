from api.api_base import ResponseFactory, ResponseField
from plugins.properties.response_objects.dataclasses import identity
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from typing import List


class _Approvers(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/approvers')

    def get(self, name_filter: str):
        params = {
            'filter': name_filter
        }
        
        class Response(ApertureResponse):
            identities: List[identity.Identity] = ResponseField()
            
        return ResponseFactory(response_cls=Response, response=self._get(params=params), root_field='identities')
