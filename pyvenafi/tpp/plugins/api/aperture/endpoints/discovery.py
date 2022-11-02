from pyvenafi.tpp.api.api_base import generate_output, ApiField
from pyvenafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from pyvenafi.tpp.plugins.api.aperture.models import config
from pyvenafi.tpp.plugins.api.aperture.models import placement_rules
from typing import List


class _Discovery(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/discovery')
        self.PlacementRules = self._PlacementRules(api_obj=self._api_obj, url=f'{self._url}/placementrules')

    class _PlacementRules(ApertureEndpoint):
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

            class Output(ApertureOutputModel):
                cert_location: config.Object = ApiField(alias='certLocation')
                conditions: List[placement_rules.Condition] = ApiField(alias='conditions', default_factory=list)
                device_location: config.Object = ApiField(alias='deviceLocation')
                guid: str = ApiField(alias='id')
                index: str = ApiField(alias='index')
                name: str = ApiField(alias='name')
                rule_container: config.Object = ApiField(alias='ruleContainer')
                type: str = ApiField(alias='type')

            return generate_output(output_cls=Output, response=self._post(data=body))

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

            class Output(ApertureOutputModel):
                cert_location: config.Object = ApiField(alias='certLocation')
                conditions: List[placement_rules.Condition] = ApiField(alias='conditions', default_factory=list)
                device_location: config.Object = ApiField(alias='deviceLocation')
                guid: str = ApiField(alias='id')
                index: str = ApiField(alias='index')
                name: str = ApiField(alias='name')
                rule_container: config.Object = ApiField(alias='ruleContainer')
                type: str = ApiField(alias='type')

            return generate_output(output_cls=Output, response=self._put(data=body))

        def Guid(self, guid: str):
            return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(ApertureEndpoint):
            def get(self):
                class Output(ApertureOutputModel):
                    cert_location: config.Object = ApiField(alias='certLocation')
                    conditions: List[placement_rules.Condition] = ApiField(alias='conditions', default_factory=list)
                    device_location: config.Object = ApiField(alias='deviceLocation')
                    dn: str = ApiField(alias='dn')
                    guid: str = ApiField(alias='id')
                    index: str = ApiField(alias='index')
                    name: str = ApiField(alias='name')
                    rule_container: config.Object = ApiField(alias='ruleContainer')
                    type: str = ApiField(alias='type')

                return generate_output(output_cls=Output, response=self._get())

            def delete(self):
                class Output(ApertureOutputModel):
                    def __init__(self, response, api_source):
                        super().__init__(response=response, api_source=api_source)

                return generate_output(output_cls=Output, response=self._delete())
