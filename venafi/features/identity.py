from typing import List
from venafi.properties.config import IdentityClassNames, IdentityAttributes, IdentityAttributeValues
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.rights import SubSystemTypes


class _IdentityBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self._identity_dn = r'\VED\Identity'

    def allow_aperture_user_search(self, prefixed_universal: str):
        result = self._auth.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal,
            rights_value='Impersonate'
        )
        result.assert_valid_response()

    def add_master_admin(self, prefixed_universal: str):
        ved_guid = self._auth.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid, 'AllPrivileges'],
            [SubSystemTypes.secret_store_config, ved_guid, '*127'],
            [SubSystemTypes.client, '', 'AllPrivileges'],
            [SubSystemTypes.rights, '', 'Supervisor'],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            result = self._auth.websdk.Rights.Add.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal,
                rights_value=rights_value
            )
            result.assert_valid_response()

    def allow_websdk_access(self, prefixed_universal: str):
        result = self._auth.websdk.Rights.Add.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal,
            rights_value='Allowed'
        )
        result.assert_valid_response()

    def find_group(self, name: str, limit: int = 100, is_distribution_group: bool = False):
        identity_type = IdentityAttributes.Types.security_group if not is_distribution_group else IdentityAttributes.Types.distribution_group
        result = self._auth.websdk.Identity.Browse.post(
            filter=name,
            limit=limit,
            identity_type=identity_type
        )
        return result.identities

    def find_user(self, name: str, limit: int = 100):
        result = self._auth.websdk.Identity.Browse.post(
            filter=name,
            limit=limit,
            identity_type=IdentityClassNames.user
        )
        return result.identities

    def exists(self, prefixed_name: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        )
        response.assert_valid_response()
        if response.json_response.content:
            return response.identity.prefixed_name == prefixed_name
        return False

    def get_memberships(self, prefixed_name: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        memberships = self._auth.websdk.Identity.GetMemberships.post(
            identity=self._identity_dict(prefixed_name=prefixed_name)
        ).identities

        return memberships

    def get_rights(self, prefixed_universal: str):
        return self._auth.websdk.Rights.Get.post(universal_id=prefixed_universal)

    def read_attribute(self, prefixed_name: str, attribute_name: str):
        result = self._auth.websdk.Identity.ReadAttribute.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            attribute_name=attribute_name
        )
        return result.attributes

    def remove_aperture_user_search(self, prefixed_universal: str):
        result = self._auth.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.aperture,
            rights_object='local',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()

    def remove_master_admin(self, prefixed_universal: str):
        ved_guid = self._auth.websdk.Config.DnToGuid.post(object_dn='\\VED').guid

        admin_rights = [
            [SubSystemTypes.config, ved_guid],
            [SubSystemTypes.secret_store_config, ved_guid],
            [SubSystemTypes.client, ''],
            [SubSystemTypes.rights, ''],
        ]
        for rights in admin_rights:
            subsystem, rights_object, rights_value = rights
            result = self._auth.websdk.Rights.Remove.post(
                subsystem=subsystem,
                rights_object=rights_object,
                universal_id=prefixed_universal
            )
            result.assert_valid_response()

    def remove_websdk_access(self, prefixed_universal: str):
        result = self._auth.websdk.Rights.Remove.post(
            subsystem=SubSystemTypes.websdk,
            rights_object='Sessions',
            universal_id=prefixed_universal
        )
        result.assert_valid_response()

    def validate(self, prefixed_name: str = None, prefixed_universal: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        identity = self._auth.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name, prefixed_universal=prefixed_universal)
        ).identity

        return identity

    @staticmethod
    def _identity_dict(prefixed_name: str = None, prefixed_universal: str = None):
        d = {}
        if prefixed_name:
            d.update({'PrefixedName': prefixed_name})
        if prefixed_universal:
            d.update({'PrefixedUniversal': prefixed_universal})
        return d


@feature()
class User(_IdentityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, password: str, email_address: str, add_master_admin: bool = False,
               allow_aperture_user_search: bool = False, allow_websdk_access: bool = False,
               add_to_everyone_group: bool = True):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        attributes = {
            'Internet Email Address': email_address
        }
        user = self._config_create(
            name=name,
            parent_folder_dn=self._identity_dn,
            config_class=IdentityClassNames.user,
            attributes=attributes,
        )
        user = self.validate(prefixed_name=f'local:{user.name}')
        self.set_password(prefixed_name=user.prefixed_name, new_password=password)

        if add_to_everyone_group:
            everyone_group = self.validate(prefixed_name='local:Everyone')
            response = self._auth.websdk.Identity.AddGroupMembers.put(
                group=self._identity_dict(prefixed_name=everyone_group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            response.assert_valid_response()

        if add_master_admin:
            self.add_master_admin(prefixed_universal=user.prefixed_universal)

        if allow_aperture_user_search:
            self.allow_aperture_user_search(prefixed_universal=user.prefixed_universal)

        if allow_websdk_access:
            self.allow_websdk_access(prefixed_universal=user.prefixed_universal)

        return user

    def delete(self, prefixed_name: str):
        user = self.validate(prefixed_name=prefixed_name)

        groups = self.get_memberships(prefixed_name=user.prefixed_name)
        for group in groups:
            result = self._auth.websdk.Identity.RemoveGroupMembers.put(
                group=self._identity_dict(prefixed_name=group.prefixed_name),
                members=[self._identity_dict(prefixed_name=user.prefixed_name)]
            )
            result.assert_valid_response()

        result = self._auth.websdk.Rights.Remove.post(
            universal_id=user.prefixed_universal
        )
        result.assert_valid_response()

        self._config_delete(object_dn=f'{self._identity_dn}\\{user.name}')

    def set_password(self, prefixed_name: str, new_password: str, old_password: str = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        response = self._auth.websdk.Identity.SetPassword.post(
            identity=self._identity_dict(prefixed_name=prefixed_name),
            old_password=old_password,
            password=new_password
        )
        return response.identity


@feature()
class Group(_IdentityBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self):
        pass

    def delete(self):
        pass

    def rename(self):
        pass

    def add_members(self):
        pass

    def remove_members(self, group_prefixed_name: str, member_prefixed_names: List[str]):
        result = self._auth.websdk.Identity.RemoveGroupMembers.put(
            group=self._identity_dict(prefixed_universal=group_prefixed_name),
            members=[
                self._identity_dict(prefixed_universal=member_prefixed_name)
                for member_prefixed_name in member_prefixed_names
            ]
        )
        result.assert_valid_response()

    def get_members(self):
        pass
