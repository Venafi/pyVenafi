from pytpp.api.api_base import ResponseField, ResponseFactory
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.plugins.properties.response_objects.dataclasses import reports
from typing import List


class _ReportDefaults(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reportdefaults/certificates'
        )

    def get(self):
        class Response(ApertureResponse):
            name: str = ResponseField(alias='name')
            title: str = ResponseField(alias='title')
            inventory: str = ResponseField(alias='inventory')
            summary: str = ResponseField(alias='summary')
            status: str = ResponseField(alias='status')
            filter: str = ResponseField(alias='filter')
            columns: List[reports.Column] = ResponseField(alias='columns')
            personalized: str = ResponseField(alias='personalized')
            location: str = ResponseField(alias='location')
            dn: str = ResponseField(alias='dn')
            guid: str = ResponseField(alias='id')
            disabled: bool = ResponseField(alias='disabled')
            description: str = ResponseField(alias='description')

        return ResponseFactory(response_cls=Response, response=self._get())
