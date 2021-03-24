from venafi.properties.response_objects.identity import Identity as _Identity


class Identity(_Identity):
    class Identity(_Identity.Identity):
        def __init__(self, response_object: dict, api_type: str):
            if not isinstance(response_object, dict):
                response_object = {}

            if api_type == 'websdk':
                self.full_name = response_object.get('FullName')  # type: str
                self.is_container = response_object.get('IsContainer')  # type: bool
                self.is_group = response_object.get('IsGroup')  # type: bool
                self.name = response_object.get('Name')  # type: str
                self.prefix = response_object.get('Prefix')  # type: str
                self.prefixed_name = response_object.get('PrefixedName')  # type: str
                self.prefixed_universal = response_object.get('PrefixedUniversal')  # type: str
                self.type = response_object.get('Type')  # type: str
                self.universal = response_object.get('Universal')  # type: str

            elif api_type == 'aperture':
                self.full_name = response_object.get('fullName')  # type: str
                self.is_container = response_object.get('isContainer')  # type: bool
                self.is_group = response_object.get('isGroup')  # type: bool
                self.name = response_object.get('name')  # type: str
                self.prefix = ''
                self.prefixed_name = response_object.get('prefixedName')  # type: str
                self.prefixed_universal = response_object.get('id')  # type: str
                self.type = ''
                self.universal = ''
