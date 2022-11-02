from datetime import datetime
from typing import List, Dict, Any
from urllib.parse import quote_plus
from pyvenafi.tpp.api.api_base import generate_output, ApiField
from pyvenafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pyvenafi.tpp.plugins.api.aperture.models import reports


class _Reports(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/reports')
        self.RunNow = self._RunNow(api_obj=self._api_obj, url=f'{self._url}/RunNow')

    # noinspection ALL
    def post(self, name: str, title: str, inventory: str, summary: str = None, description: str = None,
             filter: Dict[str, List[Any]] = None, formats: List[str] = None, columns=None,
             skip_empty: bool = False):
        encoded_filter = None
        if isinstance(filter, dict):
            encoded_filter = "/".join(f"{k}:{quote_plus(v)}" for k, values in filter.items() for v in values)
        body = {
            "name"       : name,
            "title"      : title,
            "inventory"  : inventory,
            "summary"    : summary,
            "description": description,
            "filter"     : encoded_filter,
            "formats"    : formats,
            "columns"    : columns,
            "skipEmpty"  : skip_empty
        }

        class Output(ApertureOutputModel):
            guid: str = ApiField()

        return generate_output(output_cls=Output, response=self._post(data=body), root_field='guid')

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

    class _Guid(ApertureEndpoint):
        def get(self):
            class Output(ApertureOutputModel):
                name: str = ApiField(alias='name')
                title: str = ApiField(alias='title')
                inventory: str = ApiField(alias='inventory')
                summary: str = ApiField(alias='summary')
                status: str = ApiField(alias='status')
                filter: str = ApiField(alias='filter')
                columns: List[reports.Column] = ApiField(alias='columns', default_factory=list)
                personalized: str = ApiField(alias='personalized')
                location: str = ApiField(alias='location')
                dn: str = ApiField(alias='dn')
                guid: str = ApiField(alias='id')
                disabled: bool = ApiField(alias='disabled')
                description: str = ApiField(alias='description')
                last_run: datetime = ApiField(alias='lastRun')
                downloadable_formats: List[str] = ApiField(alias='downloadableFormats', default_factory=list)

            return generate_output(output_cls=Output, response=self._get())

    class _RunNow(ApertureEndpoint):
        def Guid(self, guid: str):
            return self._Guid(self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(ApertureEndpoint):
            def post(self):
                return generate_output(output_cls=ApertureOutputModel, response=self._post(data={}))
