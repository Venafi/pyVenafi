import json
from api.api_base import API, response_property
from api.session import WEBSDK_URL
from objects.response_objects.identity import Identity


class _Identity:
    def __init__(self, session, api_type):
        self.Browse = self._Browse(session, api_type)
        self.GetAssociatedEntries = self._GetAssociatedEntries(session, api_type)
        self.GetMembers = self._GetMembers(session, api_type)
        self.GetMemberships = self._GetMemberships(session, api_type)
        self.ReadAttribute = self._ReadAttribute(session, api_type)
        self.Self = self._Self(session, api_type)
        self.SetPassword = self._SetPassword(session, api_type)
        self.Validate = self._Validate(session, api_type)

    class _Browse(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/Browse',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, filter, limit, identity_type):
            data = json.dumps({
                "Filter": filter,
                "Limit": limit,
                "IdentityType": identity_type
            })

            self.response = self._session.post(url=self._url, data=data)
            return self

    class _GetAssociatedEntries(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/GetAssociatedEntries',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity):
            pass # TODO

    class _Self(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/Self',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def get(self):
            self.response = self._session.get(url=self._url)
            return self

    class _GetMembers(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/GetMembers',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Members')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity, resolve_nested=False):
            pass #TODO

    class _GetMemberships(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/GetMemberships',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def identities(self):
            result = self.json_response(key='Identities')
            return [Identity.Identity(i, self._api_type) for i in result]

        def post(self, identity):
            pass # TODO

    class _ReadAttribute(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/ReadAttribute',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def attribute(self):
            return self.json_response(key='Attribute')

        def post(self):
            return self

    class _SetPassword(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/SetPassword',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def password(self):
            return self.json_response(key='Password')

        def post(self):
            return self

    class _Validate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Identity/Validate',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def validation(self):
            return self.json_response(key='Validation')

        def post(self):
            return self
