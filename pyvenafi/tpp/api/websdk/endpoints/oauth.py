from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import oauth

class OauthOutputBase(WebSdkOutputModel):
    success: bool = ApiField(alias='Success')
    result: bool = ApiField(alias='Result')
    error_description: str = ApiField(alias='error_description')

class _Oauth(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/oauth')

        self.GrantRole = self._GrantRole(api_obj=api_obj, url=f'{self._url}/grantrole')
        self.RevokeRole = self._RevokeRole(api_obj=api_obj, url=f'{self._url}/revokerole')
        self.ListRoles = self._ListRoles(api_obj=api_obj, url=f'{self._url}/listroles')
        self.GetRole = self._GetRole(api_obj=api_obj, url=f'{self._url}/getrole')
        self.GetConfiguration = self._GetConfiguration(api_obj=api_obj, url=f'{self._url}/getconfiguration')
        self.SetConfiguration = self._SetConfiguration(api_obj=api_obj, url=f'{self._url}/setconfiguration')
        self.CreateApplication = self._CreateApplication(api_obj=api_obj, url=f'{self._url}/createapplication')
        self.EnumerateApplications = self._Enumerateapplications(
            api_obj=api_obj,
            url=f'{self._url}/enumerateapplications'
        )
        self.GetApplications = self._GetApplications(api_obj=api_obj, url=f'{self._url}/getapplications')
        self.GetApplication = self._GetApplication(api_obj=api_obj, url=f'{self._url}/getapplication')
        self.UpdateApplication = self._UpdateApplication(api_obj=api_obj, url=f'{self._url}/updateapplication')
        self.DeleteApplication = self._DeleteApplication(api_obj=api_obj, url=f'{self._url}/deleteapplication')
        self.GetScopes = self._GetScopes(api_obj=api_obj, url=f'{self._url}/getscopes')
        self.GetGrants = self._GetGrants(api_obj=api_obj, url=f'{self._url}/getgrants')
        self.EnumerateGrants = self._EnumerateGrants(api_obj=api_obj, url=f'{self._url}/enumerategrants')
        self.RevokeGrants = self._RevokeGrants(api_obj=api_obj, url=f'{self._url}/revokegrants')
        self.CreateRule = self._CreateRule(api_obj=api_obj, url=f'{self._url}/createrule')
        self.GetRules = self._GetRules(api_obj=api_obj, url=f'{self._url}/getrules')
        self.EnumerateRules = self._EnumerateRules(api_obj=api_obj, url=f'{self._url}/enumeraterules')
        self.UpdateRule = self._UpdateRule(api_obj=api_obj, url=f'{self._url}/updaterule')
        self.DeleteRule = self._DeleteRule(api_obj=api_obj, url=f'{self._url}/deleterule')
        self.DeleteRules = self._DeleteRules(api_obj=api_obj, url=f'{self._url}/deleterules')
        self.GrantCount = self._GrantCount(api_obj=api_obj, url=f'{self._url}/grantcount')
        self.UserCount = self._UserCount(api_obj=api_obj, url=f'{self._url}/usercount')
        self.CreateJwtMapping = self._CreateJwtMapping(api_obj=api_obj, url=f'{self._url}/createjwtmapping')
        self.EnumerateJwtMappings = self._EnumerateJwtMappings(api_obj=api_obj, url=f'{self._url}/enumeratejwtmappings')
        self.GetJwtMappings = self._GetJwtMappings(api_obj=api_obj, url=f'{self._url}/getjwtmappings')
        self.GetJwtMapping = self._GetJwtMapping(api_obj=api_obj, url=f'{self._url}/getjwtmapping')
        self.UpdateJwtMapping = self._UpdateJwtMapping(api_obj=api_obj, url=f'{self._url}/updatejwtmapping')
        self.DeleteJwtMapping = self._DeleteJwtMapping(api_obj=api_obj, url=f'{self._url}/deletejwtmapping')

    class _GrantRole(WebSdkEndpoint):
        def post(self, grantee_prefixed_universal: str = None, role: int = None, application_id: str = None):
            body = {
                'GranteePrefixedUniversal': grantee_prefixed_universal,
                'Role'                    : role,
                'ApplicationId'           : application_id,
            }

            class Output(OauthOutputBase):
                success: bool = ApiField(alias='Success')
                result: bool = ApiField(alias='Result')
                error: bool = ApiField(alias='Error')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RevokeRole(WebSdkEndpoint):
        def post(self, grantee_prefixed_universal: str = None, role: int = None):
            body = {
                "GranteePrefixedUniversal": grantee_prefixed_universal,
                "Role"                    : role
            }

            class Output(OauthOutputBase):
                success: bool = ApiField(alias='Success')
                result: bool = ApiField(alias='Result')
                error: bool = ApiField(alias='Error')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ListRoles(WebSdkEndpoint):
        def post(self, grantee_prefixed_universal: str = None):
            body = {
                "GranteePrefixedUniversal": grantee_prefixed_universal
            }

            class Output(OauthOutputBase):
                roles: list[oauth.Role] = ApiField(alias='Roles')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetRole(WebSdkEndpoint):
        def post(self):
            class Output(OauthOutputBase):
                role: oauth.Role = ApiField(alias='Role')

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetConfiguration(WebSdkEndpoint):
        def post(self):
            class Output(OauthOutputBase):
                configuration: oauth.Configuration = ApiField(alias='Configuration')

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _SetConfiguration(WebSdkEndpoint):
        def post(self, configuration: oauth.Configuration | dict[str, any]):
            if isinstance(configuration, oauth.Configuration):
                configuration = configuration.dict(by_alias=True)
            body = {
                "Configuration": configuration
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CreateApplication(WebSdkEndpoint):
        def post(
            self, application_id: str = None, scope: str = None, maximum_scope: str = None,
            name: str = None, vendor: str = None, description: str = None, url: str = None,
            access_validity: int = None, grant_validity: int = None, renewable: bool = None,
        ):
            body = {
                "ApplicationId" : application_id,
                "Scope"         : scope,
                "MaximumScope"  : maximum_scope,
                "Name"          : name,
                "Vendor"        : vendor,
                "Description"   : description,
                "Url"           : url,
                "AccessValidity": access_validity,
                "GrantValidity" : grant_validity,
                "Renewable"     : renewable,
            }

            class Output(OauthOutputBase):
                application: oauth.Application = ApiField(alias='Application')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Enumerateapplications(WebSdkEndpoint):
        def post(self, start: int = None, count: int = None, order_by: int = 0, descending: bool = True):
            body = {
                "Start"     : start,
                "Count"     : count,
                "OrderBy"   : order_by,
                "Descending": descending,
            }

            class Output(OauthOutputBase):
                applications: list[oauth.Application] = ApiField(alias='Applications')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetApplications(WebSdkEndpoint):
        def post(self, filter: str = None, application_ids: list[str] = None):
            body = {
                "Filter"        : filter,
                "ApplicationIds": application_ids,
            }

            class Output(OauthOutputBase):
                applications: list[oauth.Application] = ApiField(alias='Applications')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetApplication(WebSdkEndpoint):
        def post(self, application_id: int):
            body = {
                'ApplicationId': application_id,
            }

            class Output(OauthOutputBase):
                application: oauth.Application = ApiField(alias='Application')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UpdateApplication(WebSdkEndpoint):
        def post(self, application: oauth.Application | dict):
            if isinstance(application, oauth.Application):
                application = application.dict(by_alias=True)

            body = {
                "Application": application,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteApplication(WebSdkEndpoint):
        def post(self, application_id: int):
            body = {
                "ApplicationId": application_id,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetScopes(WebSdkEndpoint):
        def post(self):
            class Output(OauthOutputBase):
                scopes: list[oauth.Scope]

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetGrants(WebSdkEndpoint):
        def post(
            self,
            grantee_prefixed_universal: str = None,
            application_id: str = None,
            start: int = None,
            count: int = None,
            order_by: int = None,
            descending: bool = None,
            resolve_identities: bool = None,
        ):
            body = {
                "GranteePrefixedUniversal": grantee_prefixed_universal,
                "ApplicationId"           : application_id,
                "Start"                   : start,
                "Count"                   : count,
                "OrderBy"                 : order_by,
                "Descending"              : descending,
                "ResolveIdentities"       : resolve_identities,
            }

            class Output(OauthOutputBase):
                grants: list[oauth.Grant] = ApiField(alias='Grants')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EnumerateGrants(WebSdkEndpoint):
        def post(
            self,
            application_id: str = None,
            start: str = None,
            count: int = None,
            order_by: int = None,
            descending: bool = None,
            resolve_identities: bool = None,
        ):
            body = {
                "ApplicationId"    : application_id,
                "Start"            : start,
                "Count"            : count,
                "OrderBy"          : order_by,
                "Descending"       : descending,
                "ResolveIdentities": resolve_identities,
            }

            class Output(OauthOutputBase):
                grants: list[oauth.Grant] = ApiField(alias='Grants')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RevokeGrants(WebSdkEndpoint):
        def post(
            self,
            application_id: str = None,
            grantee_prefixed_universal: str = None,
        ):
            body = {
                "ApplicationId"           : application_id,
                "GranteePrefixedUniversal": grantee_prefixed_universal,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CreateRule(WebSdkEndpoint):
        def post(
            self,
            application_id: str = None,
            trustee_prefixed_universal: str = None,
            maximum_scope: str = None,
            description: str = None,
            access_validity: int = None,
            grant_validity: int = None,
            renewable: bool = None,
        ):
            body = {
                "ApplicationId"           : application_id,
                "TrusteePrefixedUniversal": trustee_prefixed_universal,
                "MaximumScope"            : maximum_scope,
                "Description"             : description,
                "AccessValidity"          : access_validity,
                "GrantValidity"           : grant_validity,
                "Renewable"               : renewable,
            }

            class Output(OauthOutputBase):
                rule: oauth.Rule = ApiField(alias='Rule')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetRules(WebSdkEndpoint):
        def post(
            self,
            application_id: str = None,
            trustee_prefixed_universal: str = None,
            trustee_prefixed_universals: list[str] = None,
            maximum_scope: str = None,
            renewable: bool = None,
            no_expire: bool = None,
            resolve_identities: bool = None,
        ):
            body = {
                "ApplicationId"            : application_id,
                "TrusteePrefixedUniversal" : trustee_prefixed_universal,
                "TrusteePrefixedUniversals": trustee_prefixed_universals,
                "MaximumScope"             : maximum_scope,
                "Renewable"                : renewable,
                "NoExpire"                 : no_expire,
                "ResolveIdentities"        : resolve_identities,
            }

            class Output(OauthOutputBase):
                rules: list[oauth.Rule] = ApiField(alias='Rules')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EnumerateRules(WebSdkEndpoint):
        def post(
            self,
            application_id: str = None,
            start: int = None,
            count: int = None,
            order_by: int = None,
            descending: bool = None,
            resolve_identities: bool = None,
        ):
            body = {
                "ApplicationId"    : application_id,
                "Start"            : start,
                "Count"            : count,
                "OrderBy"          : order_by,
                "Descending"       : descending,
                "ResolveIdentities": resolve_identities,
            }

            class Output(OauthOutputBase):
                rules: list[oauth.Rule] = ApiField(alias='Rules')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UpdateRule(WebSdkEndpoint):
        def post(self, rule: oauth.Rule | dict[str, any]):
            if isinstance(rule, oauth.Rule):
                rule = rule.dict(by_alias=True)
            body = {
                "Rule": rule,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteRule(WebSdkEndpoint):
        def post(
            self,
            trustee_prefixed_universal: str,
            application_id: str,
        ):
            body = {
                "TrusteePrefixedUniversal": trustee_prefixed_universal,
                "ApplicationId"           : application_id,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteRules(WebSdkEndpoint):
        def post(
            self,
            trustee_prefixed_universal: str,
            application_id: str,
        ):
            body = {
                "TrusteePrefixedUniversal": trustee_prefixed_universal,
                "ApplicationId"           : application_id,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GrantCount(WebSdkEndpoint):
        def post(self, application_id: str):
            body = {
                "ApplicationId": application_id,
            }

            class Output(OauthOutputBase):
                count: int = ApiField(alias='Count')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UserCount(WebSdkEndpoint):
        def post(self, application_id: str):
            body = {
                "ApplicationId": application_id,
            }

            class Output(OauthOutputBase):
                count: int = ApiField(alias='Count')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CreateJwtMapping(WebSdkEndpoint):
        def post(
            self,
            name=None,
            issuer_uri=None,
            purpose_field=None,
            purpose_match=None,
            id_field=None,
            id_match=None,
            grantee_prefixed_universal=None,
        ):
            body = {
                "Name"                    : name,
                "IssuerUri"               : issuer_uri,
                "PurposeField"            : purpose_field,
                "PurposeMatch"            : purpose_match,
                "IdField"                 : id_field,
                "IdMatch"                 : id_match,
                "GranteePrefixedUniversal": grantee_prefixed_universal,
            }

            class Output(OauthOutputBase):
                jwt_mapping: oauth.JwtMapping = ApiField(alias='JwtMapping')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EnumerateJwtMappings(WebSdkEndpoint):
        def post(
            self,
            start: int = None,
            count: int = None,
            order_by: int = None,
            descending: bool = None,
            resolve_identities: bool = None,
        ):
            body = {
                "Start"            : start,
                "Count"            : count,
                "OrderBy"          : order_by,
                "Descending"       : descending,
                "ResolveIdentities": resolve_identities,
            }

            class Output(OauthOutputBase):
                jwt_mappings: list[oauth.JwtMapping] = ApiField(alias='JwtMappings')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetJwtMappings(WebSdkEndpoint):
        def post(
            self,
            filter: str = None,
            issuer_uris: list[str] = None,
            resolve_identities: bool = None
        ):
            body = {
                "Filter"           : filter,
                "IssuerUris"       : issuer_uris,
                "ResolveIdentities": resolve_identities,
            }

            class Output(OauthOutputBase):
                jwt_mappings: list[oauth.JwtMapping] = ApiField(alias='JwtMappings')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetJwtMapping(WebSdkEndpoint):
        def post(
            self,
            name: str,
            resolve_identities: bool = None,
        ):
            body = {
                "Name"             : name,
                "ResolveIdentities": resolve_identities,
            }

            class Output(OauthOutputBase):
                jwt_mapping: oauth.JwtMapping = ApiField(alias='JwtMapping')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UpdateJwtMapping(WebSdkEndpoint):
        def post(self, jwt_mapping: oauth.JwtMapping):
            if isinstance(jwt_mapping, oauth.JwtMapping):
                jwt_mapping = jwt_mapping.dict(by_alias=True)
            body = {
                'JwtMapping': jwt_mapping,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteJwtMapping(WebSdkEndpoint):
        def post(self, name: str):
            body = {
                "Name": name,
            }

            class Output(OauthOutputBase):
                pass

            return generate_output(output_cls=Output, response=self._post(data=body))
