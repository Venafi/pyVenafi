class OAuth:
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

    class Permissions:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.delete = response_object.get('delete')  # type: bool
            self.discover = response_object.get('discover')  # type: bool
            self.manage = response_object.get('manage')  # type: bool
            self.read = response_object.get('read')  # type: bool
            self.revoke = response_object.get('revoke')  # type: bool
