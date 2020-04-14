from typing import List, Dict, Any
from venafi.properties.config import PlacementRulesAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class PlacementRules(FeatureBase):
    """
    This feature provides high-level interaction with TPP device objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._layout_rules_dn = r'\VED\Layout Root\Rules'

    def condition(self, field: str, comparison: str, value: Any):
        return {
            'field'     : field,
            'comparison': comparison,
            'value'     : value
        }

    def create(self, name: str, rules: List[Dict], device_location_dn: str, certificate_location_dn: str = None):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.post(
            name=name,
            conditions=rules,
            device_location_dn=device_location_dn,
            cert_location_dn=certificate_location_dn
        )
        rule = self._auth.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object

    def delete(self, guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).delete()
        response.assert_valid_response()

    def update(self, guid: str, rules: List[Dict] = None, device_location_dn: str = None, certificate_location_dn: str = None):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        rule = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).get()
        response = self._auth.aperture.Discovery.PlacementRules.put(
            guid=rule.guid,
            name=rule.name,
            conditions=rules or [r.__dict__ for r in rule.conditions],
            device_location_dn=device_location_dn or rule.device_location.dn,
            cert_location_dn=certificate_location_dn or rule.cert_location.dn
        )
        rule = self._auth.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object

    def get(self, guid: str):
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).get()
        response.assert_valid_response()
        return response
