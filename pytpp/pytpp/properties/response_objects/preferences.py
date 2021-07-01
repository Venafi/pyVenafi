class Preferences:
    class Preference:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.id = response_object.get('Id')  # type: int
            self.universal = response_object.get('Universal')  # type: str
            self.product = response_object.get('Product')  # type: str
            self.category = response_object.get('Category')  # type: str
            self.name = response_object.get('Name')  # type: str
            self.value = response_object.get('Value')  # type: str
            self.locked = response_object.get('Locked')  # type: bool
