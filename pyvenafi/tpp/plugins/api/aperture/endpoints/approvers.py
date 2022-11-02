from pyvenafi.tpp.api.api_base import generate_output, ApiField
from pyvenafi.tpp.plugins.api.aperture.models import identity
from pyvenafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from typing import List


class _Approvers(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/approvers')

    def get(self, name_filter: str):
        params = {
            'filter': name_filter
        }

        class Output(ApertureOutputModel):
            identities: List[identity.Identity] = ApiField(default_factory=list)

        return generate_output(output_cls=Output, response=self._get(params=params), root_field='identities')
