from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import stats

class _Stats(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Stats')
        self.GetCounters = self._GetCounters(api_obj=self._api_obj, url=f'{self._url}/GetCounters')
        self.Query = self._Query(api_obj=self._api_obj, url=f'{self._url}/Query')

        self.CreateCounter = self._CreateCounter(api_obj=api_obj, url=f'{self._url}/CreateCounter')
        self.DeleteCounter = self._DeleteCounter(api_obj=api_obj, url=f'{self._url}/DeleteCounter')
        self.RenameCounter = self._RenameCounter(api_obj=api_obj, url=f'{self._url}/RenameCounter')
        self.UpdateCounter = self._UpdateCounter(api_obj=api_obj, url=f'{self._url}/UpdateCounter')
        self.GetCounter = self._GetCounter(api_obj=api_obj, url=f'{self._url}/GetCounter')
        self.CounterContainers = self._CounterContainers(api_obj=api_obj, url=f'{self._url}/CounterContainers')
        self.QueryTags = self._QueryTags(api_obj=api_obj, url=f'{self._url}/QueryTags')

    class _CreateCounter(WebSdkEndpoint):
        def post(
            self,
            stats_type: int = None,
            name: str = None,
            description: str = None,
            metadata_aname: str = None,
            metadata_bname: str = None,
            metadata_cname: str = None,
            value_description: str = None,
            sensitive: bool = None,
        ):
            body = {
                "StatsType"       : stats_type,
                "Name"            : name,
                "Description"     : description,
                "MetadataAName"   : metadata_aname,
                "MetadataBName"   : metadata_bname,
                "MetadataCName"   : metadata_cname,
                "ValueDescription": value_description,
                "Sensitive"       : sensitive,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteCounter(WebSdkEndpoint):
        def post(self, stats_type: int):
            body = {
                "StatsType": stats_type,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RenameCounter(WebSdkEndpoint):
        def post(self, stats_type: int, name: str):
            body = {
                "StatsType": stats_type,
                "Name"     : name,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UpdateCounter(WebSdkEndpoint):
        def post(
            self,
            stats_type: int = None,
            description: str = None,
            metadata_aname: str = None,
            metadata_bname: str = None,
            metadata_cname: str = None,
            value_description: str = None,
            sensitive: bool = None,
        ):
            body = {
                "StatsType"       : stats_type,
                "Description"     : description,
                "MetadataAName"   : metadata_aname,
                "MetadataBName"   : metadata_bname,
                "MetadataCName"   : metadata_cname,
                "ValueDescription": value_description,
                "Sensitive"       : sensitive,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetCounter(WebSdkEndpoint):
        def post(self, stats_type: int):
            body = {
                "StatsType": stats_type,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                counter: stats.Counter = ApiField(alias='Counter')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CounterContainers(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                counter_containers: list[stats.CounterContainer] = ApiField(alias='CounterContainers')

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _QueryTags(WebSdkEndpoint):
        def post(self, stats_type: int = None, filter: str = None, tag_number: int = None):
            body = {
                "StatsType": stats_type,
                "Filter"   : filter,
                "TagNumber": tag_number,
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                tag_a_values: list[str] = ApiField(alias='TagAValues')
                tag_b_values: list[str] = ApiField(alias='TagBValues')
                tag_c_values: list[str] = ApiField(alias='TagCValues')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetCounters(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                counters: list[stats.Counter] = ApiField(alias='Counters', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _Query(WebSdkEndpoint):
        def post(
            self, stats_type: str, tier: int, max_points: int, group_by_a: bool = None, group_by_b: bool = None,
            group_by_c: bool = None, filter_a: str = None, filter_b: str = None, filter_c: str = None
        ):
            body = {
                'StatsType': stats_type,
                'Tier'     : tier,
                'MaxPoints': max_points,
                'GroupByA' : group_by_a,
                'GroupByB' : group_by_b,
                'GroupByC' : group_by_c,
                'FilterA'  : filter_a,
                'FilterB'  : filter_b,
                'FilterC'  : filter_c
            }

            class Output(WebSdkOutputModel):
                results: list[stats.Result] = ApiField(alias='Results', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))
