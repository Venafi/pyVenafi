from typing import List
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField
from pytpp.properties.response_objects.dataclasses import identity as ident


class _Teams(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Teams')
        self.AddTeamMembers = self._AddTeamMembers(api_obj=api_obj)
        self.AddTeamOwners = self._AddTeamOwners(api_obj=api_obj)
        self.DemoteTeamOwners = self._DemoteTeamOwners(api_obj=api_obj)
        self.RemoveTeamMembers = self._RemoveTeamMembers(api_obj=api_obj)
        self.RenameTeam = self._RenameTeam(api_obj=api_obj)

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

        class Response(APIResponse):
            identity: List[ident.Identity] = ResponseField(default_factory=list, alias='Owners') 
            invalid_members: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidMembers') 

        return ResponseFactory(response_cls=Response, response=self._post(data=body))

    class _AddTeamMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamMembers')

        def put(self, members: list, team: dict = None, show_members: bool = None):
            body = {
                'Members': members,
                'Team': team,
                'ShowMembers': show_members
            }

            class Response(APIResponse):
                invalid_members: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidMembers') 
                members: List[ident.Identity] = ResponseField(default_factory=list, alias='Members') 
                message: str = ResponseField(alias='Message')

            return ResponseFactory(response_cls=Response, response=self._put(data=body))

    class _AddTeamOwners(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class Response(APIResponse):
                owners: List[ident.Identity] = ResponseField(default_factory=list, alias='Owners') 
                members: List[ident.Identity] = ResponseField(default_factory=list, alias='Members') 
                message: str = ResponseField(alias='Message')

            return ResponseFactory(response_cls=Response, response=self._put(data=body))

    class _DemoteTeamOwners(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/DemoteTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class Response(APIResponse):
                invalid_owners: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidOwners') 
                owners: List[ident.Identity] = ResponseField(default_factory=list, alias='Owners') 
                members: List[ident.Identity] = ResponseField(default_factory=list, alias='Members') 
                message: str = ResponseField(alias='Message')

            return ResponseFactory(response_cls=Response, response=self._put(data=body))

    def Prefix(self, prefix='local'):
        return self._Prefix(prefix=prefix, api_obj=self._api_obj)

    class _Prefix:
        def __init__(self, prefix: str, api_obj):
            self._prefix = prefix
            self._api_obj = api_obj

        def Universal(self, universal):
            return self._Universal(
                prefix=self._prefix,
                universal=universal,
                api_obj=self._api_obj
            )

        class _Universal(API):
            def __init__(self, prefix: str, universal: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/Teams/{prefix}/{universal}')

            def delete(self):
                class Response(APIResponse):
                    message: str = ResponseField(alias='Message')

                return ResponseFactory(response_cls=Response, response=self._delete())

            def get(self):
                class Response(APIResponse):
                    assets: List[str] = ResponseField(default_factory=list, alias='Assets')
                    description: str = ResponseField(alias='Description')
                    identity: ident.Identity = ResponseField(alias='ID')
                    members: List[ident.Identity] = ResponseField(default_factory=list, alias='Members') 
                    owners: List[ident.Identity] = ResponseField(default_factory=list, alias='Owners') 
                    products: List[str] = ResponseField(default_factory=list, alias='Products')

                return ResponseFactory(response_cls=Response, response=self._get())

            def put(self, assets: list, description: str, name: str, owners: list, members: list, products: list):
                body = {
                    'Assets': assets,
                    'Description': description,
                    'Name': name,
                    'Owners': owners,
                    'Members': members,
                    'Products': products
                }

                class Response(APIResponse):
                    identity: ident.Identity = ResponseField(alias='ID')
                    invalid_owners: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidOwners') 
                    invalid_members: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidMembers') 
                    message: str = ResponseField(alias='Message')

                return ResponseFactory(response_cls=Response, response=self._put(data=body))

    class _RemoveTeamMembers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/RemoveTeamMembers')

        def put(self, team: dict, members: list = None, show_members: bool = None):
            body = {
                'Team': team,
                'Members': members,
                'ShowMembers': show_members
            }

            class Response(APIResponse):
                invalid_members: List[ident.InvalidIdentity] = ResponseField(default_factory=list, alias='InvalidMembers') 
                members: List[ident.Identity] = ResponseField(default_factory=list, alias='Members') 
                message: str = ResponseField(alias='Message')
                owners: List[ident.Identity] = ResponseField(default_factory=list, alias='Owners') 

            return ResponseFactory(response_cls=Response, response=self._put(data=body))

    class _RenameTeam(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Teams/RenameTeam')

        def put(self, team: str, new_team_name: str):
            body = {
                'Team'       : team,
                'NewTeamName': new_team_name
            }

            class Response(APIResponse):
                identity: ident.Identity = ResponseField(alias='ID')
                message: str = ResponseField(alias='Message')

            return ResponseFactory(response_cls=Response, response=self._put(data=body))
