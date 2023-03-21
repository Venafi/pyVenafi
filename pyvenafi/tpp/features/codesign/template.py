from dataclasses import dataclass
from typing import (
    List,
    Union,
)

from pyvenafi.tpp import Authenticate
from pyvenafi.tpp.api.websdk.enums.config import CodeSignAttributeValues
from pyvenafi.tpp.api.websdk.models.codesign import (
    AppleTemplate,
    CertificateTemplate,
    CSPTemplate,
    DotNetTemplate,
    GPGTemplate,
    KeyPairTemplate,
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

@feature('Template')
class CodeSignTemplate(FeatureBase):
    def __init__(
        self,
        api: 'Authenticate'
    ):
        super().__init__(api)

    def create(
        self,
        name: str,
        template_type: Union[str, CodeSignAttributeValues.TemplateType],
        per_user: bool = False,
        parent_folder: Union[Object, str]= r'\VED\Code Signing\Environment Templates',
        raise_if_already_exists: bool = True
    ) -> TemplateTypes:
        """
        Create an environment template.

        Args:
            name: Name of the template.
            template_type: String literal:
                `Code Signing Apple Environment Template`,
                `Code Signing Certificate Environment Template`,
                `Code Signing CSP Environment Template`,
                `Code Signing DotNet Environment Template`,
                `Code Signing Key Pair Environment Template`,
                or `Code Signing GPG Environment Template`
            per_user: Immutable. The mode that supports multiple cryptographic objects to use for signing. Applies only to `Code Signing Certificate Environment Template` and `Code Signing GPG Environment Template`.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            raise_if_already_exists: If the object already exists, raise an error.

        Returns:
            A CodeSign environment template.
        """
        parent_dn = self._get_dn(parent_folder)
        dn = rf'{parent_dn}\{name}'
        try:
            self._api.websdk.Codesign.CreateTemplate.post(
                dn=dn,
                template_type=template_type,
                per_user=per_user
            )
        except:
            if raise_if_already_exists:
                raise
        template = self.get(dn=dn)
        return template

    def update(
        self,
        template: Union[Object, TemplateTypes],
        object_naming_pattern: str = None
    ):
        """
        Update an environment template.

        Args:
            template: The updated template.
            object_naming_pattern: Only valid if the template PerUser attribute is already set to true.
                The pattern that stores signing Certificate objects in the Policy Tree
                by a user's identity. Each signer has a unique Policy folder.
                The default is $Sign.Project$\$Sign.Environment$\$Sign.User$.

        Returns:

        """
        dn = self._get_dn(template)
        self._api.websdk.Codesign.UpdateTemplate.post(
            dn=dn,
            certificate_template=template,
            object_naming_pattern=object_naming_pattern,
        )

    def rename(
        self,
        template: Union[str, Object, TemplateTypes],
        new_dn: str
    ):
        """
        Rename a template by giving it a new :ref:`dn`.

        Args:
            template: Template object, :ref:`config_object`, or :ref:`dn` of the template.
            new_dn: The new :ref:`dn` for the template.
        """
        dn = self._get_dn(template)
        self._api.websdk.Codesign.RenameTemplate.post(new_dn=new_dn, dn=dn)

    def get(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> TemplateTypes:
        """
        Get an environment template using a :ref:`dn`, :ref:`guid`, or Identifier.

        Args:
            dn: :ref:`dn` of the template.
            guid: :ref:`guid` of the template.
            id: Identifier of the template.

        Returns:
            Template object.
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetTemplate.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError('You must provide a dn, guid, or id to get a template.')
        template = (output.apple_template or output.certificate_template or output.csp_template or
                    output.dot_net_template or output.gpg_template or output.key_pair_template)
        if not template:
            raise Exception('Template does not exist.')
        return template

    def enumerate(
        self,
        _filter: str = None
    ):
        """
        Enumerate the environment templates.

        Args:
            _filter: The template name.

        Returns:
            List of environment templates.
        """
        output = self._api.websdk.Codesign.EnumerateTemplates.post(fiter=_filter)

        @dataclass
        class EnumeratedTemplates:
            apple_templates: List[AppleTemplate] = output.apple_templates
            certificate_templates: List[CertificateTemplate] = output.certificate_templates
            csp_templates: List[CSPTemplate] = output.csp_templates
            dot_net_templates: List[DotNetTemplate] = output.dot_net_templates
            gpg_templates: List[GPGTemplate] = output.gpg_templates
            key_pair_templates: List[KeyPairTemplate] = output.key_pair_templates

        return EnumeratedTemplates()

    def delete(
        self,
        template: Union[str, Object, TemplateTypes],
        force: bool = False
    ):
        """
        Delete an environment template.

        Args:
            template: Template object, :ref:`dn` , or :ref:`config_object` of the template.
            force: Force the deletion of the template. If true, the template will be deleted even if it is in use.
                If false, the template will only be deleted if it is not in use.
        """
        dn = self._get_dn(template)
        if dn:
            self._api.websdk.Codesign.DeleteTemplate.post(dn=dn, force=force)
        else:
            guid = self._get_guid(template)
            if guid:
                self._api.websdk.Codesign.DeleteTemplate.post(guid=guid, force=force)
            else:
                raise ValueError('Invalid argument to delete the template.')
