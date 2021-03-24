from venafi.properties.response_objects.oauth import OAuth as _OAuth

class OAuth(_OAuth):
    class ApplicationScope:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.hidden_subsystems = [OAuth.Subsystem(ss) for ss in response_object.get('hiddenSubsystems', [])]
            self.subsystems = [OAuth.Subsystem(ss) for ss in response_object.get('subsystems', [])]

    class Subsystem:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.name = response_object.get('name')  # type: str
            self.permissions = OAuth.Permissions(response_object.get('permissions'))
