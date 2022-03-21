from pytpp.api.api_base import api_response_property
from pytpp.plugins.api.api_base import API, APIResponse
from pytpp.plugins.properties.response_objects.reports import Report


class _ReportDefaults(API):
    def __init__(self, api_obj):
        super().__init__(
            api_obj=api_obj,
            url=f'/reportdefaults/certificates'
        )

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

        return _Response(response=self._get())
