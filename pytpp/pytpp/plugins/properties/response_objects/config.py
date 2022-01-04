from pytpp.properties.response_objects.config import Config as _Config
from pytpp.properties.response_objects.dataclasses import config


class Config(_Config):
    @staticmethod
    def Object(response_object: dict, api_type: str = 'websdk'):
        if not isinstance(response_object, dict):
            response_object = {}

        if api_type.lower() == 'websdk':
            return super().Object(response_object=response_object)

        elif api_type.lower() == 'aperture':
            return config.Object(
                absolute_guid=response_object.get('parentPolicyGuid'),
                dn=response_object.get('dn'),
                guid=response_object.get('id'),
                config_id=None,
                name=response_object.get('name'),
                parent=response_object.get('parentDn'),
                revision=None,
                type_name=response_object.get('typeName')
            )

        else:
            return super().Object({})
