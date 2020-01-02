from typing import List, Union
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.config import FolderClassNames, FolderAttributes


@feature()
class Folder(FeatureBase):
    """
    This feature provides high-level interaction with TPP folders, also known as policies.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def clear_policy(self, folder_dn: str, class_name: str, attributes: Union[dict, List[str]]):
        """
        If ``attributes`` are not provided, clears the policy attribute name along with all of its values
        on a folder. If ``attributes`` are provided, then only the corresponding policy attribute values
        will be cleared. No error is thrown if the attribute value doesn't exist to begin with. If the
        same attribute name is defined in any ancestor folder, then this folder will inherit that setting.

        Examples:
        1. Clear all policy values by the given policy attribute names.

            .. code-block:: python

                from venafi import logger, Authenticate, Features, Attributes, \\
                    AttributeValues, Classes

                auth = Authenticate(# params here)
                features = Features(auth)

                features.folder.clear_all_policy_values(
                    folder_dn='\\\VED\\\Policy\\\MyPolicy',
                    class_name=Classes.Certificate.x509_certificate,
                    attributes=[
                        Attributes.Certificate.management_type,
                        Attributes.Certificate.organization
                    ]
                )

        2. Clear only the specified values of the given policy attribute names.

        .. code-block:: python

                from venafi import logger, Authenticate, Features, Attributes, \\
                    AttributeValues, Classes

                auth = Authenticate(# params here)
                features = Features(auth)

                features.folder.clear_policy_value(
                    folder_dn='\\\VED\\\Policy\\\MyPolicy',
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        Attributes.Certificate.organizational_unit: 'Venafi'
                    }
                )

        Args:
            folder_dn: Absolute path to the folder enforcing the policy.
            class_name: TPP Class Name for the attributes being locked.
            attributes: Either a list of attribute names or a dictionary of attribute
                name/value pairs where the name is the attribute name and the value
                is the attribute value.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        if isinstance(attributes, list):
            for attribute_name in attributes:
                result = self.auth.websdk.Config.ClearPolicyAttribute.post(
                    object_dn=folder_dn,
                    attribute_name=attribute_name,
                    class_name=class_name
                ).result

                if result.code != 1:
                    raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        elif isinstance(attributes, dict):
            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                for value in values:
                    result = self.auth.websdk.Config.RemovePolicyValue.post(
                        object_dn=folder_dn,
                        class_name=class_name,
                        attribute_name=name,
                        value=value
                    ).result

                    if result.code != 1:
                        raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
        else:
            raise TypeError(f'Expected attributes to be of type List[str] or Dict, but got {type(attributes)} instead.')

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Folder, or Policy, object in TPP.

        Args:
            name: Name of the folder.
            parent_folder_dn: Absolute path to the folder's parent folder.
            attributes: Attributes pertaining to the folder itself and NOT any of the policyable options.
                In order to set engines on this folder, use :meth:`set_engines`. In order to set policyable
                options on the folder, use :meth:`write_policy`.

        Returns:
            Config object representing the folder.

        """
        if self.auth.preference == ApiPreferences.aperture:
            return self.auth.aperture.ConfigObjects.Policies.post(name=name, container=parent_folder_dn).object

        if self.auth.preference == ApiPreferences.websdk:
            return self._config_create(
                name=name,
                parent_folder_dn=parent_folder_dn,
                config_class=FolderClassNames.policy,
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
                self._secret_store_delete(object_dn=child.dn)

        self._config_delete(object_dn=folder_dn, recursive=recursive)

    def delete_engines(self, folder_guid: str):
        """
        Deletes the desired TPP engine(s) that exclusively do work for all objects contained in the folder.

        Args:
            folder_guid: GUID of the folder.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self.auth.websdk.ProcessingEngines.Folder.Guid(folder_guid).delete()

    def get_engines(self, folder_guid: str):
        """
        Gets the desired TPP engine(s) that exclusively do work for all objects contained in the folder.

        Args:
            folder_guid: GUID of the folder.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        return self.auth.websdk.ProcessingEngines.Folder.Guid(folder_guid).get().engines

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

                objects = features.folder.search(object_name_pattern='*some_object*.com', starting_dn='\\\VED\\\Policy\\\Certificates')

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

    def read_policy(self, folder_dn: str, class_name: str, attribute_name: str):
        """
        Reads policy settings for the given folder, class name, and attribute name. Returns List[List, bool] where the
        first element of the list is a list of values and the second element a boolean indicating whether or not the
        value(s) are locked on the policy. An empty list of values may be returned. In order to get engines on this
        folder, use :meth:`get_engines`.

        Examples:

            .. code-block:: python

                from venafi import logger, Authenticate, Features, Attributes, \\
                    AttributeValues, Classes

                auth = Authenticate(# params here)
                features = Features(auth)

                values, locked = features.folder.read_policy(
                    folder_dn='\\\VED\\\Policy\\\MyPolicy',
                    class_name=Classes.Certificate.x509_certificate,
                    attribute_name=Attributes.Certificate.management_type
                )

        Args:
            folder_dn: Absolute path to the folder enforcing the policy.
            class_name: TPP Class Name for the attributes being locked.
            attribute_name: The attribute name.

        Returns:
            List[List, bool] where the first element of the list is a list of values and the second element a
            boolean indicating whether or not the value(s) are locked on the policy. An empty list of values may
            be returned.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        resp = self.auth.websdk.Config.ReadPolicy.post(
            object_dn=folder_dn,
            class_name=class_name,
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return [resp.values, resp.locked]

    def write_policy(self, folder_dn: str, class_name: str, attributes: dict, locked: bool):
        """
        Sets policy configurations on a folder. If the value is locked, then all objects derived
        from the folder of the specified policy class will inherit the given attribute value and
        cannot be changed by any child folders or objects. Otherwise the value will be set as a
        suggested value that appears as a default value in any of the Venafi websites. In order
        to set engines on this folder, use :meth:`set_engines`.

        Examples:

            .. code-block:: python

                from venafi import logger, Authenticate, Features, Attributes, \\
                    AttributeValues, Classes

                auth = Authenticate(# params here)
                features = Features(auth)

                features.folder.add_policy(
                    folder_dn='\\\VED\\\Policy\\\MyPolicy',
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        Attributes.Certificate.management_type: 'Enrollment',
                        Attributes.Certificate.organization: 'Venafi'
                    },
                    locked=True
                )

        Args:
            folder_dn: Absolute path to the folder enforcing the policy.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        for name, values in attributes.items():
            if not isinstance(values, list):
                values = [values]

            result = self.auth.websdk.Config.WritePolicy.post(
                object_dn=folder_dn,
                class_name=class_name,
                attribute_name=name,
                values=values,
                locked=locked
            ).result

            if result.code != 1:
                FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

    def update_policy(self, folder_dn: str, class_name: str, attributes: dict, locked: bool):
        """
        Updates policy configurations on a folder. If the value is locked, then all objects derived
        from the folder of the specified policy class will inherit the given attribute value and
        cannot be changed by any child folders or objects. Otherwise the value will be set as a
        suggested value that appears as a default value in any of the Venafi websites.

        Examples:

            .. code-block:: python

                from venafi import logger, Authenticate, Features, Attributes, \\
                    AttributeValues, Classes

                auth = Authenticate(# params here)
                features = Features(auth)

                features.folder.add_policy(
                    folder_dn='\\\VED\\\Policy\\\MyPolicy',
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        Attributes.Certificate.management_type: 'Enrollment',
                        Attributes.Certificate.organization: 'Venafi'
                    },
                    locked=True
                )

        Args:
            folder_dn: Absolute path to the folder enforcing the policy.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        for name, value in attributes.items():
            result = self.auth.websdk.Config.AddPolicyValue.post(
                object_dn=folder_dn,
                class_name=class_name,
                attribute_name=name,
                value=value,
                locked=locked,
            ).result

            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
