from typing import TYPE_CHECKING, List, Union
if TYPE_CHECKING:
    from pytpp.plugins import Authenticate
import json
from pytpp.tools.vtypes import Config
from pytpp.features.bases.feature_base import feature
from pytpp.features.placement_rules import PlacementRules as _OriginalPlacementRules, \
    PlacementRuleCondition as _OriginalPlacementRuleCondition


@feature(_OriginalPlacementRuleCondition.__feature__)
class PlacementRuleCondition(_OriginalPlacementRuleCondition):
    def __init__(self):
        pass

    @property
    def city(self):
        return self._Operators(field='L')

    @property
    def common_name(self):
        return self._Operators(field='CN')

    @property
    def country(self):
        return self._Operators(field='C')

    @property
    def domain_component(self):
        return self._Operators(field='DC')

    @property
    def expired(self):
        return self._Operators(field='CertificateExpired')

    @property
    def hostname(self):
        return self._Operators(field='HostName')

    @property
    def ip_address(self):
        return self._Operators(field='IPAddress')

    @property
    def issuer_dn(self):
        return self._Operators(field='IssuerDN')

    @property
    def operating_system(self):
        return self._Operators(field='OperatingSystem')

    @property
    def organization(self):
        return self._Operators(field='O')

    @property
    def organizational_unit(self):
        return self._Operators(field='OU')

    @property
    def port(self):
        return self._Operators(field='Port')

    @property
    def san(self):
        return self._Operators(field='SubjectAltNameDNS')

    @property
    def self_signed(self):
        return self._Operators(field='CertificateSelfSigned')

    @property
    def server_version(self):
        return self._Operators(field='ServerVersion')

    @property
    def state(self):
        return self._Operators(field='S')

    @property
    def supports_ssh_v1(self):
        return self._Operators(field='SupportsSsHv1')

    @property
    def supports_ssh_v2(self):
        return self._Operators(field='SupportsSsHv2')

    class _Operators:
        def __init__(self, field: str, force_value: str = None):
            self._field = field
            self._forced_value = force_value

        @staticmethod
        def _condition(field: str, comparison: str, value: str):
            return json.dumps({
                'field': field,
                'comparison': comparison,
                'value': value
            })

        def matches(self, value: str):
            """
            Args:
                value: String to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='Matches',
                value=value
            )

        def in_list(self, values: List[str]):
            """
            Args:
                values: List of strings to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='In',
                value=','.join(map(str, values))
            )

        def starts_with(self, value: str):
            """
            Args:
                value: String that the target field's value begins with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='StartsWith',
                value=value
            )

        def ends_with(self, value: str):
            """
            Args:
                value: String that the target field's value ends with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='EndsWith',
                value=value
            )

        def contains(self, value: str):
            """
            Args:
                value: String within the target field's value.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='Contains',
                value=value
            )

        def matches_regex(self, value: str):
            """
            Args:
                value: String to match by regular expression.

            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='MatchesRegex',
                value=value
            )

        def is_true(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='IsTrue',
                value=""
            )

        def is_false(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            return self._condition(
                field=self._field,
                comparison='IsFalse',
                value=""
            )


@feature(_OriginalPlacementRules.__feature__)
class PlacementRules(_OriginalPlacementRules):
    """
    This feature provides high-level interaction with TPP Placement Rule objects.
    """

    def __init__(self, api: 'Authenticate'):
        super().__init__(api=api)
        if TYPE_CHECKING:
            self._api = api

    def create(self, name: str, conditions: List[Union[str, dict]], device_location_dn: str,
               certificate_location_dn: str = None, rule_type: str = 'X509 Certificate',
               get_if_already_exists: bool = True):
        """
        Creates a placement rule.

        Examples:

            .. code-block:: python

                rule = features.placement_rules.create(
                    name=name,
                    conditions=[
                        features.placement_rule_condition.country.matches('US'),
                        features.placement_rule_condition.common_name.matches_regex('.*my_host\\.com'),
                    ],
                    device_location_dn='\VED\Policy\Certificates',
                    certificate_location_dn='\VED\Policy\Devices'
                )

        Args:
            name: Name of the placement rule.
            conditions: The conditional logic that defines the rule. Requires a specific dictionary with `field`, `comparison`,
                        and `value` keys. Alternatively, use the ``condition`` method to create the condition dictionary.
            device_location_dn: Absolute path to folder that should received all device and application objects that apply to
                                this rule.
            certificate_location_dn: Absolute path to folder that should received all certificate objects that apply to this
                                     rule.
            rule_type: Default is 'X509 Certificate'. 'SSH' may be specified instead for SSH discovery.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object of the placement rule.
        """
        conditions = [json.loads(c) for c in conditions]
        response = self._api.aperture.Discovery.PlacementRules.post(
            name=name,
            conditions=conditions,
            device_location_dn=device_location_dn,
            cert_location_dn=certificate_location_dn
        )
        rule = self._api.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object

    def delete(self, rule: 'Config.Object'):
        """
        Deletes a placement rule.

        Args:
            rule: Config object of the placement rule.
        """
        response = self._api.aperture.Discovery.PlacementRules.Guid(guid=rule.guid).delete()
        response.assert_valid_response()

    def update(self, rule: 'Config.Object', conditions: List[str] = None, device_location_dn: str = None,
               certificate_location_dn: str = None, rule_type: str = 'X509 Certificate'):
        """
        Updates a placement rule. If certain parameters are not provided, the current parameters will be rewritten
        to the object. In other words, only the parameters given are updated.

        Examples:

            .. code-block:: python

                rule = features.placement_rules.get('JobName')
                features.placement_rules.update(
                    rule=rule,
                    conditions=[
                        features.placement_rule_condition.country.matches('US'),
                        features.placement_rule_condition.common_name.matches_regex('.*my_host\\.com'),
                    ],
                    device_location_dn='\VED\Policy\Certificates',
                    certificate_location_dn='\VED\Policy\Devices'
                )

        Args:
            rule: Config object of the placement rule.
            conditions: The conditional logic that defines the rule. This will overwrite the existing rules.
                        Use ``:meth:`pytpp.features.placement_rules.PlacementRuleCondition`` to create a list of rules.
            device_location_dn: Absolute path to folder that should received all device and application objects that apply to
                                this rule.
            certificate_location_dn: Absolute path to folder that should received all certificate objects that apply to this
                                     rule.
            rule_type: Default is 'X509 Certificate'. 'SSH' may be specified instead for SSH discovery.
        """
        conditions = [json.loads(c) for c in conditions]
        rule = self._api.aperture.Discovery.PlacementRules.Guid(guid=rule.guid).get()
        response = self._api.aperture.Discovery.PlacementRules.put(
            guid=rule.guid,
            name=rule.name,
            conditions=conditions or [c.__dict__ for c in rule.conditions],
            device_location_dn=device_location_dn or rule.device_location.dn,
            cert_location_dn=certificate_location_dn or rule.cert_location.dn
        )
        rule = self._api.websdk.Config.IsValid.post(object_guid=response.guid)
        return rule.object
