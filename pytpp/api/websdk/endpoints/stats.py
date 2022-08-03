from typing import List
from properties.response_objects.dataclasses import stats
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField


class _Stats:
    def __init__(self, api_obj):
        self.GetCounters = self._GetCounters(api_obj=api_obj)
        self.Query = self._Query(api_obj=api_obj)
    
    class _GetCounters(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Stats/GetCounters')

        def post(self):
            class Response(APIResponse):
                counters: List[stats.Counter] = ResponseField(alias='Counters', default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._post(data={}))

    class _Query(API):
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

            class Response(APIResponse):
                results: List[stats.Result] = ResponseField(alias='Results', default_factory=list)

            return ResponseFactory(response_cls=Response, response=self._post(data=body))
