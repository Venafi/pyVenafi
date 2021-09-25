# noinspection PyUnresolvedReferences
from pytpp.features.definitions.legacy_attribute_names import AttributeNames
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.attribute_values import AttributeValues
# noinspection PyUnresolvedReferences
from pytpp.features.definitions.legacy_classes import Classes
from pytpp.features.definitions.features import (
    Features as _OriginalFeatures, _Discovery as _OriginalDiscovery,
    _Identity as _OriginalIdentity
)
from pytpp.plugins.features.discovery import NetworkDiscovery as _PluginNetworkDiscovery
from pytpp.plugins.features.placement_rules import (
    PlacementRules as _PluginPlacementRules, PlacementRuleCondition as _PluginPlacementRuleCondition
)
from pytpp.plugins.features.identity import (User as _User, Group as _Group)


class _Discovery(_OriginalDiscovery):
    def __init__(self, api):
        self._api = api

        self._network = None

    @property
    def network(self) -> _PluginNetworkDiscovery:
        self._network = self._network or _PluginNetworkDiscovery(api=self._api)
        return self._network


class _Identity(_OriginalIdentity):
    def __init__(self, api):
        self._api = api

        self._group = None
        self._user = None

    @property
    def group(self) -> _Group:
        self._group = self._group or _Group(self._api)
        return self._group

    @property
    def user(self) -> _User:
        self._user = self._user or _User(self._api)
        return self._user


class Features(_OriginalFeatures):
    @property
    def discovery(self) -> _Discovery:
        self._discovery = self._discovery or _Discovery(self._api)
        return self._discovery

    @property
    def identity(self) -> _Identity:
        self._identity = self._identity or _Identity(self._api)
        return self._identity

    @property
    def placement_rule_condition(self) -> _PluginPlacementRuleCondition:
        self._placement_rule_condition = self._placement_rule_condition or _PluginPlacementRuleCondition()
        return self._placement_rule_condition

    @property
    def placement_rules(self) -> _PluginPlacementRules:
        self._placement_rules = self._placement_rules or _PluginPlacementRules(self._api)
        return self._placement_rules
