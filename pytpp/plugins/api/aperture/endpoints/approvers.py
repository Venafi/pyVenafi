from pytpp.api.api_base import generate_output, ApiField
from pytpp.plugins.api.aperture.outputs import identity
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from typing import List


class _Approvers(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/approvers')

    def get(self, name_filter: str):
        params = {
            'filter': name_filter
        }
        
        class Response(ApertureOutputModel):
            identities: List[identity.Identity] = ApiField()
            
        return generate_output(output_cls=Response, response=self._get(params=params), root_field='identities')
