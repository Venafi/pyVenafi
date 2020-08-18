from typing import List
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.config import Config
from venafi.properties.response_objects.placement_rules import PlacementRules


class _Discovery:
    def __init__(self, api_obj):
        self.PlacementRules = self._PlacementRules(api_obj)

    class _PlacementRules(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='discovery/placementrules')

        def post(self, name: str, conditions: List[dict], device_location_dn: dict, cert_location_dn: dict = None):
            body = {
                'name': name,
                'certLocation'  : {
                    'dn': cert_location_dn
                },
                'conditions'    : conditions,
                'deviceLocation': {
                    'dn': device_location_dn
                },
                'ruleContainer' : {
                    'dn': r'\VED\Layout Root\Rules'
                },
                'type': 'Certificate' if cert_location_dn else 'Ssh'
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def cert_location(self):
                    return Config.Object(self._from_json(key='certLocation'), self._api_source)

                @property
                @json_response_property()
                def conditions(self):
                    return [PlacementRules.Condition(condition) for condition in self._from_json(key='conditions')]

                @property
                @json_response_property()
                def device_location(self):
                    return Config.Object(self._from_json(key='deviceLocation'), self._api_source)

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='id')

                @property
                @json_response_property()
                def index(self) -> str:
                    return self._from_json(key='index')

                @property
                @json_response_property()
                def name(self) -> str:
                    return self._from_json(key='name')

                @property
                @json_response_property()
                def rule_container(self):
                    return Config.Object(self._from_json(key='ruleContainer'), self._api_source)

                @property
                @json_response_property()
                def type(self) -> str:
                    return self._from_json(key='type')

            return _Response(response=self._post(data=body), api_source=self._api_source)

        def put(self, guid: str, name: str, conditions: List[dict], device_location_dn: dict, cert_location_dn: dict = None):
            body = {
                'id': guid,
                'name': name,
                'certLocation'  : {
                    'dn': cert_location_dn
                },
                'conditions'    : conditions,
                'deviceLocation': {
                    'dn': device_location_dn
                },
                'ruleContainer' : {
                    'dn': r'\VED\Layout Root\Rules'
                },
                'type': 'Certificate' if cert_location_dn else 'Ssh'
            }

            class _Response(APIResponse):
                def __init__(self, response, api_source):
                    super().__init__(response=response, api_source=api_source)

                @property
                @json_response_property()
                def cert_location(self):
                    return Config.Object(self._from_json(key='certLocation'), self._api_source)

                @property
                @json_response_property()
                def conditions(self):
                    return [PlacementRules.Condition(condition) for condition in self._from_json(key='conditions')]

                @property
                @json_response_property()
                def device_location(self):
                    return Config.Object(self._from_json(key='deviceLocation'), self._api_source)

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='id')

                @property
                @json_response_property()
                def index(self) -> str:
                    return self._from_json(key='index')

                @property
                @json_response_property()
                def name(self) -> str:
                    return self._from_json(key='name')

                @property
                @json_response_property()
                def rule_container(self):
                    return Config.Object(self._from_json(key='ruleContainer'), self._api_source)

                @property
                @json_response_property()
                def type(self) -> str:
                    return self._from_json(key='type')

            return _Response(response=self._put(data=body), api_source=self._api_source)

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'discovery/placementrules/{guid}')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response, api_source):
                        super().__init__(response=response, api_source=api_source)

                    @property
                    @json_response_property()
                    def cert_location(self):
                        return Config.Object(self._from_json(key='certLocation'), self._api_source)

                    @property
                    @json_response_property()
                    def conditions(self):
                        return [PlacementRules.Condition(condition) for condition in self._from_json(key='conditions')]

                    @property
                    @json_response_property()
                    def device_location(self):
                        return Config.Object(self._from_json(key='deviceLocation'), self._api_source)

                    @property
                    @json_response_property()
                    def dn(self) -> str:
                        return self._from_json(key='dn')

                    @property
                    @json_response_property()
                    def guid(self) -> str:
                        return self._from_json(key='id')

                    @property
                    @json_response_property()
                    def index(self) -> str:
                        return self._from_json(key='index')

                    @property
                    @json_response_property()
                    def name(self) -> str:
                        return self._from_json(key='name')

                    @property
                    @json_response_property()
                    def rule_container(self):
                        return Config.Object(self._from_json(key='ruleContainer'), self._api_source)

                    @property
                    @json_response_property()
                    def type(self) -> str:
                        return self._from_json(key='type')

                return _Response(response=self._get(), api_source=self._api_source)

            def delete(self):
                class _Response(APIResponse):
                    def __init__(self, response, api_source):
                        super().__init__(response=response, api_source=api_source)

                return _Response(response=self._delete(), api_source=self._api_source)
