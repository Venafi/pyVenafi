from __future__ import annotations

import time
from typing import (
    Iterable,
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
            applications: List of :class:`~.models.codesign.Application`, :class:`~.models.codesign.ApplicationCollection`, :ref:`config_object`, or :ref:`dn` of application or application collections.
            auditors: List of :ref:`identity_object`, :ref:`config_object`, or prefixed universal of identities to be project auditors.
            description: Description of the project.
            key_use_approvers: List of :ref:`identity_object`, :ref:`config_object`, or prefixed universal of identities who can approve environment usage.
            key_users: List of :ref:`identity_object`, :ref:`config_object`, or prefixed universal of identities who can sign with environments.
            owners: List of :ref:`identity_object`, :ref:`config_object`, or prefixed universal of identities to be project owners.
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

        self.enable(project=dn)
        time.sleep(5)
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
            ]
        ):
            project.description = description
            project.application_dns = Items(items=applications)
            project.auditors = Items(items=auditors)
            project.key_use_approvers = Items(items=key_use_approvers)
            project.key_users = Items(items=key_users)
            project.owners = Items(items=owners)
            project.status = CodeSignAttributeValues.ProjectStatus.enabled

            self.update(project=project)

        # Add environments
        if environments:
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
        response = self._api.websdk.Codesign.UpdateProject.post(project=project)
        response.assert_valid_response()
        if response.error:
            raise Exception(response.error)

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
    ) -> list[Project]:
        """
        Enumerate the projects.

        Args:
            _filter: A simple filter on the project name.
            rights: Show only projects for which you have a minimum set of permissions. See :class:`~.models.codesign.Rights`.

        Returns:
            list[:class:`~.models.codesign.Project`]
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
        project: Union[Object, Project, str]
    ):
        """
        Disable a project. Changes project status to "disabled".

        Args:
            project: :class:`~.models.codesign.Project` to disable.
        """
        self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.disabled)

    def enable(
        self,
        project: Union[Object, Project, str]
    ):
        """
        Enable a project.

        Args:
            project: :class:`~.models.codesign.Project` to enable.
        """
        dn = self._get_dn(project)
        project = self.get(dn=dn)
        match project.status:
            case CodeSignAttributeValues.ProjectStatus.enabled:
                return  # project is already enabled
            case CodeSignAttributeValues.ProjectStatus.disabled:
                # re-enable the project
                self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.enabled)
            case CodeSignAttributeValues.ProjectStatus.draft | CodeSignAttributeValues.ProjectStatus.pending:
                # make sure project has pending status to create a flow ticket
                if project.status == CodeSignAttributeValues.ProjectStatus.draft:
                    self._update_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.pending)

                # approve the flow ticket to enable the project
                try:
                    self._approve_flow_ticket(project=project)
                    self._wait_for_status(project=project, project_status=CodeSignAttributeValues.ProjectStatus.enabled)
                except:
                    self._api.websdk.Config.Write.post(
                        object_dn=dn,
                        attribute_data=[{'Status': [1]}]
                    )
                    self._api.websdk.Config.ClearAttribute.post(object_dn=dn, attribute_name='Disabled')
            case CodeSignAttributeValues.ProjectStatus.disabled_by_parent:
                raise ValueError(f'Project is disabled by parent. Enable the parent first and try again.')
            case CodeSignAttributeValues.ProjectStatus.deleted:
                raise ValueError(f'Project is marked for deletion.')
            case _:
                raise ValueError(f'Invalid project status {project.status}.')

    def _update_status(
        self,
        project: Union[Object, Project],
        project_status: Union[int, CodeSignAttributeValues.ProjectStatus]
    ):
        project_status = int(project_status)
        dn = self._get_dn(project)
        output = self._api.websdk.Codesign.UpdateProjectStatus.post(project_status=project_status, dn=dn)
        output.assert_valid_response()
        if output.error:
            raise Exception(output.error)
        self._wait_for_status(project=project, project_status=project_status)

    def _wait_for_status(
        self,
        project: Union[Object, Project],
        project_status: Union[int, CodeSignAttributeValues.ProjectStatus],
        timeout: float = 120.0,
        interval: float = 1.0
    ):
        project_status = int(project_status)
        current_status = None
        dn = self._get_dn(project)

        start = time.time()
        while time.time() < start + timeout:
            project = self.get(dn=dn)
            if project.status == project_status:
                return
            current_status = int(project.status)
            time.sleep(interval)
        raise TimeoutError(
            f'Timed out waiting for project status {project_status}. '
            f'Current status is {current_status}.'
        )

    def _approve_flow_ticket(
        self,
        project: Union[Project, Object, str],
        attempts: int = 5,
        interval: float = 5.0
    ):
        dn = self._get_dn(project)
        for i in range(attempts):
            tickets = self._api.websdk.Flow.Tickets.Enumerate.post().tickets
            for ticket in tickets:
                for key_value in ticket.environment:
                    if key_value.key == 'ObjectDn' and key_value.value == dn:
                        self._api.websdk.Flow.Tickets.Approve.post(ticket_id=ticket.id)
                        return
            time.sleep(interval)
        raise ValueError(f'No flow ticket found for {dn} after {attempts} attempts.')
    # endregion Update Project Status
