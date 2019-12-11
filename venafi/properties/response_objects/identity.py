class Identity:
    class Identity:
        def __init__(self, identity_dict: dict):
            if not isinstance(identity_dict, dict):
                identity_dict = {}

            self.full_name = identity_dict.get('FullName')
            self.is_container = identity_dict.get('IsContainer')
            self.is_group = identity_dict.get('IsGroup')
            self.name = identity_dict.get('Name')
            self.prefix = identity_dict.get('Prefix')
            self.prefixed_name = identity_dict.get('PrefixedName')
            self.prefixed_universal = identity_dict.get('PrefixedUniversal')
            self.type = identity_dict.get('Type')
            self.universal = identity_dict.get('Universal')

    class InvalidMembers:
        def __init__(self, invalid_members_dict: dict):
            if not isinstance(invalid_members_dict, dict):
                invalid_members_dict = {}

            self.prefix = invalid_members_dict.get('Prefix')
            self.prefixed_name = invalid_members_dict.get('PrefixedName')
            self.prefixed_universal = invalid_members_dict.get('PrefixedUniversal')
            self.universal = invalid_members_dict.get('Universal')
