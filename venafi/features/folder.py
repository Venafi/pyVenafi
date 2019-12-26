from typing import List
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.config import ConfigClass, FolderAttributes


@feature()
class Folder(FeatureBase):
    """
    This feature provides high-level interaction with TPP folders, also known as policies.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, attributes: dict = None):
        """
        Creates a Folder, or Policy, object in TPP.

        Args:
            name: Name of the folder.
            container: Absolute path to the folder's parent folder.
            attributes: Attributes pertaining to the folder itself and NOT any of the policyable options.
                In order to set engines on this folder, use :meth:`set_engines`.

        Returns:
            Config object representing the folder.

        """
        if self.auth.preference == ApiPreferences.aperture:
            return self.auth.aperture.ConfigObjects.Policies.post(name=name, container=container).object

        if self.auth.preference == ApiPreferences.websdk:
            return self._config_create(
                name=name,
                container=container,
                config_class=ConfigClass.policy,
                attributes=attributes
            )

    def delete(self, object_dn: str, recursive: bool = True):
        """
        Deletes the folder. The folder is, by default, deleted recursively. All objects deleted will be deleted from config
        and secret store.

        Args:
            object_dn: Absolute path to the folder.
            recursive: If True, delete all sub-folders, etc., from config and secret store.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if recursive:
            # Must delete all of the secrets first.
            response = self.auth.websdk.Config.Enumerate.post(object_dn=object_dn, recursive=True)
            result = response.result
            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

            all_child_dns = response.objects
            for child in all_child_dns:
                self._secret_store_delete_by_dn(object_dn=child.dn)

        self._config_delete(object_dn=object_dn, recursive=recursive)

    def set_engines(self, object_dn: str, engines: List[str]):
        """
        Sets the desired TPP engine(s) to exclusively do work for all objects contained in the folder.

        Args:
            object_dn: Absolute path to the folder.
            engines: List of engine names listed in TPP.
        """

        pass
