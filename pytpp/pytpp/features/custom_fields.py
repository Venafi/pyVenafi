from typing import List, Dict, Union
from pytpp.vtypes import Config
from pytpp.properties.config import CustomFieldAttributes, CustomFieldAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature


@feature()
class CustomField(FeatureBase):
    """
    This feature provides high-level interaction with TPP Custom Field objects.
    """

    def __init__(self, api):
        super().__init__(api)
        self._metadata_root_dn = r'\VED\Metadata Root'

    @staticmethod
    def _guid_data_list(guid_data_dict: dict):
        return [
            {"ItemGuid": key, "List": value}
            for key, value in guid_data_dict.items()
        ]

    @staticmethod
    def _validate_result_code(result):
        if result.code != 0:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.metadata_result)

    def create(self, label: str, name: str, classes: list, data_type: int, allowed_characters: List[str] = None,
               allowed_values: List[str] = None, category: str = None, date_only: bool = None, default_values: List = None,
               display_after: str = None, error_message: str = None, help_text: str = None, localization_table: str = None,
               localized_help: Union[List[str], Dict] = None, localized_label: str = None, localized_set: str = None,
               mandatory: bool = None, mask: str = None, maximum_length: int = None, minimum_length: int = None,
               policyable: bool = None, regular_expression: str = None, render_hidden: bool = None,
               render_read_only: bool = None, single: bool = None, time_only: bool = None
               ):
        """
        Creates a Custom Field (or Metadata Item). Custom fields appear in the UI unless ``render_hidden = True``. If
        the custom field should be implemented on a folder policy, then set ``policyable=True``, otherwise the custom
        field cannot be enforced on a policy, but will instead apply to all objects that belong to one of the ``classes``.
        If it is configured to be policyable, the ``classes`` still apply. For example, if one of the classes is set to
        "X509 Certificate", then all objects that are a "X509 Certificate" will inherit the custom field. If it is set
        to be policyable and is locked to a specific value, only "X509 Certificate" objects under the policy folder
        will have that value locked.

        The field ``data_types`` are stored in AttributeValues.

        Examples:
            .. code-block::python

                from pytpp import Authenticate, Features, AttributeValues, Classes

                api = Authenticate(...)
                features = Features(api)

                custom_field = features.custom_fields.create(
                    label='What do you think about custom fields?',
                    name='My Fancy Custom Field',
                    classes=[
                        Classes.Certificate.x509_certificate
                    ],
                    data_type=AttributeValues.CustomField.Type.list,
                    mandatory=False,
                    allowed_values=[
                        'Cool',
                        'Needs Improvement',
                        'Dumb',
                    ],
                    error_message="Something ain't right...',
                    single=False,  # Multiple selection enabled.
                    policyable=True  # Set to True to enable locking values on policy folders.
                )

        Args:
            label: The label text for the custom field.
            name: The name of the custom field object.
            classes: The classes that this field applies to.
            data_type: The field type as an integer.
            allowed_characters: A set of allowable alphabetic, numeric, or symbols.
            allowed_values: An array of allowable values.
            category: Absolute path to the item category.
            date_only: If ``True``, a calendar date is required.
            default_values: List of default values.
            display_after: Appears after a list of Custom Field values.
            error_message: The error message when an error is encountered.
            help_text: The tool tip for the UI.
            localization_table: A list or dictionary of strings from another language.
            localized_help: The localized help text that describes the Metadata Custom Field.
            localized_label: A localized label text describing the Metadata Custom Field.
            localized_set: A list of localization settings.
            mandatory: If ``True``, this field is required.
            mask: The set of characters to use to hide user input in the UI.
            maximum_length: Maximum number of allowed characters.
            minimum_length: Minimum number of allowed characters.
            policyable: If ``True``, the custom field can be enforced on a policy folder.
            regular_expression: The regular expression to control user input.
            render_hidden: If ``True``, hides the field from the UI.
            render_read_only: If ``False``, the user can change the default values (if not locked by policy).
            single: If ``False``, the user can select/input multiple items.
            time_only: If ``True``, time of day is required.

        Returns:
            Metadata Item object.

        """
        item = {
            'AllowedCharacters': allowed_characters,
            'AllowedValues': allowed_values,
            'Category': category,
            'Classes': classes,
            'DateOnly': date_only,
            'DefaultValues': default_values,
            'DisplayAfter': display_after,
            'ErrorMessage': error_message,
            'Help': help_text,
            'Label': label,
            'LocalizationTable': localization_table,
            'LocalizedHelp': localized_help,
            'LocalizedLabel': localized_label,
            'LocalizedSet': localized_set,
            'Mandatory': mandatory,
            'Name': name,
            'Mask': mask,
            'MaximumLength': maximum_length,
            'MinimumLength': minimum_length,
            'Policyable': policyable,
            'RegularExpression': regular_expression,
            'RenderHidden': render_hidden,
            'RenderReadOnly': render_read_only,
            'Single': single,
            'TimeOnly': time_only,
            'Type': data_type
        }

        response = self._api.websdk.Metadata.DefineItem.post(item=item)
        self._validate_result_code(response.result)
        return response.item

    def delete(self, custom_field: 'Config.Object', remove_data: bool = True):
        """
        Deletes a custom field and all instances of it, including policy settings. If ``remove_data = False``, then
        an exception will be raised if there is existing data for the custom field on any object.

        Args:
            custom_field: Config object of the custom field
            remove_data: If ``True``, then deletes the custom field regardless of data existing on the custom field
                on any object that implements it.
        """
        response = self._api.websdk.Metadata.UndefineItem.post(
            item_guid=custom_field.guid,
            remove_data=remove_data
        )
        self._validate_result_code(response.result)

    def get(self, name: str = None):
        """
        Fetches the config object a custom field object.

        Args:
            name: The name of the custom field object.

        Returns:
            Config object of the custom field.
        """
        response = self._api.websdk.Config.IsValid.post(
            object_dn=f'{self._metadata_root_dn}\\{name}'
        )
        return response.object

    def get_item_details(self, custom_field: 'Config.Object' = None):
        """
        Fetches the item details of a custom field object according to the data
        returned by the WebSDK API "POST Metadata/LoadItem".

        Args:
            custom_field: The name of the custom field object.

        Returns:
            Metadata Item object.
        """
        response = self._api.websdk.Metadata.LoadItem.post(dn=custom_field.dn)
        self._validate_result_code(result=response.result)
        return response.item

    def list(self):
        """
        Lists all custom fields registered in TPP.

        Returns:
            List of Metadata Item objects.
        """
        response = self._api.websdk.Metadata.Items.get()
        self._validate_result_code(response.result)
        return response.items

    def read(self, obj: 'Config.Object', custom_field: 'Config.Object'):
        """
        Reads the actual value(s) of a custom field, accounting for policy settings. Value(s) may be None.

        Args:
            obj: Config object of the object having the custom field.
            custom_field: Config object of the custom field.

        Returns:
            EffectiveValues object:
                * locked: Boolean. If ``True``, the ``values`` are locked by the policy.
                * policy_dn: Absolute path to the policy locking the values.
                * values: List of values.
        """
        response = self._api.websdk.Metadata.ReadEffectiveValues.post(
            dn=obj.dn,
            item_guid=custom_field.guid
        )
        self._validate_result_code(response.result)

        class EffectiveValues:
            def __init__(self):
                self.locked = response.locked
                self.policy_dn = response.policy_dn
                self.values = response.values

        return EffectiveValues()

    def read_policy(self, folder: 'Config.Object', custom_field: 'Config.Object', class_name: str):
        """
        Reads the policy value(s) of a custom field, accounting for policy settings. Value(s) may be None.

        Args:
            folder: Config object of the folder.
            custom_field: Config object of the custom field object.
            class_name: Object class.

        Returns:
            EffectiveValues object:
                * locked: Boolean. If ``True``, the ``values`` are locked by the policy.
                * values: List of values.
        """
        response = self._api.websdk.Metadata.ReadPolicy.post(
            dn=folder.dn,
            item_guid=custom_field.guid,
            obj_type=class_name
        )
        self._validate_result_code(response.result)

        class PolicyValues:
            def __init__(self):
                self.locked = response.locked
                self.values = response.values

        return PolicyValues()

    def update(self, custom_field: 'Config.Object', allowed_characters: List[str] = None, allowed_values: List[str] = None,
               category: str = None, classes: list = None, data_type: int = None, date_only: bool = None,
               default_values: str = None, display_after: str = None, error_message: str = None, help_text: str = None,
               label: str = None, localization_table: str = None, localized_help: str = None, localized_label: str = None,
               localized_set: str = None, mandatory: bool = None, mask: str = None, maximum_length: int = None,
               minimum_length: int = None, name: str = None, policyable: bool = None, regular_expression: str = None,
               render_hidden: bool = None, render_read_only: bool = None, single: bool = None, time_only: bool = None):
        """
        Updates a custom field's properties. If a parameter is ``None`` it does not affect the current setting of that
        property. Property values are not reset to their defaults.

        Args:
            custom_field: Config object of the metadata object.
            label: The label text for the custom field.
            name: The name of the custom field object.
            classes: The classes that this field applies to.
            data_type: The field type as an integer.
            allowed_characters: A set of allowable alphabetic, numeric, or symbols.
            allowed_values: An array of allowable values.
            category: Absolute path to the item category.
            date_only: If ``True``, a calendar date is required.
            default_values: List of default values.
            display_after: Appears after a list of Custom Field values.
            error_message: The error message when an error is encountered.
            help_text: The tool tip for the UI.
            localization_table: A list or dictionary of strings from another language.
            localized_help: The localized help text that describes the Metadata Custom Field.
            localized_label: A localized label text describing the Metadata Custom Field.
            localized_set: A list of localization settings.
            mandatory: If ``True``, this field is required.
            mask: The set of characters to use to hide user input in the UI.
            maximum_length: Maximum number of allowed characters.
            minimum_length: Minimum number of allowed characters.
            policyable: If ``True``, the custom field can be enforced on a policy folder.
            regular_expression: The regular expression to control user input.
            render_hidden: If ``True``, hides the field from the UI.
            render_read_only: If ``False``, the user can change the default values (if not locked by policy).
            single: If ``False``, the user can select/input multiple items.
            time_only: If ``True``, time of day is required.
        Returns:
            Metadata Item object.
        """
        listify = lambda x: [x] if x and not isinstance(x, list) else x

        item = {
            'AllowedCharacters': listify(allowed_characters),
            'AllowedValues': listify(allowed_values),
            'Category': listify(category),
            'Classes': listify(classes),
            'DateOnly': listify(date_only),
            'DefaultValues': listify(default_values),
            'DisplayAfter': listify(display_after),
            'ErrorMessage': listify(error_message),
            'Help': listify(help_text),
            'Label': label,
            'LocalizationTable': listify(localization_table),
            'LocalizedHelp': listify(localized_help),
            'LocalizedLabel': listify(localized_label),
            'LocalizedSet': listify(localized_set),
            'Mandatory': listify(mandatory),
            'Name': listify(name),
            'Mask': listify(mask),
            'MaximumLength': listify(maximum_length),
            'MinimumLength': listify(minimum_length),
            'Policyable': listify(policyable),
            'RegularExpression': listify(regular_expression),
            'RenderHidden': listify(render_hidden),
            'RenderReadOnly': listify(render_read_only),
            'Single': listify(single),
            'TimeOnly': listify(time_only),
            'Type': listify(data_type)
        }
        response = self._api.websdk.Metadata.UpdateItem.post(
            update={
                "DN": custom_field.dn,
                "Data": self._name_value_list(attributes=item, keep_list_values=True)
            }
        )
        self._validate_result_code(response.result)
        return self.get_item_details(custom_field=custom_field)

    def write(self, obj: 'Config.Object', custom_field: 'Config.Object', values: List, keep_existing: bool = True):
        """
        Writes a set of values to a custom field on the specified ``obj``. If ``keep_existing = False``,
        then all custom fields related to the ``obj`` are reset to their default values.

        Args:
            obj: Config object of the object with the custom field.
            custom_field: Config object of the custom field object.
            values: List of values to write to ``object_dn``.
            keep_existing: If ``True``, all other custom fields remain unaffected.
        """
        response = self._api.websdk.Metadata.Set.post(
            dn=obj.dn,
            guid_data=self._guid_data_list({custom_field.guid: values}),
            keep_existing=keep_existing
        )
        self._validate_result_code(result=response.result)

    def write_policy(self, folder: 'Config.Object', custom_field: 'Config.Object', class_name: str,
                     values: List, locked: bool = False):
        """
        Writes a set of values to a custom field on the specified ``folder``. The custom field MUST be policyable.
        To ensure, use :meth:``get`` to get the current settings and verify that ``policyable=True``. If not, use
        :meth:``update`` to update the custom field with ``policyable=True``.

        Args:
            folder: Config object of the folder.
            custom_field: Config object of the custom field object.
            class_name: Name of the object class.
            values: List of values to write to ``obj``.
            locked: If ``True``, all subordinate objects inherit and cannot modify the ``values``.
        """
        response = self._api.websdk.Metadata.SetPolicy.post(
            dn=folder.dn,
            config_class=class_name,
            guid_data=self._guid_data_list({custom_field.guid: values}),
            locked=locked
        )
        self._validate_result_code(result=response.result)
