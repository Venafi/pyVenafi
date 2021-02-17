class PlacementRules:
    class Condition:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}
                
            self.field = response_object.get('field')  # type: str
            self.comparison = response_object.get('comparison')  # type: str
            self.value = response_object.get('value')  # type: str
