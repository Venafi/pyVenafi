import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
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
            identities = []
            for identity in self.response.json().get('Identities', []):
                identities.append(Identity(identity))

            self.logger.log('Identities: %s' % ', '.join([x.PrefixedName for x in identities]))
            return identities

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
            identities = []
            for identity in self.response.json().get('Identities', []):
                identities.append(Identity(identity))

            return identities

        def post(self, identity):
            """
            :param identity: http://doc.venqa.venafi.com/Content/SDK/WebSDK/API_Reference/r-SDK-IdentityInformation.htm
            :type identity: Identity or dict
            """
            if isinstance(identity, Identity):
                data = json.dumps({
                    "PrefixedUniversal": identity.PrefixedUniversal
                })
            elif isinstance(identity, dict):
                data = json.dumps(identity)
            else:
                raise TypeError('Parameter "identity" must be of type "Identity" or dict. See docstring.')

            self.response = self._session.post(url=self._url, data=data)

            return self

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
            identities = []
            for identity in self.response.json().get('Identities', []):
                identities.append(Identity(identity))

            return identities

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
        def members(self):
            identities = []
            for identity in self.response.json().get('Identities', []):
                identities.append(Identity(identity))

            self.logger.log('Identities: %s' % ', '.join([x.PrefixedName for x in identities]))
            return identities

        def post(self, identity, resolve_nested=False):
            """
            :type identity: Identity
            :type resolve_nested: bool
            """
            body = json.dumps({
                'ID': {
                    'Name': identity.Name,
                    'PrefixedUniversal': identity.PrefixedUniversal
                },
                'ResolveNested': 1 if resolve_nested else 0
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

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
        def memberships(self):
            identities = []
            for identity in self.response.json().get('Identities', []):
                identities.append(Identity(identity))

            self.logger.log('Identities: %s' % ', '.join([x.PrefixedName for x in identities]))
            return identities

        def post(self, identity):
            """
            :type identity: Identity
            :type resolve_nested: bool
            """
            body = json.dumps({
                'ID': {
                    'Name': identity.Name,
                    'PrefixedUniversal': identity.PrefixedUniversal
                }
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

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
            attribute = None
            return attribute

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
            password = None
            return password

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
            validation = None
            return validation

        def post(self):
            return self
