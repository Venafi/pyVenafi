from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from enums.config import ConfigClass
from enums.secret_store import Namespaces


@feature()
class Folder(FeatureBase):
    def __init__(self, auth=None, name: str = None, container: str = None, attributes: list = None):
        if auth:
            super().__init__(auth)
        assert self.auth

        self.name = name
        self.container = container
        self.attributes = attributes

        self.absolute_guid = None
        self.dn = None
        self.guid = None
        self.config_id = None
        self.name = None
        self.parent = None
        self.revision = None
        self.type_name = None

    def __enter__(self):
        self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete(self.dn, recursive=True)

    def _load(self, policy_object):
        self.absolute_guid = policy_object.absolute_guid
        self.dn = policy_object.dn
        self.guid = policy_object.guid
        self.config_id = policy_object.config_id
        self.name = policy_object.name
        self.parent = policy_object.parent
        self.revision = policy_object.revision
        self.type_name = policy_object.type_name

    def create(self, name: str = None, container: str = None, attributes: dict = None):
        def throw_error():
            raise FeatureError.NoParameterProvided()

        name = name or self.name or throw_error()
        container = container or self.container or throw_error()
        attributes = attributes or self.attributes
        if attributes:
            attributes = [{'Name': key, 'Value': value} for key, value in attributes.items()]

        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.websdk:
            policy = self.auth.websdk.Config.Create.post(dn, ConfigClass.policy, attributes or [])
        elif self.auth.preference == ApiPreferences.aperture:
            policy = self.auth.aperture.ConfigObjects.Policies.post(name, container)
        else:
            raise FeatureError.InvalidAPIPreference(self.auth.preference)

        result = policy.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        self._load(policy.object)

    def delete(self, object_dn: str = None, recursive: bool = True):
        object_dn = object_dn or self.dn

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
        self.__init__()
