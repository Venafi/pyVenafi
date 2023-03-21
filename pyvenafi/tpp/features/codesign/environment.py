from typing import Union

from pyvenafi.tpp.api.websdk.enums.config import CodeSignAttributeValues
from pyvenafi.tpp.api.websdk.models.codesign import (
    AppleEnvironment,
    AppleTemplate,
    CertificateEnvironment,
    CertificateTemplate,
    CSPEnvironment,
    CSPTemplate,
    DotNetEnvironment,
    DotNetTemplate,
    GPGEnvironment,
    GPGTemplate,
    KeyPairEnvironment,
    KeyPairTemplate,
    Project,
)
from pyvenafi.tpp.api.websdk.models.config import Object
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

TemplateTypes = Union[
    AppleTemplate,
    CertificateTemplate,
    CSPTemplate,
    DotNetTemplate,
    GPGTemplate,
    KeyPairTemplate,
]

EnvironmentTypes = Union[
    AppleEnvironment,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    KeyPairEnvironment,
]

@feature('Environment')
class CodeSignEnvironment(FeatureBase):
    def create(
        self,
        name: str,
        template: Union[str, Object, TemplateTypes],
        project: Union[str, Object, Project],
        raise_if_already_exists: bool = False,
    ) -> EnvironmentTypes:
        """
        Create an environment for a project using a template.

        Args:
            name: Name of the environment.
            template: :class:`~.models.codesign.Template`.
            project: :class:`~.models.codesign.Project`.
            raise_if_already_exists: If the object already exists, raise an error.

        Returns:
            A CodeSign Environment
        """

        project_dn = self._get_dn(project)
        project = self._api.websdk.Codesign.GetProject.post(dn=project_dn).project

        project_dn = project_dn.replace("\\", "\\\\")
        dn = rf'{project_dn}\\{name}'

        template_dn = self._get_dn(template)
        template_output = self._api.websdk.Codesign.GetTemplate.post(dn=template_dn)
        template_types = {
            CodeSignAttributeValues.TemplateTypeKey.apple_template      : template_output.apple_template,
            CodeSignAttributeValues.TemplateTypeKey.certificate_template: template_output.certificate_template,
            CodeSignAttributeValues.TemplateTypeKey.csp_template        : template_output.csp_template,
            CodeSignAttributeValues.TemplateTypeKey.dotnet_template     : template_output.dot_net_template,
            CodeSignAttributeValues.TemplateTypeKey.gpg_template        : template_output.gpg_template,
            CodeSignAttributeValues.TemplateTypeKey.key_pair_template   : template_output.key_pair_template
        }
        try:
            template_type, template = next((k, v) for k, v in template_types.items() if v)
        except:
            raise ValueError('The template provided does not exist.')

        try:
            self._api.websdk.Codesign.CreateEnvironment.post(
                dn=dn,
                project={
                    'Dn'  : project_dn,
                    'Guid': self._get_guid(project),
                    'Id'  : project.id
                },
                environment_name=name,
                template_dn=template_dn.replace("\\", "\\\\"),
                template_type=template_type,
                template=template
            )
        except:
            if raise_if_already_exists:
                raise

        environment = self.get(dn=dn)
        return environment

    def update(
        self,
        environment: Union[Object, EnvironmentTypes]
    ):
        """
        Update an environment.

        Args:
            environment: The updated environment.
        """
        if isinstance(environment, AppleEnvironment):
            key = 'apple_environment'
        elif isinstance(environment, CertificateEnvironment):
            key = 'certificate_environment'
        elif isinstance(environment, CSPEnvironment):
            key = 'csp_environment'
        elif isinstance(environment, DotNetEnvironment):
            key = 'dot_net_environment'
        elif isinstance(environment, GPGEnvironment):
            key = 'gpg_environment'
        elif isinstance(environment, KeyPairEnvironment):
            key = 'key_pair_environment'
        else:
            raise ValueError(f'Invalid type {type(environment)}')
        kwargs = {
            key: environment
        }
        self._api.websdk.Codesign.UpdateEnvironment.post(**kwargs)

    def get(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> EnvironmentTypes:
        """
        Get an environment using a :ref:`dn`, :ref:`guid`, or Identifier.

        Args:
            dn: :ref:`dn` of the environment.
            guid: :ref:`guid` of the environment.
            id: Identifier of the environment.

        Returns:
            A CodeSign environment.
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetEnvironment.post(dn=dn, guid=guid, id=id)
            output.assert_valid_response()
        else:
            raise ValueError('You must provide a dn, guid, or id to get an environment.')
        environment = (output.apple_environment or output.certificate_environment or output.csp_environment or
                       output.dot_net_environment or output.gpg_environment or output.key_pair_environment)
        if not environment:
            raise Exception('Environment does not exist.')
        return environment

    def delete(
        self,
        environment: Union[str, Object, EnvironmentTypes]
    ):
        """
        Delete an environment.

        Args:
            environment: Environment, :ref:`dn` , or :ref:`config_object` of the environment.
        """
        dn = self._get_dn(environment)
        if dn:
            self._api.websdk.Codesign.DeleteEnvironment.post(dn=dn)
        else:
            guid = self._get_guid(environment)
            if guid:
                self._api.websdk.Codesign.DeleteEnvironment.post(guid=guid)
            else:
                raise ValueError('Invalid argument to delete the environment.')
