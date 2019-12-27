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

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Folder, or Policy, object in TPP.

        Args:
            name: Name of the folder.
            parent_folder_dn: Absolute path to the folder's parent folder.
            attributes: Attributes pertaining to the folder itself and NOT any of the policyable options.
                In order to set engines on this folder, use :meth:`set_engines`. In order to set policyable
                options on the folder, use :meth:`lock_attributes`.

        Returns:
            Config object representing the folder.

        """
        if self.auth.preference == ApiPreferences.aperture:
            return self.auth.aperture.ConfigObjects.Policies.post(name=name, container=parent_folder_dn).object

        if self.auth.preference == ApiPreferences.websdk:
            return self._config_create(
                name=name,
                container=parent_folder_dn,
                config_class=ConfigClass.policy,
                attributes=attributes
            )

    def delete(self, folder_dn: str, recursive: bool = True):
        """
        Deletes the folder. The folder is, by default, deleted recursively. All objects deleted will be deleted from config
        and secret store.

        Args:
            folder_dn: Absolute path to the folder.
            recursive: If True, delete all sub-folders, etc., from config and secret store.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if recursive:
            # Must delete all of the secrets first.
            response = self.auth.websdk.Config.Enumerate.post(object_dn=folder_dn, recursive=True)
            result = response.result
            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

            all_child_dns = response.objects
            for child in all_child_dns:
                self._secret_store_delete_by_dn(object_dn=child.dn)

        self._config_delete(object_dn=folder_dn, recursive=recursive)

    def lock_attributes(self):
        pass

    def search(self, object_name_pattern: str, object_type: str = None, recursive: bool = True, starting_dn: str = None):
        """
        Searches for an object with the given object name pattern. The pattern is a regular expression. An object type
        can be supplied to specify the TPP object type, such as 'X509 Certificate'. If a starting DN is given without
        an object type, a search will be performed from the starting DN. This can improve the efficiency of this method.
        However, if both a starting DN and object type is provided, due to limitations of the WebSDK API, a search will
        be performed against the object type first, and then filtered by matches to the starting DN.

        If no objects are found, an empty list is returned.

        Examples:

            .. code-block:: python

                from venafi import Authenticate, Features

                auth = Authenticate(# params here)
                features = Features(auth)

                objects = features.folder.search(object_name_pattern='*some_object*.com', starting_dn='\\VED\\Policy\\Certificates')

        Args:
            object_name_pattern: A regular expression
            object_type: TPP Object Type (also called a Config Class)
            recursive: Search sub-folders when True
            starting_dn: Parent folder to all desired results

        Returns:
            A list of Config Objects representing the objects found.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if object_type:
            objects = self.auth.websdk.Config.EnumerateObjectsDerivedFrom.post(derived_from=object_type, pattern=object_name_pattern).objects
            if starting_dn:
                objects = [obj for obj in objects if starting_dn in obj.dn]
            return objects
        elif starting_dn:
            objects = self.auth.websdk.Config.Enumerate.post(object_dn=starting_dn, pattern=object_name_pattern, recursive=recursive).objects
        else:
            objects = self.auth.websdk.Config.EnumerateAll.post(pattern=object_name_pattern).objects

        return objects

    def set_engines(self, folder_guid: str, engine_guids: List[str], append_engines: bool = False):
        """
        Sets the desired TPP engine(s) to exclusively do work for all objects contained in the folder.

        Args:
            folder_guid: GUID of the folder.
            engine_guids: List of engine GUIDs listed in TPP.
            append_engines: If True, append `engine_guids` to the current list on the folder. Otherwise
                overwrite the current setting.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if append_engines:
            current_engines = self.auth.websdk.ProcessingEngines.Folder.Guid(folder_guid).get().engines
            engine_guids.extend([engine.engine_guid for engine in current_engines])
        result = self.auth.websdk.ProcessingEngines.Folder.Guid(folder_guid).put(engine_guids)
        result.assert_valid_response()
