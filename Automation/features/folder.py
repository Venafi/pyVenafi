from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from enums.config import ConfigClass
from enums.secret_store import Namespaces


@feature()
class Folder(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, attributes: dict = None):
        if attributes:
            attributes = [{'Name': key, 'Value': value} for key, value in attributes.items()]

        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.websdk:
            policy = self.auth.websdk.Config.Create.post(dn, ConfigClass.policy, attributes or [])
        elif self.auth.preference == ApiPreferences.aperture:
            policy = self.auth.aperture.ConfigObjects.Policies.post(self.name, self.container)
        else:
            raise FeatureError.InvalidAPIPreference(self.auth.preference)

        result = policy.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return policy.object

    def delete(self, object_dn: str, recursive: bool = True):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if recursive:
            # Must delete all of the secrets first.
            all_child_dns = self.auth.websdk.Config.Enumerate.post(object_dn=object_dn, recursive=True).objects
            for child in all_child_dns:
                owners = self.auth.websdk.SecretStore.LookupByOwner.post(namespace=Namespaces.config, owner=child.dn).vault_ids
                for owner in owners:
                    self.auth.websdk.SecretStore.OwnerDelete.post(namespace=Namespaces.config, owner=owner)

        result = self.auth.websdk.Config.Delete.post(object_dn, recursive).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
