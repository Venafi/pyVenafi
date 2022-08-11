from typing import List
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from pytpp.api.websdk.outputs import identity as ident


class _Teams(WebSdkEndpoint):
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

        class Output(WebSdkOutputModel):
            identity: ident.Identity = ApiField(default_factory=list, alias='ID')
            invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
            invalid_owners: List[ident.InvalidIdentity] = ApiField(alias='InvalidOwners')
            message: str = ApiField(alias='Message')

        return generate_output(output=Output, response=self._post(data=body))

    class _AddTeamMembers(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamMembers')

        def put(self, members: list, team: dict = None, show_members: bool = None):
            body = {
                'Members': members,
                'Team': team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')

            return generate_output(output=Output, response=self._put(data=body))

    class _AddTeamOwners(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/AddTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output=Output, response=self._put(data=body))

    class _DemoteTeamOwners(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/DemoteTeamOwners')

        def put(self, owners: list = None, team: dict = None, show_members: bool = None):
            body = {
                'Owners': owners,
                'Team': team,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output=Output, response=self._put(data=body))

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

        class _Universal(WebSdkEndpoint):
            def __init__(self, prefix: str, universal: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/Teams/{prefix}/{universal}')

            def delete(self):
                class Output(WebSdkOutputModel):
                    message: str = ApiField(alias='Message')

                return generate_output(output=Output, response=self._delete())

            def get(self):
                class Output(WebSdkOutputModel):
                    assets: List[str] = ApiField(default_factory=list, alias='Assets')
                    description: str = ApiField(alias='Description')
                    identity: ident.Identity = ApiField(alias='ID')
                    members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                    message: str = ApiField(alias='Message')
                    owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')
                    products: List[str] = ApiField(default_factory=list, alias='Products')

                return generate_output(output=Output, response=self._get())

            def put(self, assets: list, description: str, name: str, owners: list, members: list, products: list):
                body = {
                    'Assets': assets,
                    'Description': description,
                    'Name': name,
                    'Owners': owners,
                    'Members': members,
                    'Products': products
                }

                class Output(WebSdkOutputModel):
                    identity: ident.Identity = ApiField(alias='ID')
                    invalid_owners: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidOwners')
                    invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                    message: str = ApiField(alias='Message')

                return generate_output(output=Output, response=self._put(data=body))

    class _RemoveTeamMembers(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Teams/RemoveTeamMembers')

        def put(self, team: dict, members: list = None, show_members: bool = None):
            body = {
                'Team': team,
                'Members': members,
                'ShowMembers': show_members
            }

            class Output(WebSdkOutputModel):
                invalid_members: List[ident.InvalidIdentity] = ApiField(default_factory=list, alias='InvalidMembers')
                members: List[ident.Identity] = ApiField(default_factory=list, alias='Members')
                message: str = ApiField(alias='Message')
                owners: List[ident.Identity] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output=Output, response=self._put(data=body))

    class _RenameTeam(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Teams/RenameTeam')

        def put(self, team: str, new_team_name: str):
            body = {
                'Team'       : team,
                'NewTeamName': new_team_name
            }

            class Output(WebSdkOutputModel):
                identity: ident.Identity = ApiField(alias='ID')
                message: str = ApiField(alias='Message')

            return generate_output(output=Output, response=self._put(data=body))
