class Rights:
    class Rights:
        def __init__(self, rights_dict: dict):
            if not isinstance(rights_dict, dict):
                rights_dict = {}

            self.checksum = rights_dict.get('Checksum')  # type: str
            self.is_container = rights_dict.get('IsContainer')  # type: bool
            self.is_group = rights_dict.get('IsGroup')  # type: bool
            self.object = rights_dict.get('Object')  # type: str
            self.principal = rights_dict.get('Principal')  # type: str
            self.rights = rights_dict.get('Rights')  # type: str
            self.sub_system = rights_dict.get('SubSystem')  # type: str
