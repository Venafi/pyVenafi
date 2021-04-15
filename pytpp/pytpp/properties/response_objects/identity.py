class Identity:
    class Identity:
        def __init__(self, response_object: dict):
            self.full_name = response_object.get('FullName')  # type: str
            self.is_container = response_object.get('IsContainer')  # type: bool
            self.is_group = response_object.get('IsGroup')  # type: bool
            self.name = response_object.get('Name')  # type: str
            self.prefix = response_object.get('Prefix')  # type: str
            self.prefixed_name = response_object.get('PrefixedName')  # type: str
            self.prefixed_universal = response_object.get('PrefixedUniversal')  # type: str
            self.type = response_object.get('Type')  # type: str
            self.universal = response_object.get('Universal')  # type: str


    class InvalidIdentity:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.prefix = response_object.get('Prefix')  # type: str
            self.prefixed_name = response_object.get('PrefixedName')  # type: str
            self.prefixed_universal = response_object.get('PrefixedUniversal')  # type: str
            self.universal = response_object.get('Universal')  # type: str
