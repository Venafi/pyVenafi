from typing import List, Union
from pytpp.vtypes import Config
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
from pytpp.properties.response_objects.config import Config


class _AttributeValue:
    def __init__(self, values: List[str], locked: bool):
        self.values = values
        self.locked = locked


@feature()
class Objects(FeatureBase):
    """
    This feature provides access to read, write, update, clear, and retrieve config objects and their attributes.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def clear(self, obj: 'Config.Object', attributes: Union[dict, List[str]]):
        """
        If ``attributes`` are not provided, clears the DN attribute name along with all of its values.
        If ``attributes`` are provided, then only the corresponding policy attribute values
        will be cleared. No error is thrown if the attribute value doesn't exist to begin with. If the
        same attribute name is defined in any ancestor folder, then this folder will inherit that setting.

        Examples:
        1. Clear all policy values by the given policy attribute names.

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                # Clear all values pertaining to Certificate Management Type and
                # Certificate Organization.
                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                features.objects.clear(
                    obj=obj,
                    attributes=[
                        AttributeNames.Certificate.management_type,
                        AttributeNames.Certificate.organization
                    ]
                )

        2. Clear only the specified values of the given policy attribute names.

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                # Clear all values pertaining to Certificate Organizational Unit only where
                # the value equals "Venafi".
                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                features.objects.clear(
                    obj=obj,
                    attributes={
                        AttributeNames.Certificate.organizational_unit: 'Venafi'
                    }
                )

        Args:
            obj: Config object of the TPP Object.
            attributes: Either a list of attribute names or a dictionary of attribute
                name/value pairs where the name is the attribute name and the value
                is the attribute value.
        """
        if isinstance(attributes, list):
            for attribute_name in attributes:
                result = self._api.websdk.Config.ClearAttribute.post(
                    object_dn=obj.dn,
                    attribute_name=attribute_name
                ).result

                if result.code != 1:
                    raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        elif isinstance(attributes, dict):
            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                for value in values:
                    result = self._api.websdk.Config.RemoveDnValue.post(
                        object_dn=obj.dn,
                        attribute_name=name,
                        value=value
                    ).result

                    if result.code != 1:
                        raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
        else:
            raise TypeError(f'Expected attributes to be of type "list[str]" or "dict", but got {type(attributes)} instead.')

    def find_policy(self, obj: 'Config.Object', class_name: str, attribute_name: str):
        """
        Returns the folder that suggests or locks a particular attribute value to the specified object.
        A tuple of 3 elements is returned where the first element is the absolute path to the folder that
        specifies the attribute values, the attribute values, and whether those values are locked or not.

        Args:
            obj: Config object of the TPP Object.
            class_name: TPP Class Name of TPP Object.
            attribute_name: Name of the attribute.

        Returns:
            A tuple of 3 elements:
            1. Policy DN: the absolute path to the folder that suggests or locks a particular attribute.
            2. Attribute Values: A list of all values corresponding to the given attribute name.
            3. Locked: A boolean representing whether or not the returned values are locked.
        """
        resp = self._api.websdk.Config.FindPolicy.post(
            object_dn=obj.dn,
            class_name=class_name,
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        class Policy:
            policy_dn = resp.policy_dn
            values = resp.values
            locked = resp.locked

        return Policy()

    def get(self, object_dn: str = None, object_guid: str = None, raise_error_if_not_exists: bool = False):
        """
        Converts an Object DN or Object GUID into a Config Object and returns it. Only
        one of the parameters is required.

        Args:
            object_dn: Absolute path to the object.
            object_guid: GUID of the object.
            raise_error_if_not_exists: If ``True``, an empty Config Object is returned where each property
                is ``None``.

        Returns:
            Config Object
        """
        if not (object_dn or object_guid):
            raise ValueError(
                'Must supply either an Object DN or Object GUID, but neither was provided.'
            )
        obj = self._api.websdk.Config.IsValid.post(object_dn=object_dn, object_guid=object_guid)
        if obj.result.code == 400 and not raise_error_if_not_exists:
            # The object doesn't exist, but just return an empty object.
            return Config.Object(response_object={})
        return obj.object

    def read(self, obj: 'Config.Object', attribute_name: str, include_policy_values: bool = False, timeout: int = 10):
        """
        Reads attributes on the given TPP Object and attribute name. Returns List[List, bool] where the
        first element of the list is a list of values and the second element a boolean indicating whether
        or not the value(s) are locked on the policy. An empty list of values may be returned.

        Note that the values returned are the `effective` values for the given attribute name, meaning that
        the policy values enforced by the object's ancestor folders that effectively override any setting
        on the object are taken into account. If the goal is to read the attribute values for an attribute
        without any regard to policy rules, do this:

        .. code-block:: python

            from pytpp import logger, Authenticate, AttributeNames

            api = Authenticate(# params here)

            resp = api.websdk.Config.ReadDn.post(
                object_dn='\\VED\\Policy\\MyPolicy\\MyCert',
                attribute_name=AttributeNames.Certificate.management_type
            )

            values, locked = resp.values, resp.locked

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                values, locked = features.objects.read(
                    obj=obj,
                    attribute_name=AttributeNames.Certificate.management_type
                )

        Args:
            obj: Config object of the TPP Object.
            attribute_name: The attribute name.
            include_policy_values: If ``True``, the effective value(s) are returned.
                Otherwise only values assigned to the DN explicitly are returned.
            timeout: Read timeout in seconds.

        Returns:
            List[List, bool] where the first element of the list is a list of values and the second element a
            boolean indicating whether or not the value(s) are locked on the policy. An empty list of values may
            be returned.
        """
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                result, attr = self._read(
                    obj=obj,
                    attribute_name=attribute_name,
                    include_policy_values=include_policy_values
                )
                if result.code != 1:
                    continue
                if attr and attr.values:
                    return attr

        FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
        raise TimeoutError(f'Could not read {attribute_name} on {obj.dn} because it did not exist '
                           f'after {timeout} seconds.')

    def read_all(self, obj: 'Config.Object'):
        """
        Reads all attributes on the given TPP Object.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                values, locked = features.folder.read_all(obj=obj)

        Args:
            obj: Config object of the TPP Object.

        Returns:
            A list of NameValue objects having ``name`` and ``values`` properties corresponding to each
            attribute name and attribute value.
        """
        resp = self._api.websdk.Config.ReadAll.post(object_dn=obj.dn)

        result = resp.result
        if result.code != 1:
            FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return resp.name_values

    def rename(self, obj: 'Config.Object', new_object_dn: str):
        """
        Renames an object DN. This method requires two absolute paths, the old one and the new one. This
        method also effectively moves objects from one folder to another.

        Args:
            obj: Config object of the TPP Object.
            new_object_dn: Absolute path to the new object location.
        """
        if not new_object_dn.startswith('\\VED'):
            raise FeatureError.InvalidFormat(f'"{new_object_dn}" must be an absolute path starting from \\VED.')

        response = self._api.websdk.Config.RenameObject.post(object_dn=obj.dn, new_object_dn=new_object_dn)
        result = response.result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return self.get(object_dn=new_object_dn, raise_error_if_not_exists=True)

    def update(self, obj: 'Config.Object', attributes: dict):
        """
        Updates attributes on an object. If the attribute is locked TPP will simply ignore the request. To avoid
        any confusion, it would be wise to consider validating the policy settings to ensure the desired attribute
        is not already locked. To do so, use :meth:`pytpp.features.folder.Folder.read_policy`.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                features.objects.update(
                    obj=obj,
                    attributes={
                        AttributeNames.Certificate.organizational_unit: 'Engineering'
                    }
                )

        Args:
            obj: Config object of the TPP Object.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
        """
        for name, value in attributes.items():
            result = self._api.websdk.Config.AddValue.post(
                object_dn=obj.dn,
                attribute_name=name,
                value=value,
            ).result

            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def wait_for(self, obj: 'Config.Object', attribute_name: str, attribute_value: str, include_policy_values: bool = False,
                 timeout: int = 10):
        """
        Waits for the ``attribute_name`` to have the ``attribute_value`` on the object_dn for the timeout period. A
        TimeoutError is thrown if the ``attribute_name`` does not have the ``attribute_value``.

        Args:
            obj: Config object of the TPP Object.
            attribute_name: The name of the attribute.
            attribute_value: The expected value to the ``attribute_name``.
            include_policy_values: If ``True``, the effective value(s) are returned.
                Otherwise only values assigned to the DN explicitly are returned.
            timeout: Timeout period in seconds.

        Returns:
            Values of the given ``attribute_name`` for the given ``object_dn``.
        """

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                result, attr = self._read(
                    obj=obj,
                    attribute_name=attribute_name,
                    include_policy_values=include_policy_values
                )
                if result.code != 1:
                    continue
                if attr and any([True for value in attr.values if str(value).lower() == attribute_value.lower()]):
                    return attr

        FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()
        raise FeatureError.TimeoutError(method=self.wait_for, expected_value=attribute_value,
                                        actual_value=attr.values, timeout=timeout)

    def write(self, obj: 'Config.Object', attributes: dict):
        """
        Writes new attributes on an object. If the attribute is locked TPP will simply ignore the request. To avoid
        any confusion, it would be wise to consider validating the policy settings to ensure the desired attribute
        is not already locked. To do so, use :meth:`pytpp.features.folder.Folder.read_policy`.

        Examples:

            .. code-block:: python

                from pytpp import logger, Authenticate, Features, AttributeNames

                api = Authenticate(# params here)
                features = Features(api)

                obj = features.objects.get('\\VED\\Policy\\MyPolicy\\MyCert')
                features.objects.write(
                    obj=obj,
                    attributes={
                        AttributeNames.Certificate.organizational_unit: 'Engineering'
                    }
                )

        Args:
            obj: Config object of the TPP Object.
            attributes: A dictionary of attribute name/value pairs where the name is the
                attribute name and the value is the attribute value.
        """
        attributes = {k: ([v] if not isinstance(v, list) else v) for k, v in attributes.items()}

        result = self._api.websdk.Config.Write.post(
            object_dn=obj.dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def _read(self, obj: 'Config.Object', attribute_name: str, include_policy_values: bool):
        if include_policy_values is True:
            resp = self._api.websdk.Config.ReadEffectivePolicy.post(
                object_dn=obj.dn,
                attribute_name=attribute_name
            )
            return resp.result, _AttributeValue(values=resp.values, locked=resp.locked)
        else:
            resp = self._api.websdk.Config.Read.post(
                object_dn=obj.dn,
                attribute_name=attribute_name
            )
            return resp.result, _AttributeValue(values=resp.values, locked=False)
