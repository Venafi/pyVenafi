from typing import (
    List,
    Literal,
)

from pyvenafi.tpp.api.websdk.models.codesign import (
    GlobalConfiguration,
    Items,
)
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

@feature('Global Configuration')
class CodeSignGlobalConfiguration(FeatureBase):
    def get(
        self
    ) -> GlobalConfiguration:
        """
        Returns settings that apply to all CodeSign Protect projects.

        Returns:
            :class:`~.models.codesign.GlobalConfiguration`
        """
        output = self._api.websdk.Codesign.GetGlobalConfiguration.get()
        return output.global_configuration

    def set(
        self,
        global_configuration: GlobalConfiguration
    ):
        """
        Update global configuration settings for CodeSign Protect.

        Args:
            global_configuration: :class:`~.models.codesign.GlobalConfiguration`
        """
        self._api.websdk.Codesign.SetGlobalConfiguration.post(global_configuration=global_configuration)

    def set_values(
        self,
        approved_key_storage_locations: List[Literal['Software', 'HSM']] = None,
        available_key_storage_locations: List[Literal['Software', 'HSM']] = None,
        default_ca_container: str = None,
        default_certificate_container: str = None,
        default_credential_container: str = None,
        key_use_timeout: int = None,
        project_description_tooltip: str = None,
        request_in_progress_message: str = None,
    ):
        """
        Update specific value(s) on the existing global configuration settings for CodeSign Protect.

        Args:
            approved_key_storage_locations: Key storage locations that are approved for use with CodeSign Protect. This information is also available in the Encryption tree.
            available_key_storage_locations: Available key storage locations, such as HSM and Venafi key storage locations.
            default_ca_container: :ref:`dn` of container where CodeSign Protect creates and stores CA templates.
            default_certificate_container: The default :ref:`dn` of container that holds certificate objects.
            default_credential_container: The default :ref:`dn` of container that holds credentials.
            key_use_timeout: The number of seconds a client should wait for a response when attempting to use a key. The default is 120.
            project_description_tooltip: A description that appears when a project owner is creating a project.
            request_in_progress_message: The message that appears when a KeyUser attempts to access a key that requires approval.
        """

        global_configuration = self.get()
        if any(
                [
                    approved_key_storage_locations,
                    available_key_storage_locations,
                    default_ca_container,
                    default_certificate_container,
                    default_credential_container,
                    key_use_timeout,
                    project_description_tooltip,
                    request_in_progress_message,
                ]
        ):
            if approved_key_storage_locations:
                global_configuration.approved_key_storage_locations = Items(items=approved_key_storage_locations)
            if available_key_storage_locations:
                global_configuration.available_key_storage_locations = Items(items=available_key_storage_locations)
            if default_ca_container:
                global_configuration.default_ca_container = default_ca_container
            if default_certificate_container:
                global_configuration.default_certificate_container = default_certificate_container
            if default_credential_container:
                global_configuration.default_credential_container = default_credential_container
            if key_use_timeout is not None:
                global_configuration.key_use_timeout = key_use_timeout
            if project_description_tooltip:
                global_configuration.project_description_tooltip = project_description_tooltip
            if request_in_progress_message:
                global_configuration.request_in_progress_message = request_in_progress_message

            self._api.websdk.Codesign.SetGlobalConfiguration.post(global_configuration=global_configuration)
