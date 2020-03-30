from typing import List
from venafi.api.api_base import API, json_response_property
from venafi.properties.response_objects.identity import Identity


class _Teams(API):
    def __init__(self, websdk_obj):
        super().__init__(api_obj=websdk_obj, url='/Teams', valid_return_codes=[200])
        self.AddTeamMembers = self._AddTeamMembers(websdk_obj=websdk_obj)
        self.AddTeamOwners = self._AddTeamOwners(websdk_obj=websdk_obj)
        self.DemoteTeamOwners = self._DemoteTeamOwners(websdk_obj=websdk_obj)
        self.RemoveTeamMembers = self._RemoveTeamMembers(websdk_obj=websdk_obj)

    @property
    @json_response_property()
    def identity(self):
        return [Identity.Identity(owner, self._api_type) for owner in self._from_json(key='Owners')]

    @property
    @json_response_property()
    def invalid_members(self):
        return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

    def post(self, name: str, owners: list, assets: list = None, description: str = None, members: list = None,
             products: list = None):
        body = {
            'Assets': assets,
            'Description': description,
            'Name': name,
            'Owners': owners,
            'Members': members,
            'Products': products
        }

        self.json_response = self._post(data=body)
        return self

    class _AddTeamMembers(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Teams/AddTeamMembers', valid_return_codes=[200])

        @property
        @json_response_property()
        def invalid_members(self):
            return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

        @property
        @json_response_property()
        def members(self):
            return [Identity.Identity(member, api_type=self._api_type) for member in self._from_json(key='Members')]

        @property
        @json_response_property()
        def message(self) -> str:
            return self._from_json(key='Message')

        def put(self, members: list, team: dict = None, show_members: bool = None):
            body = {
                'Members': members,
                'Team': team,
                'ShowMembers': show_members
            }

            self.json_response = self._put(data=body)
            return self

    class _AddTeamOwners(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Teams/AddTeamOwners', valid_return_codes=[200])

        @property
        @json_response_property()
        def owners(self):
            return [Identity.Identity(owner, api_type=self._api_type) for owner in self._from_json(key='Owners')]

        @property
        @json_response_property()
        def members(self):
            return [Identity.Identity(member, api_type=self._api_type) for member in self._from_json(key='Members')]

        @property
        @json_response_property()
        def message(self) -> str:
            return self._from_json(key='Message')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            self.json_response = self._put(data=body)
            return self

    class _DemoteTeamOwners(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Teams/DemoteTeamOwners', valid_return_codes=[200])

        @property
        @json_response_property()
        def invalid_owners(self):
            return [Identity.InvalidIdentity(owner) for owner in self._from_json(key='InvalidOwners')]

        @property
        @json_response_property()
        def owners(self):
            return [Identity.Identity(owner, api_type=self._api_type) for owner in self._from_json(key='Owners')]

        @property
        @json_response_property()
        def members(self):
            return [Identity.Identity(member, api_type=self._api_type) for member in self._from_json(key='Members')]

        @property
        @json_response_property()
        def message(self) -> str:
            return self._from_json(key='Message')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            self.json_response = self._put(data=body)
            return self

    def Prefix(self, prefix='local'):
        return self._Prefix(prefix=prefix, websdk_obj=self._api_obj)

    class _Prefix:
        def __init__(self, prefix: str, websdk_obj):
            self._prefix = prefix
            self._websdk_obj = websdk_obj

        def Universal(self, universal):
            return self._Universal(
                prefix=self._prefix,
                universal=universal,
                websdk_obj=self._websdk_obj
            )

        class _Universal(API):
            def __init__(self, prefix: str, universal: str, websdk_obj):
                super().__init__(api_obj=websdk_obj, url=f'/Teams/{prefix}/{universal}', valid_return_codes=[200])

            @property
            @json_response_property()
            def assets(self) -> List[str]:
                return self._from_json(key='Assets')

            @property
            @json_response_property()
            def description(self) -> str:
                return self._from_json(key='Description')

            @property
            @json_response_property()
            def identity(self):
                return Identity.Identity(self._from_json(key='ID'), self._api_type)

            @property
            @json_response_property()
            def invalid_owners(self):
                return [Identity.InvalidIdentity(owner) for owner in self._from_json(key='InvalidOwners')]

            @property
            @json_response_property()
            def invalid_members(self):
                return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

            @property
            @json_response_property()
            def owners(self):
                return [Identity.Identity(owner, api_type=self._api_type) for owner in self._from_json(key='Owners')]

            @property
            @json_response_property()
            def members(self):
                return [Identity.Identity(member, api_type=self._api_type) for member in self._from_json(key='Members')]

            @property
            @json_response_property()
            def products(self) -> List[str]:
                return self._from_json(key='Products')

            def delete(self):
                self.json_response = self._delete()
                return self

            def get(self):
                self.json_response = self._get()
                return self

            def put(self, assets: list, description: str, name: str, owners: list, members: list, products: list):
                body = {
                    'Assets': assets,
                    'Description': description,
                    'Name': name,
                    'Owners': owners,
                    'Members': members,
                    'Products': products
                }

                self.json_response = self._put(data=body)
                return self

    class _RemoveTeamMembers(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Teams/RemoveTeamMembers', valid_return_codes=[200])

        @property
        @json_response_property()
        def invalid_members(self):
            return [Identity.InvalidIdentity(member) for member in self._from_json(key='InvalidMembers')]

        @property
        @json_response_property()
        def members(self):
            return [Identity.Identity(member, api_type=self._api_type) for member in self._from_json(key='Members')]

        @property
        @json_response_property()
        def message(self) -> str:
            return self._from_json(key='Message')

        @property
        @json_response_property()
        def owners(self):
            return [Identity.Identity(owner, api_type=self._api_type) for owner in self._from_json(key='Owners')]

        def put(self, team: dict, members: list = None, show_members: bool = None):
            body = {
                'Team': team,
                'Members': members,
                'ShowMembers': show_members
            }

            self.json_response = self._put(data=body)
            return self
