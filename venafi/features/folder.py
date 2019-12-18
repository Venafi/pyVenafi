"""
This feature allows you to create a folder, sometimes called a "policy", under \VED\Policy.
"""
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.config import ConfigClass, FolderAttributes


@feature()
class Folder(FeatureBase):
    """
    Folder details here.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, attributes: bool = None):
        """
        This is what this does....
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
