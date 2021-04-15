class Rights:
    class Rights:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.checksum = response_object.get('Checksum')  # type: str
            self.is_container = response_object.get('IsContainer')  # type: bool
            self.is_group = response_object.get('IsGroup')  # type: bool
            self.object = response_object.get('Object')  # type: str
            self.principal = response_object.get('Principal')  # type: str
            self.rights = response_object.get('Rights')  # type: str
            self.sub_system = response_object.get('SubSystem')  # type: str
