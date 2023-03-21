from typing import (
    List,
    Union,
)

from pyvenafi.tpp import Authenticate
from pyvenafi.tpp.api.websdk.models.codesign import (
    AppleEnvironment,
    CertificateEnvironment,
    CSPEnvironment,
    DotNetEnvironment,
    GPGEnvironment,
    KeyPairEnvironment,
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

@feature('Rights')
class CodeSignRights(FeatureBase):
    def __init__(
        self,
        api: 'Authenticate'
    ):
        super().__init__(api)

    def add_administrator(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Grant Code Signing Administrator rights to allow a trustee to administer any CodeSign Protect project.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.AddAdministrator.post(prefixed_universal)

    def add_application_administrator(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Grant Code Signing Application Administrator rights to a trustee.
        The Code Signing Application Administrator has permissions to
        :class:`~.models.codesign.Application` and :class:`~.models.codesign.ApplicationCollection`
        objects in CodeSign Protect.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.AddApplicationAdministrator.post(prefixed_universal)

    def add_project_approver(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Grant Project Approval rights to a trustee to sign projects.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.AddProjectApprover.post(prefixed_universal)

    def remove_administrator(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Revoke Code Signing Administrator rights from a trustee.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.RemoveAdministrator.post(prefixed_universal)

    def remove_application_administrator(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Revoke Code Signing Application Administrator rights from a trustee.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.RemoveApplicationAdministrator.post(prefixed_universal)

    def remove_project_approver(
        self,
        trustee: Union[str, Identity]
    ):
        """
        Revoke Key Use Approver rights from a trustee.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        self._api.websdk.Codesign.RemoveProjectApprover.post(prefixed_universal)

    def get_right(
        self,
        obj: Union[str, Object]
    ) -> Rights:
        """
        Returns your rights for a CodeSign Protect object.

        Args:
            obj: :ref:`dn` or :ref:`config_object`

        Returns:
            :class:`~.models.codesign.Rights`
        """
        dn = self._get_dn(obj)
        output = self._api.websdk.Codesign.GetRight.post(dn=dn)
        return output.rights

    def get_trustee_rights(
        self,
        trustee: Union[str, Identity]
    ) -> List[Rights]:
        """
        Returns all CodeSign Protect code signing rights for a user.

        Args:
            trustee: :ref:`identity_object`, :ref:`config_object`, or prefixed universal of an identity.

        Returns:
            :class:`~.models.codesign.Rights`
        """
        prefixed_universal = self._get_prefixed_universal(trustee)
        output = self._api.websdk.Codesign.GetTrusteeRights.post(trustee=prefixed_universal)
        rights_list = [Rights(value=r.value) for r in output.rights_list]
        return rights_list

    def get_object_rights(
        self,
        obj: Union[str, Object]
    ) -> List[Rights]:
        """
        Returns all identities that have rights to a CodeSign Protect object.

        Args:
            obj: :ref:`dn` or :ref:`config_object`

        Returns:
            :class:`~.models.codesign.Rights`
        """
        dn = self._get_dn(obj)
        output = self._api.websdk.Codesign.GetObjectRights.post(dn=dn)
        rights_list = [Rights(value=r.value) for r in output.rights_list]
        return rights_list
