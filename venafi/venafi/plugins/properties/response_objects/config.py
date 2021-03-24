from venafi.properties.response_objects.config import Config as _Config


class Config(_Config):
    class Object(_Config.Object):
        def __init__(self, response_object: dict, api_type: str):
            if not isinstance(response_object, dict):
                response_object = {}

            if api_type.lower() == 'websdk':
                self.absolute_guid = response_object.get('AbsoluteGUID')  # type: str
                self.dn = response_object.get('DN')  # type: str
                self.guid = response_object.get('GUID')  # type: str
                self.config_id = response_object.get('Id')  # type: int
                self.name = response_object.get('Name')  # type: str
                self.parent = response_object.get('Parent')  # type: str
                self.revision = response_object.get('Revision')  # type: int
                self.type_name = response_object.get('TypeName')  # type: str

            elif api_type.lower() == 'aperture':
                self.absolute_guid = response_object.get('parentPolicyGuid')  # type: str
                self.dn = response_object.get('dn')  # type: str
                self.guid = response_object.get('id')  # type: str
                self.config_id = None
                self.name = response_object.get('name')  # type: str
                self.parent = response_object.get('parentDn')  # type: str
                self.revision = None
                self.type_name = response_object.get('typeName')  # type: str

