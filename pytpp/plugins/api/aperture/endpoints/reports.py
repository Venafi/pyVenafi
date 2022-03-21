from typing import List, Dict, Any
from urllib.parse import quote_plus
from pytpp.api.api_base import api_response_property
from pytpp.plugins.api.api_base import API, APIResponse
from pytpp.plugins.properties.response_objects.reports import Report
from pytpp.tools.helpers.date_converter import from_date_string


class _Reports(API):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reports'
        )
        self.RunNow = self._RunNow(api_obj=api_obj)

    def post(self, name: str, title: str, inventory: str, summary: str = None, description: str = None, filter: Dict[str, List[Any]] = None, formats: List[str] = None, columns = None, skip_empty: bool = False):
        encoded_filter = "/".join(f"{k}:{quote_plus(v)}" for k,values in filter.items() for v in values)
        body = {
            "name" : name,
            "title": title,
            "inventory": inventory,
            "summary": summary,
            "description": description,
            "filter": encoded_filter,
            "formats": formats,
            "columns": columns,
            "skipEmpty": skip_empty
        }

        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response, api_source='aperture')

            @property
            @api_response_property()
            def guid(self):
                return self._from_json()

        return _Response(response=self._post(data=body))

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, guid=guid)

    class _Guid(API):
        def __init__(self, api_obj, guid: str):
            super().__init__(api_obj=api_obj, url=f'/reports/{guid}')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response, api_source='aperture')

                @property
                @api_response_property()
                def name(self) -> str:
                    return self._from_json(key='name')

                @property
                @api_response_property()
                def title(self) -> str:
                    return self._from_json(key='title')

                @property
                @api_response_property()
                def inventory(self) -> str:
                    return self._from_json(key='inventory')

                @property
                @api_response_property()
                def summary(self) -> str:
                    return self._from_json(key='summary')

                @property
                @api_response_property()
                def status(self) -> str:
                    return self._from_json(key='status')

                @property
                @api_response_property()
                def filter(self) -> str:
                    return self._from_json(key='filter')

                @property
                @api_response_property()
                def columns(self):
                    return [Report.Column(c) for c in self._from_json(key='columns')]

                @property
                @api_response_property()
                def personalized(self) -> str:
                    return self._from_json(key='personalized')

                @property
                @api_response_property()
                def location(self) -> str:
                    return self._from_json(key='location')

                @property
                @api_response_property()
                def description(self) -> str:
                    return self._from_json(key='description')

                @property
                @api_response_property()
                def disabled(self) -> str:
                    return self._from_json(key='disabled')

                @property
                @api_response_property()
                def guid(self) -> str:
                    return self._from_json(key='id')

                @property
                @api_response_property()
                def dn(self) -> str:
                    return self._from_json(key='dn')
                
                @property
                @api_response_property()
                def last_run(self):
                    return from_date_string(self._from_json(key='lastRun'))

            return _Response(response=self._get())


    class _RunNow:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(self._api_obj, guid=guid)

        class _Guid(API):
            def __init__(self, api_obj, guid: str):
                super().__init__(
                    api_obj=api_obj,
                    url=f'/reports/RunNow/{guid}'
                )

            def post(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response, api_source='aperture')

                return _Response(response=self._post(data={}))
