from typing import List, Dict, Any
from urllib.parse import quote_plus
from pytpp.api.api_base import api_response_property
from pytpp.plugins.api.api_base import API, APIResponse


class _Reports(API):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reports'
        )

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
            @api_response_property
            def guid(self):
                return self._from_json()

        return _Response(response=self._post(data=body))
