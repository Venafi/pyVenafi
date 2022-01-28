from pytpp.properties.response_objects.oauth import OAuth as _OAuth
from pytpp.plugins.properties.response_objects.dataclasses import oauth


class OAuth(_OAuth):
    @staticmethod
    def ApplicationScope(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return oauth.ApplicationScope(
            hidden_subsystems=[OAuth.Subsystem(ss) for ss in response_object.get('hiddenSubsystems', [])],
            subsystems=[OAuth.Subsystem(ss) for ss in response_object.get('subsystems', [])],
        )

    @staticmethod
    def Subsystem(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return oauth.Subsystem(
            name=response_object.get('name'),
            permissions=OAuth.Permissions(response_object.get('permissions')),
        )
