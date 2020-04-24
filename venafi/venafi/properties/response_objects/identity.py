class Identity:
    class Identity:
        def __init__(self, identity_dict: dict, api_type: str):
            if not isinstance(identity_dict, dict):
                identity_dict = {}

            if api_type == 'websdk':
                self.full_name = identity_dict.get('FullName')  # type: str
                self.is_container = identity_dict.get('IsContainer')  # type: bool
                self.is_group = identity_dict.get('IsGroup')  # type: bool
                self.name = identity_dict.get('Name')  # type: str
                self.prefix = identity_dict.get('Prefix')  # type: str
                self.prefixed_name = identity_dict.get('PrefixedName')  # type: str
                self.prefixed_universal = identity_dict.get('PrefixedUniversal')  # type: str
                self.type = identity_dict.get('Type')  # type: str
                self.universal = identity_dict.get('Universal')  # type: str

            elif api_type == 'aperture':
                self.full_name = identity_dict.get('fullName')  # type: str
                self.is_container = identity_dict.get('isContainer')  # type: bool
                self.is_group = identity_dict.get('isGroup')  # type: bool
                self.name = identity_dict.get('name')  # type: str
                self.prefix = ''
                self.prefixed_name = identity_dict.get('prefixedName')  # type: str
                self.prefixed_universal = identity_dict.get('id')  # type: str
                self.type = ''
                self.universal = ''

    class InvalidIdentity:
        def __init__(self, invalid_identity_dict: dict):
            if not isinstance(invalid_identity_dict, dict):
                invalid_identity_dict = {}

            self.prefix = invalid_identity_dict.get('Prefix')  # type: str
            self.prefixed_name = invalid_identity_dict.get('PrefixedName')  # type: str
            self.prefixed_universal = invalid_identity_dict.get('PrefixedUniversal')  # type: str
            self.universal = invalid_identity_dict.get('Universal')  # type: str
