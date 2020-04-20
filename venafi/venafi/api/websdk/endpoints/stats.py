from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.stats import Stats


class _Stats:
    def __init__(self, websdk_obj):
        self.GetCounters = self._GetCounters(websdk_obj=websdk_obj)
        self.Query = self._Query(websdk_obj=websdk_obj)
    
    class _GetCounters(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='Stats/GetCounters')

        def post(self):
            
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def counters(self):
                    return [Stats.Counter(counter) for counter in self._from_json(key='Counters')]

                @property
                @json_response_property()
                def error(self) -> str:
                    return self._from_json(key='Error')

            return _Response(
                response=self._post(data={}),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Query(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='Stats/Query')

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

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def results(self):
                    return [Stats.Result(result) for result in self._from_json(key='Results')]

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )
