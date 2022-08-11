from typing import List, Dict, Union
from pytpp.api.websdk.outputs import codesign
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Codesign:
    def __init__(self, api_obj):
        self.AddAdministrator = self._AddAdministrator(api_obj=api_obj)
        self.AddApplicationAdministrator = self._AddApplicationAdministrator(api_obj=api_obj)
        self.AddProjectAdministrator = self._AddProjectAdministrator(api_obj=api_obj)
        self.AddProjectApprover = self._AddProjectApprover(api_obj=api_obj)
        self.CountReferences = self._CountReferences(api_obj=api_obj)
        self.CreateApplication = self._CreateApplication(api_obj=api_obj)
        self.CreateApplicationCollection = self._CreateApplicationCollection(api_obj=api_obj)
        self.CreateEnvironment = self._CreateEnvironment(api_obj=api_obj)
        self.CreateProject = self._CreateProject(api_obj=api_obj)
        self.CreateTemplate = self._CreateTemplate(api_obj=api_obj)
        self.DeleteApplication = self._DeleteApplication(api_obj=api_obj)
        self.DeleteApplicationCollection = self._DeleteApplicationCollection(api_obj=api_obj)
        self.DeleteEnvironment = self._DeleteEnvironment(api_obj=api_obj)
        self.DeleteProject = self._DeleteProject(api_obj=api_obj)
        self.DeleteTemplate = self._DeleteTemplate(api_obj=api_obj)
        self.EnumerateApplications = self._EnumerateApplications(api_obj=api_obj)
        self.EnumerateApplicationCollections = self._EnumerateApplicationCollections(api_obj=api_obj)
        self.EnumerateProjects = self._EnumerateProjects(api_obj=api_obj)
        self.EnumerateReferences = self._EnumerateReferences(api_obj=api_obj)
        self.EnumerateTemplates = self._EnumerateTemplates(api_obj=api_obj)
        self.GetApplication = self._GetApplication(api_obj=api_obj)
        self.GetApplicationCollection = self._GetApplicationCollection(api_obj=api_obj)
        self.GetApplicationCollectionMembers = self._GetApplicationCollectionMembers(api_obj=api_obj)
        self.GetApplicationCollectionMemberDNs = self._GetApplicationCollectionMemberDNs(api_obj=api_obj)
        self.GetEnvironment = self._GetEnvironment(api_obj=api_obj)
        self.GetGlobalConfiguration = self._GetGlobalConfiguration(api_obj=api_obj)
        self.GetObjectRights = self._GetObjectRights(api_obj=api_obj)
        self.GetProject = self._GetProject(api_obj=api_obj)
        self.GetRight = self._GetRight(api_obj=api_obj)
        self.GetTemplate = self._GetTemplate(api_obj=api_obj)
        self.GetTrusteeRights = self._GetTrusteeRights(api_obj=api_obj)
        self.RemoveAdministrator = self._RemoveAdministrator(api_obj=api_obj)
        self.RemoveApplicationAdministrator = self._RemoveApplicationAdministrator(api_obj=api_obj)
        self.RemoveProjectAdministrator = self._RemoveProjectAdministrator(api_obj=api_obj)
        self.RenameApplication = self._RenameApplication(api_obj=api_obj)
        self.RenameApplicationCollection = self._RenameApplicationCollection(api_obj=api_obj)
        self.RenameProject = self._RenameProject(api_obj=api_obj)
        self.RenameTemplate = self._RenameTemplate(api_obj=api_obj)
        self.SetGlobalConfiguration = self._SetGlobalConfiguration(api_obj=api_obj)
        self.UpdateApplication = self._UpdateApplication(api_obj=api_obj)
        self.UpdateApplicationCollection = self._UpdateApplicationCollection(api_obj=api_obj)
        self.UpdateEnvironment = self._UpdateEnvironment(api_obj=api_obj)
        self.UpdateProject = self._UpdateProject(api_obj=api_obj)
        self.UpdateProjectStatus = self._UpdateProjectStatus(api_obj=api_obj)
        self.UpdateTemplate = self._UpdateTemplate(api_obj=api_obj)

    class _AddAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddApplicationAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddApplicationAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddProjectAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddProjectAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddProjectApprover(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddProjectApprover')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddPreApproval(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/AddPreApproval')

        def post(self, dn: str, comment: str, user: str, hours: int = None, ip_address: str = None,
                 signing_executable: str = None, single_use: bool = None, not_before: str = None, ):
            body = {
                'Dn'               : dn,
                'Comment'          : comment,
                'Hours'            : hours,
                'IPAddress'        : ip_address,
                'SigningExecutable': signing_executable,
                'SingleUse'        : single_use,
                'User'             : user,
                'NotBefore'        : not_before
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CountReferences(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CountReferences')

        def post(self, application: dict = None, application_collection: dict = None):
            body = {
                'Application'          : application,
                'ApplicationCollection': application_collection
            }

            class Output(WebSdkOutputModel):
                count: int = ApiField(alias='Count')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateApplication(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateApplication')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                application: codesign.Application = ApiField(alias='Application')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateApplicationCollection(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateApplicationCollection')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                application: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateEnvironment(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateEnvironment')

        def post(self, dn: str, environment_name: str, project: Dict[str, Union[str, int]],
                 template: List[Dict[str, str]], template_dn: str = None):
            body = {
                'Dn'             : dn,
                'EnvironmentName': environment_name,
                'Project'        : project,
                'Template'       : template,
                'TemplateDn'     : template_dn
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                apple_template: codesign.AppleTemplate = ApiField(alias='AppleTemplate')
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                csp_template: codesign.CSPTemplate = ApiField(alias='EnviCSPTemplateronment')
                dot_net_template: codesign.DotNetTemplate = ApiField(alias='DotNetTemplate')
                gpg_template: codesign.GPGTemplate = ApiField(alias='GPGTemplate')
                key_pair_template: codesign.KeyPairTemplate = ApiField(alias='KeyPairTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateProject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateProject')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                project: codesign.Project = ApiField(alias='Project')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CreateTemplate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/CreateTemplate')

        def post(self, dn: str, template_type: codesign.TemplateType = None, per_user: bool = None):
            body = {
                'Dn'          : dn,
                'TemplateType': template_type,
                'PerUser'     : per_user
            }

            class Output(WebSdkOutputModel):
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteApplication(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteApplication')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteApplicationCollection(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteApplicationCollection')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteEnvironment(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteEnvironment')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteProject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteProject')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DeleteTemplate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/DeleteTemplate')

        def post(self, dn: str = None, force: bool = None, guid: str = None, id: int = None):
            body = {
                'Dn'   : dn,
                'Force': force,
                'Guid' : guid,
                'Id'   : id
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateApplications(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateApplications')

        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                applications: List[codesign.Application] = ApiField(alias='Applications')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateApplicationCollections(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateApplicationCollections')

        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                application_collections: List[codesign.ApplicationCollection] = ApiField(alias='ApplicationCollections')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateProjects(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateProjects')

        # noinspection ALL
        def post(self, filter: str = None, rights: int = None):
            body = {
                'Filter': filter,
                'Rights': rights
            }

            class Output(WebSdkOutputModel):
                projects: List[codesign.Project] = ApiField(alias='Projects')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateReferences(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateReferences')

        def post(self, application: dict = None, application_collection: dict = None,
                 application_dn: str = None, application_guid: str = None,
                 collection_dn: str = None, collection_guid: str = None):
            body = {
                'Application'          : application,
                'ApplicationCollection': application_collection,
                'ApplicationDn'        : application_dn,
                'ApplicationGuid'      : application_guid,
                'CollectionDn'         : collection_dn,
                'CollectionGuid'       : collection_guid
            }

            class Output(WebSdkOutputModel):
                reference_dns: List[str] = ApiField(alias='ReferenceDNs')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateTemplates(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/EnumerateTemplates')

        # noinspection ALL
        def post(self, filter: str = None):
            body = {
                'Filter': filter
            }

            class Output(WebSdkOutputModel):
                apple_templates: List[codesign.AppleTemplate] = ApiField(alias='AppleTemplates')
                certificate_templates: List[codesign.CertificateTemplate] = ApiField(alias='CertificateTemplates')
                csp_templates: List[codesign.CSPTemplate] = ApiField(alias='CSPTemplates')
                dot_net_templates: List[codesign.DotNetTemplate] = ApiField(alias='DotNetTemplates')
                gpg_templates: List[codesign.GPGTemplate] = ApiField(alias='GPGTemplates')
                key_pair_templates: List[codesign.KeyPairTemplate] = ApiField(alias='KeyPairTemplates')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplication(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplication')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application: codesign.Application = ApiField(alias='Application')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollection(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollection')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollectionMembers(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollectionMembers')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetApplicationCollectionMemberDNs(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetApplicationCollectionMemberDNs')

        def post(self, dn: str = None, guid: str = None, id: int = None, application: dict = None):
            body = {
                'Application': application,
                'Dn'         : dn,
                'Guid'       : guid,
                'Id'         : id
            }

            class Output(WebSdkOutputModel):
                application_collection: codesign.ApplicationCollection = ApiField(alias='ApplicationCollection')
                application_collection_dns: List[str] = ApiField(alias='ApplicationCollectionDNs')
                application_dns: List[str] = ApiField(alias='ApplicationDNs')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetEnvironment(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetEnvironment')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetGlobalConfiguration(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetGlobalConfiguration')

        def get(self):
            class Output(WebSdkOutputModel):
                global_configuration: codesign.GlobalConfiguration = ApiField(alias='GlobalConfiguration')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._get(), output_cls=Output)

    class _GetObjectRights(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetObjectRights')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights_list: List[codesign.RightsKeyValue] = ApiField(alias='RightsList')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetProject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetProject')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                project: codesign.Project = ApiField(alias='Project')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetRight(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetRight')

        def post(self, dn: str):
            body = {
                'Dn': dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights: codesign.Rights = ApiField(alias='Rights', converter=lambda x: codesign.Rights(value=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetTemplate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetTemplate')

        def post(self, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id
            }

            class Output(WebSdkOutputModel):
                apple_template: codesign.AppleTemplate = ApiField(alias='AppleTemplate')
                certificate_template: codesign.CertificateTemplate = ApiField(alias='CertificateTemplate')
                csp_template: codesign.CSPTemplate = ApiField(alias='CSPTemplate')
                dot_net_template: codesign.DotNetTemplate = ApiField(alias='DotNetTemplate')
                gpg_template: codesign.GPGTemplate = ApiField(alias='GPGTemplate')
                key_pair_template: codesign.KeyPairTemplate = ApiField(alias='KeyPairTemplate')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetTrusteeRights(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/GetTrusteeRights')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                rights_list : List[codesign.RightsKeyValue] = ApiField(alias='RightsList')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveApplicationAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveApplicationAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveProjectAdministrator(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveProjectAdministrator')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveProjectApprover(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RemoveProjectApprover')

        def post(self, trustee: str):
            body = {
                'Trustee': trustee
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameApplication(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameApplication')

        def post(self, dn: str, new_dn: str):
            body = {
                'Dn'   : dn,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameApplicationCollection(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameApplicationCollection')

        def post(self, dn: str, new_dn: str):
            body = {
                'Dn'   : dn,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameProject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameProject')

        def post(self, new_dn: str, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'   : dn,
                'Guid' : guid,
                'Id'   : id,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RenameTemplate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/RenameTemplate')

        def post(self, new_dn: str, dn: str = None, guid: str = None):
            body = {
                'Dn'  : dn,
                'Guid': guid,
                'Id'  : id,
                'NewDn': new_dn
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _SetGlobalConfiguration(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/SetGlobalConfiguration')

        def post(self, global_configuration: dict):
            body = {
                'GlobalConfiguration': global_configuration
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateApplication(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateApplication')

        def post(self, application: dict):
            body = {
                'Application': application
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateApplicationCollection(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateApplicationCollection')

        def post(self, application_collection: dict):
            body = {
                'ApplicationCollection': application_collection
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateEnvironment(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateEnvironment')

        def post(self, certificate_environment: dict = None, apple_environment: dict = None, csp_environment: dict = None,
                 dot_net_environment: dict = None, gpg_environment: dict = None, key_pair_environment: dict = None):
            body = {
                'AppleEnvironment'      : apple_environment,
                'CertificateEnvironment': certificate_environment,
                'CSPEnvironment'        : csp_environment,
                'DotNetEnvironment'     : dot_net_environment,
                'GPGEnvironment'        : gpg_environment,
                'KeyPairEnvironment'    : key_pair_environment
            }

            class Output(WebSdkOutputModel):
                apple_environment: codesign.AppleEnvironment = ApiField(alias='AppleEnvironment')
                certificate_environment: codesign.CertificateEnvironment = ApiField(alias='CertificateEnvironment')
                csp_environment: codesign.CSPEnvironment = ApiField(alias='CSPEnvironment')
                dot_net_environment: codesign.DotNetEnvironment = ApiField(alias='DotNetEnvironment')
                gpg_environment: codesign.GPGEnvironment = ApiField(alias='GPGEnvironment')
                key_pair_environment: codesign.KeyPairEnvironment = ApiField(alias='KeyPairEnvironment')
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateProject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateProject')

        def post(self, project: dict):
            body = {
                'Project': project
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateProjectStatus(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateProjectStatus')

        def post(self, project_status: int, dn: str = None, guid: str = None, id: int = None):
            body = {
                'Dn'           : dn,
                'Guid'         : guid,
                'Id'           : id,
                'ProjectStatus': project_status,
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _UpdateTemplate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Codesign/UpdateTemplate')

        def post(self, dn: str, certificate_template: dict, object_naming_pattern: str = None):
            body = {
                'Dn'                 : dn,
                'CertificateTemplate': certificate_template,
                'ObjectNamingPattern': object_naming_pattern
            }

            class Output(WebSdkOutputModel):
                result: codesign.ResultCode = ApiField(alias='Result', converter=lambda x: codesign.ResultCode(code=x))
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)
