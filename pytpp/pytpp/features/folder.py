from typing import List, Union
from pytpp.vtypes import Config
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.properties.config import FolderClassNames, FolderAttributes


@feature()
class Folder(FeatureBase):
    """
    This feature provides high-level interaction with TPP folders, also known as policies.
    """
    def __init__(self, api):
        super().__init__(api)

    def apply_workflow(self, folder: 'Config.Object', workflow: 'Config.Object'):
        """
        Applies a workflow to a folder and all of its subordinate objects. However, a subordinate folder
        may block the workflow.

        Args:
            folder: Config object of the folder object.
            workflow: Config object of the workflow object.
        """
        result = self._api.websdk.Config.AddValue.post(
            object_dn=folder.dn,
            attribute_name=FolderAttributes.workflow,
            value=workflow.dn
        )

        result.assert_valid_response()

    def block_workflow(self, folder: 'Config.Object', workflow: 'Config.Object'):
        """
        Blocks a workflow on a folder and all of its subordinate objects. This prevents any parent folders from
        enforcing a workflow on this folder and its subordinate objects.

        Args:
            folder: Config object of the folder object.
            workflow: Config object of the workflow object.
        """
        result = self._api.websdk.Config.AddValue.post(
            object_dn=folder.dn,
            attribute_name=FolderAttributes.workflow_block,
            value=workflow.dn
        )

        result.assert_valid_response()

    def clear_policy(self, folder: 'Config.Object', class_name: str, attributes: Union[dict, List[str]]):
        """
        If ``attributes`` are not provided, clears the policy attribute name along with all of its values
        on a folder. If ``attributes`` are provided, then only the corresponding policy attribute values
        will be cleared. No error is thrown if the attribute value doesn't exist to begin with. If the
        same attribute name is defined in any ancestor folder, then this folder will inherit that setting.

        Examples:
        1. Clear all policy values by the given policy attribute names.

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames, \\
                    AttributeValues, Classes

                api = Authenticate(# params here)
                features = Features(api)

                folder = features.objects.get(object_dn='\\\VED\\\Policy\\\MyPolicy')
                features.folder.clear_all_policy_values(
                    folder=folder,
                    class_name=Classes.Certificate.x509_certificate,
                    attributes=[
                        AttributeNames.Certificate.management_type,
                        AttributeNames.Certificate.organization
                    ]
                )

        2. Clear only the specified values of the given policy attribute names.

        .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames, \\
                    AttributeValues, Classes

                api = Authenticate(# params here)
                features = Features(api)

                folder = features.objects.get(object_dn='\\\VED\\\Policy\\\MyPolicy')
                features.folder.clear_policy_value(
                    folder=folder,
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        AttributeNames.Certificate.organizational_unit: 'Venafi'
                    }
                )

        Args:
            folder: Config object of the folder object.
            class_name: TPP Class Name for the attributes being locked.
            attributes: Either a list of attribute names or a dictionary of attribute
                name/value pairs where the name is the attribute name and the value
                is the attribute value.
        """
        if isinstance(attributes, list):
            for attribute_name in attributes:
                result = self._api.websdk.Config.ClearPolicyAttribute.post(
                    object_dn=folder.dn,
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
                    result = self._api.websdk.Config.RemovePolicyValue.post(
                        object_dn=folder.dn,
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
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=FolderClassNames.policy,
            attributes=attributes
        )

    def delete(self, folder: 'Config.Object', recursive: bool = True):
        """
        Deletes the folder. The folder is, by default, deleted recursively. All objects deleted will be deleted from config
        and secret store.

        Args:
            folder: Config object of the folder.
            recursive: If True, delete all sub-folders, etc., from config and secret store.
        """
        if recursive:
            # Must delete all of the secrets first.
            response = self._api.websdk.Config.Enumerate.post(object_dn=folder.dn, recursive=True)
            result = response.result
            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

            all_child_dns = response.objects
            for child in all_child_dns:
                self._secret_store_delete(object_dn=child.dn)

        self._config_delete(object_dn=folder.dn, recursive=recursive)

    def delete_engines(self, folder: 'Config.Object'):
        """
        Deletes the desired TPP engine(s) that exclusively do work for all objects contained in the folder.

        Args:
            folder: Config object of the folder object.
        """
        return self._api.websdk.ProcessingEngines.Folder.Guid(folder.guid).delete()

    def get_engines(self, folder: 'Config.Object'):
        """
        Gets the desired TPP engine(s) that exclusively do work for all objects contained in the folder.

        Args:
            folder: Config object of the folder object.
        """
        return self._api.websdk.ProcessingEngines.Folder.Guid(folder.guid).get().engines

    def search(self, object_name_pattern: str = '*', object_types: List[str] = None, recursive: bool = True,
               starting_dn: str = None):
        """
        Searches for an object with the given object name pattern. The pattern is a regular expression. An object type
        can be supplied to specify the TPP object type, such as 'X509 Certificate'. If a starting DN is given without
        an object type, a search will be performed from the starting DN. This can improve the efficiency of this method.
        However, if both a starting DN and object type is provided, due to limitations of the WebSDK API, a search will
        be performed against the object type first, and then filtered by matches to the starting DN.

        If no objects are found, an empty list is returned.

        Examples:

            .. code-block:: python

                from pytpp import Authenticate, Features

                api = Authenticate(# params here)
                features = Features(api)

                objects = features.folder.search(
                    object_name_pattern='*some_object*.com',
                    starting_dn='\\\VED\\\Policy\\\Certificates'
                )

        Args:
            object_name_pattern: A regular expression
            object_types: List of TPP Object Types (also called a Config Classes)
            recursive: Search sub-folders when True
            starting_dn: Parent folder DN to begin search

        Returns:
            A list of Config Objects representing the objects found.
        """
        if object_types:
            objects = self._api.websdk.Config.FindObjectsOfClass.post(
                classes=object_types,
                pattern=object_name_pattern,
                object_dn=starting_dn,
                recursive=recursive
            ).objects
        elif starting_dn:
            objects = self._api.websdk.Config.Enumerate.post(
                object_dn=starting_dn,
                pattern=object_name_pattern,
                recursive=recursive
            ).objects
        else:
            objects = self._api.websdk.Config.EnumerateAll.post(
                pattern=object_name_pattern
            ).objects

        return objects

    def set_engines(self, folder: 'Config.Object', engines: 'List[Config.Object]', append_engines: bool = False):
        """
        Sets the desired TPP engine(s) to exclusively do work for all objects contained in the folder.

        Args:
            folder: Config object of the folder object.
            engines: List of engine config objects listed in TPP.
            append_engines: If True, append `engines` to the current list on the folder. Otherwise
                overwrite the current setting.
        """
        engine_guids = [e.guid for e in engines]
        if append_engines:
            current_engines = self._api.websdk.ProcessingEngines.Folder.Guid(folder.guid).get().engines
            engine_guids.extend([engine.engine_guid for engine in current_engines])
        result = self._api.websdk.ProcessingEngines.Folder.Guid(folder.guid).put(engine_guids=engine_guids)
        result.assert_valid_response()

    def read_policy(self, folder: 'Config.Object', class_name: str, attribute_name: str):
        """
        Reads policy settings for the given folder, class name, and attribute name. Returns List[List, bool] where the
        first element of the list is a list of values and the second element a boolean indicating whether or not the
        value(s) are locked on the policy. An empty list of values may be returned. In order to get engines on this
        folder, use :meth:`get_engines`.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames, \\
                    AttributeValues, Classes

                api = Authenticate(# params here)
                features = Features(api)

                folder = features.objects.get(object_dn='\\\VED\\\Policy\\\MyPolicy')
                values, locked = features.folder.read_policy(
                    folder=folder,
                    class_name=Classes.Certificate.x509_certificate,
                    attribute_name=AttributeNames.Certificate.management_type
                )

        Args:
            folder: Config object of the folder object.
            class_name: TPP Class Name for the attributes being locked.
            attribute_name: The attribute name.

        Returns:
            List[List, bool] where the first element of the list is a list of values and the second element a
            boolean indicating whether or not the value(s) are locked on the policy. An empty list of values may
            be returned.
        """
        resp = self._api.websdk.Config.ReadPolicy.post(
            object_dn=folder.dn,
            class_name=class_name,
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return [resp.values, resp.locked]

    def remove_workflow(self, folder: 'Config.Object', workflow: 'Config.Object'):
        """
        Removes an applied workflow from a folder.

        Args:
            folder: Config object of the folder object.
            workflow: Config object of the workflow object.
        """
        result = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=folder.dn,
            attribute_name=FolderAttributes.workflow,
            value=workflow.dn
        )

        result.assert_valid_response()

    def remove_blocked_workflow(self, folder: 'Config.Object', workflow: 'Config.Object'):
        """
        Removes a blocked workflow from a folder.

        Args:
            folder: Config object of the folder object.
            workflow: Config object of the workflow object.
        """
        result = self._api.websdk.Config.RemoveDnValue.post(
            object_dn=folder.dn,
            attribute_name=FolderAttributes.workflow_block,
            value=workflow.dn
        )

        result.assert_valid_response()

    def write_policy(self, folder: 'Config.Object', class_name: str, attributes: dict, locked: bool):
        """
        Sets policy configurations on a folder. If the value is locked, then all objects derived
        from the folder of the specified policy class will inherit the given attribute value and
        cannot be changed by any child folders or objects. Otherwise the value will be set as a
        default value.

        In order to set engines on this folder, use :meth:`set_engines`.

        In order to set custom field policies, use :meth:`pytpp.features.custom_fields.CustomField.write_policy`.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames, \\
                    AttributeValues, Classes

                api = Authenticate(# params here)
                features = Features(api)

                folder = features.objects.get(object_dn='\\\VED\\\Policy\\\MyPolicy')
                features.folder.write_policy(
                    folder=folder,
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        AttributeNames.Certificate.management_type: 'Enrollment',
                        AttributeNames.Certificate.organization: 'Venafi'
                    },
                    locked=True
                )

        Args:
            folder: Config object of the folder object.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        for name, values in attributes.items():
            if not isinstance(values, list):
                values = [values]

            result = self._api.websdk.Config.WritePolicy.post(
                object_dn=folder.dn,
                class_name=class_name,
                attribute_name=name,
                values=values,
                locked=locked
            ).result

            if result.code != 1:
                FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

    def update_policy(self, folder: 'Config.Object', class_name: str, attributes: dict, locked: bool):
        """
        Updates policy configurations on a folder. If the value is locked, then all objects derived
        from the folder of the specified policy class will inherit the given attribute value and
        cannot be changed by any child folders or objects. Otherwise the value will be set as a
        default value.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames, \\
                    AttributeValues, Classes

                api = Authenticate(# params here)
                features = Features(api)

                folder = features.objects.get(object_dn='\\\VED\\\Policy\\\MyPolicy')
                features.folder.update_policy(
                    folder=folder
                    class_name=Classes.Certificate.x509_certificate,
                    attributes={
                        AttributeNames.Certificate.management_type: 'Enrollment',
                        AttributeNames.Certificate.organization: 'Venafi'
                    },
                    locked=True
                )

        Args:
            folder: Config object of the folder object.
            class_name: TPP Class Name for the attributes being locked.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
            locked: Enforces the policy on all subordinate folders and objects.
        """
        for name, value in attributes.items():
            result = self._api.websdk.Config.AddPolicyValue.post(
                object_dn=folder.dn,
                class_name=class_name,
                attribute_name=name,
                value=value,
                locked=locked,
            ).result

            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
