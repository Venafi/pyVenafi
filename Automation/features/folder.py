from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from enums.config import ConfigClass, FolderAttributes
from enums.secret_store import Namespaces


@feature()
class Folder(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, attributes: dict = None):
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
            all_child_dns = self.auth.websdk.Config.Enumerate.post(object_dn=object_dn, recursive=True).objects
            for child in all_child_dns:
                owners = self.auth.websdk.SecretStore.LookupByOwner.post(namespace=Namespaces.config, owner=child.dn).vault_ids
                for owner in owners:
                    result = self.auth.websdk.SecretStore.Delete.post(vault_id=owner).result
                    if result.code != 0:
                        raise FeatureError.InvalidResultCode(code=result.code, code_description=result.secret_store_result)

        result = self.auth.websdk.Config.Delete.post(object_dn, recursive).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
