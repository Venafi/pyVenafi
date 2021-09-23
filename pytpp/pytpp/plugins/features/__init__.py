# noinspection PyUnresolvedReferences
from pytpp.features import Features as _OriginalFeatures, AttributeNames, AttributeValues, Classes, \
    _Discovery as _OriginalDiscovery
from pytpp.plugins.features.discovery import NetworkDiscovery as _PluginNetworkDiscovery
from pytpp.plugins.features.placement_rules import PlacementRules as _PluginPlacementRules, \
    PlacementRuleCondition as _PluginPlacementRuleCondition


class _Discovery(_OriginalDiscovery):
    def __init__(self, api):
        self._api = api

        self._network = None

    @property
    def network(self) -> _PluginNetworkDiscovery:
        self._network = self._network or _PluginNetworkDiscovery(api=self._api)
        return self._network


class Features(_OriginalFeatures):
    @property
    def discovery(self) -> _Discovery:
        self._discovery = self._discovery or _Discovery(self._api)
        return self._discovery

    @property
    def placement_rule_condition(self) -> _PluginPlacementRuleCondition:
        self._placement_rule_condition = self._placement_rule_condition or _PluginPlacementRuleCondition()
        return self._placement_rule_condition

    @property
    def placement_rules(self) -> _PluginPlacementRules:
        self._placement_rules = self._placement_rules or _PluginPlacementRules(self._api)
        return self._placement_rules
