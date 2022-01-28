from pytpp.plugins.properties.response_objects.dataclasses import placement_rules


class PlacementRules:
    @staticmethod
    def Condition(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return placement_rules.PlacementRules(
            field=response_object.get('field'),
            comparison=response_object.get('comparison'),
            value=response_object.get('value'),
        )
