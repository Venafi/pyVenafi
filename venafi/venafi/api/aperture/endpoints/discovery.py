from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.config import Config
from venafi.properties.response_objects.placement_rules import PlacementRules


class _Discovery:
    def __init__(self, aperture_obj):
        self.PlacementRules = self._PlacementRules(aperture_obj)

    class _PlacementRules(API):
        def __init__(self, aperture_obj):
            super().__init__(api_obj=aperture_obj, url='discovery/placementrules', valid_return_codes=[200])

        @property
        @json_response_property()
        def cert_location(self):
            return Config.Object(self._from_json(key='certLocation'), self._api_type)
        
        @property
        @json_response_property()
        def conditions(self):
            return [PlacementRules.Condition(condition) for condition in self._from_json(key='conditions')]
        
        @property
        @json_response_property()
        def device_location(self):
            return Config.Object(self._from_json(key='deviceLocation'), self._api_type)
        
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
            return Config.Object(self._from_json(key='ruleContainer'), self._api_type)

        @property
        @json_response_property()
        def type(self) -> str:
            return self._from_json(key='type')

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

            self.json_response = self._post(data=body)
            return self

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

            self.json_response = self._put(data=body)
            return self

        def Guid(self, guid: str):
            return self._Guid(guid=guid, aperture_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, aperture_obj):
                super().__init__(api_obj=aperture_obj, url=f'discovery/placementrules/{guid}', valid_return_codes=[200])

            @property
            @json_response_property()
            def cert_location(self):
                return Config.Object(self._from_json(key='certLocation'), self._api_type)

            @property
            @json_response_property()
            def conditions(self):
                return [PlacementRules.Condition(condition) for condition in self._from_json(key='conditions')]

            @property
            @json_response_property()
            def device_location(self):
                return Config.Object(self._from_json(key='deviceLocation'), self._api_type)

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
                return Config.Object(self._from_json(key='ruleContainer'), self._api_type)

            @property
            @json_response_property()
            def type(self) -> str:
                return self._from_json(key='type')

            def get(self):
                self.json_response = self._get()
                return self

            def delete(self):
                self.json_response = self._delete()
                return self
