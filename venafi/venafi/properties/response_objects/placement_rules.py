class PlacementRules:
    class Condition:
        def __init__(self, condition_dict: dict):
            if not isinstance(condition_dict, dict):
                condition_dict = {}
                
            self.field = condition_dict.get('field')  # type: str
            self.comparison = condition_dict.get('comparison')  # type: str
            self.value = condition_dict.get('value')  # type: str
