class OAuth:
    class ApplicationScope:
        def __init__(self, application_scope_dict: dict):
            if not isinstance(application_scope_dict, dict):
                application_scope_dict = {}

            self.hidden_subsystems = [OAuth.Subsystem(ss) for ss in application_scope_dict.get('hiddenSubsystems', [])]
            self.subsystems = [OAuth.Subsystem(ss) for ss in application_scope_dict.get('subsystems', [])]

    class Subsystem:
        def __init__(self, subsystem_dict: dict):
            if not isinstance(subsystem_dict, dict):
                subsystem_dict = {}

            self.name = subsystem_dict.get('name')  # type: str
            self.permissions = OAuth.Permissions(subsystem_dict.get('permissions'))

    class Permissions:
        def __init__(self, permissions_dict: dict):
            if not isinstance(permissions_dict, dict):
                permissions_dict = {}

            self.delete = permissions_dict.get('delete')  # type: bool
            self.discover = permissions_dict.get('discover')  # type: bool
            self.manage = permissions_dict.get('manage')  # type: bool
            self.read = permissions_dict.get('read')  # type: bool
            self.revoke = permissions_dict.get('revoke')  # type: bool
