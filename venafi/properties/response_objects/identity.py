class Identity:
    class Identity:
        def __init__(self, identity_dict: dict):
            if not isinstance(identity_dict, dict):
                identity_dict = {}

            self.full_name = identity_dict.get('FullName')  # type: str
            self.is_container = identity_dict.get('IsContainer')  # type: str
            self.is_group = identity_dict.get('IsGroup')  # type: bool
            self.name = identity_dict.get('Name')  # type: str
            self.prefix = identity_dict.get('Prefix')  # type: str
            self.prefixed_name = identity_dict.get('PrefixedName')  # type: str
            self.prefixed_universal = identity_dict.get('PrefixedUniversal')  # type: str
            self.type = identity_dict.get('Type')  # type: str
            self.universal = identity_dict.get('Universal')  # type: str

    class InvalidMembers:
        def __init__(self, invalid_members_dict: dict):
            if not isinstance(invalid_members_dict, dict):
                invalid_members_dict = {}

            self.prefix = invalid_members_dict.get('Prefix')  # type: str
            self.prefixed_name = invalid_members_dict.get('PrefixedName')  # type: str
            self.prefixed_universal = invalid_members_dict.get('PrefixedUniversal')  # type: str
            self.universal = invalid_members_dict.get('Universal')  # type: str
