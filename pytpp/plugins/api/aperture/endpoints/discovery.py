from pytpp.api.api_base import ResponseFactory, ResponseField
from pytpp.plugins.api.api_base import ApertureEndpoint, ApertureResponse
from pytpp.plugins.properties.response_objects.dataclasses import config
from pytpp.plugins.properties.response_objects.dataclasses import placement_rules
from typing import List


class _Discovery:
    def __init__(self, api_obj):
        self.PlacementRules = self._PlacementRules(api_obj)

    class _PlacementRules(ApertureEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='discovery/placementrules')

        def post(self, name: str, conditions: List[dict], device_location_dn: dict, cert_location_dn: dict = None):
            body = {
                'name'          : name,
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
                'type'          : 'Certificate' if cert_location_dn else 'Ssh'
            }

            class Response(ApertureResponse):
                cert_location: config.Object = ResponseField(alias='certLocation')
                conditions: List[placement_rules.Condition] = ResponseField(alias='conditions', default_factory=list)
                device_location: config.Object = ResponseField(alias='deviceLocation')
                guid: str = ResponseField(alias='id')
                index: str = ResponseField(alias='index')
                name: str = ResponseField(alias='name')
                rule_container: config.Object = ResponseField(alias='ruleContainer')
                type: str = ResponseField(alias='type')

            return ResponseFactory(response_cls=Response, response=self._post(data=body))

        def put(self, guid: str, name: str, conditions: List[dict], device_location_dn: dict, cert_location_dn: dict = None):
            body = {
                'id'            : guid,
                'name'          : name,
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
                'type'          : 'Certificate' if cert_location_dn else 'Ssh'
            }

            class Response(ApertureResponse):
                cert_location: config.Object = ResponseField(alias='certLocation')
                conditions: List[placement_rules.Condition] = ResponseField(alias='conditions', default_factory=list)
                device_location: config.Object = ResponseField(alias='deviceLocation')
                guid: str = ResponseField(alias='id')
                index: str = ResponseField(alias='index')
                name: str = ResponseField(alias='name')
                rule_container: config.Object = ResponseField(alias='ruleContainer')
                type: str = ResponseField(alias='type')

            return ResponseFactory(response_cls=Response, response=self._put(data=body))

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(ApertureEndpoint):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'discovery/placementrules/{guid}')

            def get(self):
                class Response(ApertureResponse):
                    cert_location: config.Object = ResponseField(alias='certLocation')
                    conditions: List[placement_rules.Condition] = ResponseField(alias='conditions', default_factory=list)
                    device_location: config.Object = ResponseField(alias='deviceLocation')
                    dn: str = ResponseField(alias='dn')
                    guid: str = ResponseField(alias='id')
                    index: str = ResponseField(alias='index')
                    name: str = ResponseField(alias='name')
                    rule_container: config.Object = ResponseField(alias='ruleContainer')
                    type: str = ResponseField(alias='type')

                return ResponseFactory(response_cls=Response, response=self._get())

            def delete(self):
                class Response(ApertureResponse):
                    def __init__(self, response, api_source):
                        super().__init__(response=response, api_source=api_source)

                return ResponseFactory(response_cls=Response, response=self._delete())
