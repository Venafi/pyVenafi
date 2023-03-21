from typing import (
    Iterable,
    List,
    Union,
)

from pyvenafi.tpp.api.websdk.enums.config import CodeSignAttributeValues
from pyvenafi.tpp.api.websdk.models.codesign import (
    AppleEnvironment,
    Application,
    ApplicationCollection,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    Items,
    KeyPairEnvironment,
    Project,
    Rights,
)
from pyvenafi.tpp.api.websdk.models.config import Object
from pyvenafi.tpp.api.websdk.models.identity import Identity
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

EnvironmentTypes = Union[
    AppleEnvironment,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    KeyPairEnvironment,
]

@feature('Project')
class CodeSignProject(FeatureBase):
    def create(
        self,
        name: str,
        owners: Iterable[Union[Identity, str]],
        parent_folder: Union[Object, str] = r'\VED\Code Signing\Projects',
        applications: Iterable[Union[str, Object, Application, ApplicationCollection]] = None,
        auditors: Iterable[Union[Identity, str]] = None,
        description: str = None,
        key_use_approvers: Iterable[Union[Identity, str]] = None,
        key_users: Iterable[Union[Identity, str]] = None,
        environments: Iterable[Union[Object, EnvironmentTypes]] = None,
        raise_if_already_exists: bool = False
    ) -> Project:
        """
        Create a project with the specified values.

        Args:
            name: Name of the project.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            applications: List of :class:`~.models.codesign.Application`\s, :class:`~.models.codesign.ApplicationCollection`\s, :ref:`config_object`\s, or :ref:`dn`\s of application or application collections.
            auditors: List of :ref:`identity_object`\s, :ref:`config_object`\s, or prefixed universal of identities to be project auditors.
            description: Description of the project.
            key_use_approvers: List of :ref:`identity_object`\s, :ref:`config_object`\s, or prefixed universal of identities who can approve environment usage.
            key_users: List of :ref:`identity_object`\s, :ref:`config_object`\s, or prefixed universal of identities who can sign with environments.
            owners: List of :ref:`identity_object`\s, :ref:`config_object`\s, or prefixed universal of identities to be project owners.
            environments: List of signing environments for the project.
            raise_if_already_exists: If the object already exists, raise an error.

        Returns:
            :class:`~.models.codesign.Project`
        """
        parent_dn = self._get_dn(parent_folder)

        applications = [self._get_dn(x) for x in applications] if applications else []
        auditors = [self._get_prefixed_universal(x) for x in auditors] if auditors else []
        key_use_approvers = [self._get_prefixed_universal(x) for x in key_use_approvers] if key_use_approvers else []
        key_users = [self._get_prefixed_universal(x) for x in key_users] if key_users else []
        owners = [self._get_prefixed_universal(x) for x in owners] if owners else []
        dn = rf'{parent_dn}\{name}'
        environments = environments or []

        # Create the project
        try:
            self._api.websdk.Codesign.CreateProject.post(dn=dn)
        except:
            if raise_if_already_exists:
                raise

        project = self.get(dn=dn)

        # Update project attributes
        if any(
                [
                    applications,
                    auditors,
                    description,
                    key_use_approvers,
                    key_users,
                    owners,
                    environments,
                ]
        ):
            project.description = description
            project.application_dns = Items(items=applications)
            project.auditors = Items(items=auditors)
            project.key_use_approvers = Items(items=key_use_approvers)
            project.key_users = Items(items=key_users)
            project.owners = Items(items=owners)

            self.update(project=project)

        templates = self._api.websdk.Codesign.EnumerateTemplates.post()

        def get_env_template_and_update_kwargs(
            _e: EnvironmentTypes
        ):
            try:
                if isinstance(_e, AppleEnvironment):
                    _key, _templates = 'apple_environment', templates.apple_templates
                elif isinstance(_e, CertificateEnvironment):
                    _key, _templates = 'certificate_environment', templates.certificate_templates
                elif isinstance(_e, CSPEnvironment):
                    _key, _templates = 'csp_environment', templates.csp_templates
                elif isinstance(_e, DotNetEnvironment):
                    _key, _templates = 'dot_net_environment', templates.dot_net_templates
                elif isinstance(_e, GPGEnvironment):
                    _key, _templates = 'gpg_environment', templates.gpg_templates
                elif isinstance(_e, KeyPairEnvironment):
                    _key, _templates = 'key_pair_environment', templates.key_pair_templates
                else:
                    raise ValueError(f'Invalid type {type(_e)}')
                _template = next(t for t in _templates if t.dn == _e.template_dn)
                return _template, {
                    _key: _e
                }
            except:
                raise ValueError(f'Unable to find template "{_e.template_dn}" for environment "{_e.dn}".')

        for e in environments:
            template, update_kwargs = get_env_template_and_update_kwargs(e)
            self._api.websdk.Codesign.CreateEnvironment.post(
                dn=e.dn,
                project={
                    'Dn'  : project.dn,
                    'Guid': project.guid,
                    'Id'  : project.id
                },
                template=template,
                template_dn=template.dn
            )
            self._api.websdk.Codesign.UpdateEnvironment.post(**update_kwargs)

        return self.get(guid=project.guid)

    def update(
        self,
        project: Project
    ):
        """
        Update a project.

        Args:
            project: The updated :class:`~.models.codesign.Project`.
        """
        self._api.websdk.Codesign.UpdateProject.post(project=project)

    def rename(
        self,
        project: Union[str, Object, Project],
        new_dn: str
    ):
        """
        Rename a project by giving it a new :ref:`dn`.

        Args:
            project: :class:`~.models.codesign.Project`, :ref:`config_object`, or :ref:`dn` of the project.
            new_dn: The new :ref:`dn` for the project.
        """
        dn = self._get_dn(project)
        self._api.websdk.Codesign.RenameProject.post(new_dn=new_dn, dn=dn)

    def get(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> Project:
        """
       Get a project using a :ref:`dn`, :ref:`guid`, or Identifier.

       Args:
           dn: :ref:`dn` of the project object.
           guid: :ref:`guid` of the project object.
           id: Identifier of the project object.

       Returns:
           :class:`~.models.codesign.Project`
       """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetProject.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError('You must provide a dn, guid, or id to get a project.')
        if not output.project:
            raise Exception('Project does not exist.')
        return output.project

    def enumerate(
        self,
        _filter: str = None,
        rights: Union[int, Rights] = None
    ) -> List[Project]:
        """
        Enumerate the projects.

        Args:
            _filter: A simple filter on the project name.
            rights: Show only projects for which you have a minimum set of permissions. See :class:`~.models.codesign.Rights`.

        Returns:
            List[:class:`~.models.codesign.Project`]
        """
        if isinstance(rights, Rights):
            rights = rights.value
        output = self._api.websdk.Codesign.EnumerateProjects.post(filter=_filter, rights=rights)
        return output.projects

    def delete(
        self,
        project: Union[str, Object, Project]
    ):
        """
        Delete a project.

        Args:
            project: :class:`~.models.codesign.Project`, :ref:`dn`, or :ref:`config_object` of the project.
        """
        dn = self._get_dn(project)
        if dn:
            self._api.websdk.Codesign.DeleteProject.post(dn=dn)
        else:
            guid = self._get_guid(project)
            if guid:
                self._api.websdk.Codesign.DeleteProject.post(guid=guid)
            else:
                raise ValueError('Invalid argument to delete the project.')

    # region Update Project Status
    def disable(
        self,
        project: Union[Object, Project]
    ):
        """
        Disable a project. Changes project status to "disabled".

        Args:
            project: :class:`~.models.codesign.Project` to disable.
        """
        self.update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.disabled)

    def submit_for_approval(
        self,
        project: Union[Object, Project]
    ):
        """
        Submit a "draft" project to be approved. Changes project status to "pending".

        Args:
            project: :class:`~.models.codesign.Project` to submit.
        """
        dn = self._get_dn(project)
        project = self.get(dn=dn)
        if project.status == int(CodeSignAttributeValues.ProjectStatus.draft):
            self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.pending)

    def approve(
        self,
        project: Union[Object, Project]
    ):
        """
        Approve a "pending" project. Changes project status to "enabled".

        Args:
            project: :class:`~.models.codesign.Project` to approve.
        """
        dn = self._get_dn(project)
        project = self.get(dn=dn)
        if project.status == int(CodeSignAttributeValues.ProjectStatus.pending):
            self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.enabled)

    def submit_and_approve(
        self,
        project: Union[Object, Project]
    ):
        """
        Approves a "draft" or "pending" project. Changes project status to "enabled".

        Args:
            project: :class:`~.models.codesign.Project` to submit and approve.
        """
        dn = self._get_dn(project)
        project = self.get(dn=dn)
        if project.status == int(CodeSignAttributeValues.ProjectStatus.draft):
            self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.pending)
            self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.enabled)
        if project.status == int(CodeSignAttributeValues.ProjectStatus.pending):
            self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.enabled)

    def _update_status(
        self,
        project: Union[Object, Project],
        project_status: Union[int, CodeSignAttributeValues.ProjectStatus]
    ):
        project_status = int(project_status)
        dn = self._get_dn(project)
        self._api.websdk.Codesign.UpdateProjectStatus.post(project_status=project_status, dn=dn)
    # endregion Update Project Status
