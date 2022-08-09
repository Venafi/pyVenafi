from datetime import datetime
from typing import List, Dict, Any
from urllib.parse import quote_plus
from pytpp.api.api_base import ResponseFactory, ResponseField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.plugins.properties.response_objects.dataclasses import reports


class _Reports(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reports'
        )
        self.RunNow = self._RunNow(api_obj=api_obj)

    # noinspection ALL
    def post(self, name: str, title: str, inventory: str, summary: str = None, description: str = None,
             filter: Dict[str, List[Any]] = None, formats: List[str] = None, columns=None,
             skip_empty: bool = False):
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

        class Response(ApertureResponse):
            guid: str = ResponseField()

        return ResponseFactory(response_cls=Response, response=self._post(data=body), root_field='guid')

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, guid=guid)

    class _Guid(ApertureEndpoint):
        def __init__(self, api_obj, guid: str):
            super().__init__(api_obj=api_obj, url=f'/reports/{guid}')

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
                last_run: datetime = ResponseField(alias='lastRun')

            return ResponseFactory(response_cls=Response, response=self._get())

    class _RunNow:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(self._api_obj, guid=guid)

        class _Guid(ApertureEndpoint):
            def __init__(self, api_obj, guid: str):
                super().__init__(
                    api_obj=api_obj,
                    url=f'/reports/RunNow/{guid}'
                )

            def post(self):
                return ResponseFactory(response_cls=ApertureResponse, response=self._post(data={}))
