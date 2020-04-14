from typing import List, Dict, Any
from venafi.properties.config import PlacementRulesAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class PlacementRules(FeatureBase):
    """
    This feature provides high-level interaction with TPP Placement Rule objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._layout_rules_dn = r'\VED\Layout Root\Rules'

    @staticmethod
    def condition(field: str, comparison: str, value: Any):
        """
        Args:
            field: Certificate or device attribute.
            comparison: Comparator.
            value: Value to compare.

        Returns:
            Dictionary that can be used when creating or modifying a placement rule.
        """
        return {
            'field'     : field,
            'comparison': comparison,
            'value'     : value
        }

    def create(self, name: str, conditions: List[Dict], device_location_dn: str, certificate_location_dn: str = None):
        """
        Creates a placement rule.

        Examples:

            .. code-block:: python

                features.placement_rules.create(
                    name='My favorite placement rule',
                    conditions=[
                        features.placement_rules.condition(
                            field=AttributeValues.PlacementRules.Field.country,
                            comparison=AttributeValues.PlacementRules.Condition.matches,
                            value='US'
                        ),
                        features.placement_rules.condition(
                            field=AttributeValues.PlacementRules.Field.common_name,
                            comparison=AttributeValues.PlacementRules.Condition.ends_with,
                            value='venafi.com'
                        )
                    ],
                    device_location_dn=r'\VED\Policy\Installations',
                    certificate_location_dn=r'\VED\Policy\Certificates\Venafi'
                )

        Args:
            name: Name of the placement rule.
            conditions: The conditional logic that defines the rule. Requires a specific dictionary with `field`, `comparison`,
                        and `value` keys. Alternatively, use the ``condition`` method to create the condition dictionary.
            device_location_dn: Absolute path to folder that should received all device and application objects that apply to
                                this rule.
            certificate_location_dn: Absolute path to folder that should received all certificate objects that apply to this
                                     rule.

        Returns:
            Config object of the placement rule.
        """
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.post(
            name=name,
            conditions=conditions,
            device_location_dn=device_location_dn,
            cert_location_dn=certificate_location_dn
        )
        rule = self._auth.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object

    def delete(self, guid: str):
        """
        Deletes a placement rule.

        Args:
            guid: GUID of the placement rule.
        """
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).delete()
        response.assert_valid_response()

    def update(self, guid: str, conditions: List[Dict] = None, device_location_dn: str = None, certificate_location_dn: str = None):
        """
        Updates a placement rule. If certain parameters are not provided, the current corresponding settings will be assumed to
        be rewritten to the object. In other words, only the parameters given are updated.

        Examples:

            .. code-block:: python

                features.placement_rules.update(
                    guid=rule.guid,
                    conditions=[
                        features.placement_rules.condition(
                            field=AttributeValues.PlacementRules.Field.country,
                            comparison=AttributeValues.PlacementRules.Condition.matches,
                            value='US'
                        ),
                        features.placement_rules.condition(
                            field=AttributeValues.PlacementRules.Field.common_name,
                            comparison=AttributeValues.PlacementRules.Condition.ends_with,
                            value='venafi.com'
                        )
                    ],
                    device_location_dn=r'\VED\Policy\Installations',
                    certificate_location_dn=r'\VED\Policy\Certificates\Venafi'
                )

        Args:
            guid: Name of the placement rule.
            conditions: The conditional logic that defines the rule. Requires a specific dictionary with `field`, `comparison`,
                        and `value` keys. Alternatively, use the ``condition`` method to create the condition dictionary.
            device_location_dn: Absolute path to folder that should received all device and application objects that apply to
                                this rule.
            certificate_location_dn: Absolute path to folder that should received all certificate objects that apply to this
                                     rule.

        Returns:
            Config object of the placement rule.
        """
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        rule = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).get()
        response = self._auth.aperture.Discovery.PlacementRules.put(
            guid=rule.guid,
            name=rule.name,
            conditions=conditions or [c.__dict__ for c in rule.conditions],
            device_location_dn=device_location_dn or rule.device_location.dn,
            cert_location_dn=certificate_location_dn or rule.cert_location.dn
        )
        rule = self._auth.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object

    def get(self, guid: str):
        """
        Args:
            guid: GUID of the placement rule.

        Returns:
            Placement rule attributes.
        """
        if self._auth.preference == ApiPreferences.websdk:
            self._log_not_implemented_warning(ApiPreferences.websdk)

        response = self._auth.aperture.Discovery.PlacementRules.Guid(guid=guid).get()
        response.assert_valid_response()
        return response
