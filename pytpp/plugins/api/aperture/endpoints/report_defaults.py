from pytpp.api.api_base import ApiField, generate_output
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pytpp.plugins.api.aperture.outputs import reports
from typing import List


class _ReportDefaults(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reportdefaults/certificates'
        )

    def get(self):
        class Response(ApertureOutputModel):
            name: str = ApiField(alias='name')
            title: str = ApiField(alias='title')
            inventory: str = ApiField(alias='inventory')
            summary: str = ApiField(alias='summary')
            status: str = ApiField(alias='status')
            filter: str = ApiField(alias='filter')
            columns: List[reports.Column] = ApiField(alias='columns')
            personalized: str = ApiField(alias='personalized')
            location: str = ApiField(alias='location')
            dn: str = ApiField(alias='dn')
            guid: str = ApiField(alias='id')
            disabled: bool = ApiField(alias='disabled')
            description: str = ApiField(alias='description')

        return generate_output(response_cls=Response, response=self._get())
