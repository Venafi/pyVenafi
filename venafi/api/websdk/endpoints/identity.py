from api.api_base import API, response_property
from properties.response_objects.identity import Identity


class _Identity:
    def __init__(self, websdk_obj):
        self.Browse = self._Browse(websdk_obj=websdk_obj)
        self.GetAssociatedEntries = self._GetAssociatedEntries(websdk_obj=websdk_obj)
        self.GetMembers = self._GetMembers(websdk_obj=websdk_obj)
        self.GetMemberships = self._GetMemberships(websdk_obj=websdk_obj)
        self.ReadAttribute = self._ReadAttribute(websdk_obj=websdk_obj)
        self.Self = self._Self(websdk_obj=websdk_obj)
        self.SetPassword = self._SetPassword(websdk_obj=websdk_obj)
        self.Validate = self._Validate(websdk_obj=websdk_obj)

    class _Browse(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/Browse', valid_return_codes=[200])

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, filter, limit, identity_type):
            data = {
                "Filter": filter,
                "Limit": limit,
                "IdentityType": identity_type
            }

            self.response = self._post(data=data)
            return self

    class _GetAssociatedEntries(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/GetAssociatedEntries', valid_return_codes=[200])

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity):
            pass # TODO

    class _Self(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/Self', valid_return_codes=[200])

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def get(self):
            self.response = self._get()
            return self

    class _GetMembers(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/GetMembers', valid_return_codes=[200])

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Members')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity, resolve_nested=False):
            pass #TODO

    class _GetMemberships(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/GetMemberships', valid_return_codes=[200])

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity):
            pass # TODO

    class _ReadAttribute(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/ReadAttribute', valid_return_codes=[200])

        @property
        @response_property()
        def attribute(self):
            return self.json_response(key='Attribute')

        def post(self):
            return self

    class _SetPassword(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/SetPassword', valid_return_codes=[200])

        @property
        @response_property()
        def password(self):
            return self.json_response(key='Password')

        def post(self):
            return self

    class _Validate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Identity/Validate', valid_return_codes=[200])

        @property
        @response_property()
        def validation(self):
            return self.json_response(key='Validation')

        def post(self):
            return self
