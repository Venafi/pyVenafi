from typing import List
from pytpp.api.websdk.outputs import stats
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Stats:
    def __init__(self, api_obj):
        self.GetCounters = self._GetCounters(api_obj=api_obj)
        self.Query = self._Query(api_obj=api_obj)
    
    class _GetCounters(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Stats/GetCounters')

        def post(self):
            class Response(WebSdkOutputModel):
                counters: List[stats.Counter] = ApiField(alias='Counters', default_factory=list)

            return generate_output(response_cls=Response, response=self._post(data={}))

    class _Query(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Stats/Query')

        def post(self, stats_type: str, tier: int, max_points: int, group_by_a: bool = None, group_by_b: bool = None,
                 group_by_c: bool = None, filter_a: str = None, filter_b: str = None, filter_c: str = None):
            body = {
                'StatsType': stats_type,
                'Tier': tier,
                'MaxPoints': max_points,
                'GroupByA': group_by_a,
                'GroupByB': group_by_b,
                'GroupByC': group_by_c,
                'FilterA': filter_a,
                'FilterB': filter_b,
                'FilterC': filter_c
            }

            class Response(WebSdkOutputModel):
                results: List[stats.Result] = ApiField(alias='Results', default_factory=list)

            return generate_output(response_cls=Response, response=self._post(data=body))
