from pytpp.properties.response_objects.dataclasses import identity
from pytpp.properties.response_objects.identity import Identity as _Identity


class Identity(_Identity):
    @staticmethod
    def Identity(response_object: dict, api_type: str = 'websdk'):
        if not isinstance(response_object, dict):
            response_object = {}

        if api_type == 'websdk':
            return super().Identity(response_object=response_object)

        elif api_type == 'aperture':
            return identity.Identity(
                full_name=response_object.get('fullName'),
                is_container=response_object.get('isContainer'),
                is_group=response_object.get('isGroup'),
                name=response_object.get('name'),
                prefix='',
                prefixed_name=response_object.get('prefixedName'),
                prefixed_universal=response_object.get('id'),
                type='',
                universal='',
            )

        else:
            return super().Identity({})
