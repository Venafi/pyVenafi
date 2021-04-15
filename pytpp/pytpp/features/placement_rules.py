from typing import List
import re
from pytpp.vtypes import Config
from pytpp.properties.config import PlacementRulesAttributeNames, PlacementRulesAttributeValues, \
    PlacementRulesClassNames
from pytpp.features.bases.feature_base import FeatureBase, feature


@feature()
class PlacementRuleCondition:
    def __init__(self):
        pass

    @property
    def city(self):
        return self._Operators(field='Certificate.City')

    @property
    def common_name(self):
        return self._Operators(field='Certificate.CN')

    @property
    def country(self):
        return self._Operators(field='Certificate.C')

    @property
    def domain_component(self):
        return self._Operators(field='Certificate.DC')

    @property
    def expired(self):
        return self._Operators(field='Certificate.Expired')

    @property
    def hostname(self):
        return self._Operators(field='Discovery.Hostname')

    @property
    def ip_address(self):
        return self._Operators(field='Discovery.Address')

    @property
    def issuer_dn(self):
        return self._Operators(field='Certificate.Issuer')

    @property
    def operating_system(self):
        return self._Operators(field='Discovery.OS')

    @property
    def organization(self):
        return self._Operators(field='Certificate.O')

    @property
    def organizational_unit(self):
        return self._Operators(field='Certificate.OU')

    @property
    def port(self):
        return self._Operators(field='Discovery.Port')

    @property
    def san(self):
        return self._Operators(field='Certificate.SANDNS')

    @property
    def self_signed(self):
        return self._Operators(field='Certificate.SelfSigned')

    @property
    def server_version(self):
        return self._Operators(field='SSH.ServerVersion')

    @property
    def state(self):
        return self._Operators(field='Certificate.State')

    @property
    def supports_ssh_v1(self):
        return self._Operators(field='SSH.Version', force_value='1')

    @property
    def supports_ssh_v2(self):
        return self._Operators(field='SSH.Version', force_value='2')

    class _Operators:
        def __init__(self, field: str, force_value: str = None):
            self._field = field
            self._forced_value = force_value

        def matches(self, value: str):
            """
            Args:
                value: String to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} == "{value}"'

        def in_list(self, values: List[str]):
            """
            Args:
                values: List of strings to match.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f"{self._field} in [{','.join(map(str, values))}]"

        def starts_with(self, value: str):
            """
            Args:
                value: String that the target field's value begins with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} > "{value}"'

        def ends_with(self, value: str):
            """
            Args:
                value: String that the target field's value ends with.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} < "{value}"'

        def contains(self, value: str):
            """
            Args:
                value: String within the target field's value.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} like "{value}"'

        def matches_regex(self, value: str):
            """
            Args:
                value: String to match by regular expression.

            Returns: Condition string for the Placement Rule to be created.
            """
            return f'{self._field} @= "{value}"'

        def is_true(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            if self._forced_value:
                return f"{self._field} == {self._forced_value}"
            return f"{self._field} == 1"

        def is_false(self):
            """
            Returns: Condition string for the Placement Rule to be created.
            """
            if self._forced_value:
                return f"{self._field} != {self._forced_value}"
            return f"{self._field} == 0"


@feature()
class PlacementRules(FeatureBase):
    """
    This feature provides high-level interaction with TPP Placement Rule objects.
    """
    def __init__(self, api):
        super().__init__(api=api)
        self._layout_rules_dn = r'\VED\Layout Root\Rules'

    @staticmethod
    def _format_rule_attribute(conditions: List[str], device_location_dn: str,
                               certificate_location_dn: str = None, rule_type: str = 'X509 Certificate'):
        """
        Formats the rule attribute on the Placement Rule object.
        """
        context = 'CONTEXT\n\tDiscovery'
        rule_types = f"FOR\n\t{','.join(('Device', rule_type))}"
        conditions = f"IF\n\t{' && '.join(conditions)}"
        locations = [f'Location[Device]={device_location_dn}']
        if certificate_location_dn:
            locations.append(f'Location[X509 Certificate Base]={certificate_location_dn}')
        locations = f"THEN\n\t" + '\n\t'.join(locations)

        return f"{context}\n{rule_types}\n{conditions}\n{locations}\nEND"

    def create(self, name: str, conditions: List[str], device_location_dn: str,
               certificate_location_dn: str = None, rule_type: str = 'X509 Certificate'):
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

        Returns:
            Config object of the placement rule.
        """
        rule_attr = self._format_rule_attribute(
            conditions=conditions,
            device_location_dn=device_location_dn,
            certificate_location_dn=certificate_location_dn,
            rule_type=rule_type
        )
        rule = self._config_create(
            name=name,
            parent_folder_dn=self._layout_rules_dn,
            attributes={
                PlacementRulesAttributeNames.rule: rule_attr
            },
            config_class=PlacementRulesClassNames.layout_rule_base
        )
        return rule

    def delete(self, rule: 'Config.Object'):
        """
        Deletes a placement rule.

        Args:
            rule: Config object of the placement rule.
        """
        response = self._config_delete(object_dn=rule.dn)
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
        current_attr = self._api.websdk.Config.Read.post(
            object_dn=rule.dn,
            attribute_name=PlacementRulesAttributeNames.rule
        ).values[0]
        new_conditions = conditions or []
        new_certificate_dn = certificate_location_dn or ''
        new_device_dn = device_location_dn or ''
        get_conditions = get_locations = False
        for line in current_attr.splitlines():
            if line.strip() == 'IF':
                if not conditions:
                    get_conditions = True
                get_locations = False
            elif line.strip() == 'THEN':
                get_conditions = False
                if not(new_certificate_dn and new_device_dn):
                    get_locations = True
            elif line.strip() == 'END':
                break
            elif get_conditions:
                new_conditions = line.strip().split(' && ')
                get_conditions = False
            elif get_locations:
                if 'Location[Device]' in line and not new_device_dn:
                    new_device_dn = line.split('=', 1)[-1].strip()
                elif 'Location[X509 Certificate Base]' in line and not new_certificate_dn:
                    new_certificate_dn = line.split('=', 1)[-1].strip()

        if rule_type == PlacementRulesAttributeValues.RuleType.ssh:
            new_certificate_dn = None

        rule_attr = self._format_rule_attribute(
            conditions=new_conditions,
            device_location_dn=new_device_dn,
            certificate_location_dn=new_certificate_dn,
            rule_type=rule_type
        )
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=rule.dn,
            attribute_name=PlacementRulesAttributeNames.rule,
            values=[
                rule_attr
            ]
        )
        response.assert_valid_response()

    def get(self, name: str):
        """
        Args:
            name: Name of the placement rule.

        Returns:
            Config object of the placement rule.
        """
        rule = self._api.websdk.Config.IsValid.post(
            object_dn=f'{self._layout_rules_dn}\\{name}'
        )
        return rule.object
