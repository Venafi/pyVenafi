class OAuth:
    class Permissions:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.delete = response_object.get('delete')  # type: bool
            self.discover = response_object.get('discover')  # type: bool
            self.manage = response_object.get('manage')  # type: bool
            self.read = response_object.get('read')  # type: bool
            self.revoke = response_object.get('revoke')  # type: bool
