from typing import List
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature
from venafi.properties.config import FolderClassNames


@feature()
class Attributes(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)
        self.policy = self._Policy(auth=auth)

    def wait_for(self, object_dn: str, attiribute_name: str, attribute_value: str, timeout: int = 10):
        def get_attribute():
            values = self.read(object_dn=object_dn, attribute_name=attiribute_name)
            found = any([True for value in values if str(value).lower() == attribute_value.lower()])
            if found:
                return True
        self._wait_for_method(method=get_attribute, return_value=True, timeout=timeout)

    def add_value(self, object_dn: str, attributes: dict):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        for name, value in attributes.items():
            result = self.auth.websdk.Config.AddValue.post(
                object_dn=object_dn,
                attribute_name=name,
                value=value,
            ).result

            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def read(self, object_dn: str, attribute_name: str = None):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        resp = self.auth.websdk.Config.ReadEffectivePolicy.post(
            object_dn=object_dn,
            attribute_name=attribute_name
        )

        result = resp.result
        if result.code != 1:
            FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return resp.values

    def read_all(self, object_dn: str):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        resp = self.auth.websdk.Config.ReadAll.post(object_dn=object_dn)

        result = resp.result
        if result.code != 1:
            FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

        return resp.name_values

    def clear(self, object_dn: str, attributes: dict):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        for name, values in attributes.items():
            if not isinstance(values, list):
                values = [values]

            for value in values:
                result = self.auth.websdk.Config.RemoveDnValue.post(
                    object_dn=object_dn,
                    attribute_name=name,
                    value=value
                ).result

                if result.code != 1:
                    raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def clear_all(self, object_dn: str, attribute_names: List[str]):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        for attribute_name in attribute_names:
            result = self.auth.websdk.Config.ClearAttribute.post(
                object_dn=object_dn,
                attribute_name=attribute_name
            ).result

            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def rename_object(self, object_dn: str, new_object_dn: str):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Config.RenameObject.post(object_dn=object_dn, new_object_dn=new_object_dn).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    def write(self, object_dn: str, attributes: dict):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        attributes = {k: ([v] if not isinstance(v, list) else v) for k, v in attributes.items()}

        result = self.auth.websdk.Config.Write.post(
            object_dn=object_dn,
            attribute_data=self._name_value_list(attributes)
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

    class _Policy(FeatureBase):
        def __init__(self, auth):
            super().__init__(auth=auth)

        def _validate_object_is_folder(self, object_dn: str):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            resp = self.auth.websdk.Config.IsValid.post(object_dn=object_dn).object
            if resp.type_name != FolderClassNames.policy:
                raise FeatureError(f'Expected "{object_dn}" to be of class" {FolderClassNames.policy}", '
                                   f'but it is of type "{resp.type_name}" instead.')

        def add_value(self, folder_dn: str, class_name: str, attributes: dict, locked: bool):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            self._validate_object_is_folder(object_dn=folder_dn)

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

        def clear(self, folder_dn: str, attributes: dict):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            self._validate_object_is_folder(object_dn=folder_dn)

            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                for value in values:
                    result = self.auth.websdk.Config.RemovePolicyValue.post(
                        object_dn=folder_dn,
                        attribute_name=name,
                        value=value
                    ).result

                    if result.code != 1:
                        raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        def clear_all(self, folder_dn: str, class_name: str, attribute_names: List[str]):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            self._validate_object_is_folder(object_dn=folder_dn)

            for attribute_name in attribute_names:
                result = self.auth.websdk.Config.ClearPolicyAttribute.post(
                    object_dn=folder_dn,
                    attribute_name=attribute_name,
                    class_name=class_name
                ).result

                if result.code != 1:
                    raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        def find(self, object_dn: str, class_name: str, attribute_name: str):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            resp = self.auth.websdk.Config.FindPolicy.post(
                object_dn=object_dn,
                class_name=class_name,
                attribute_name=attribute_name
            )

            result = resp.result
            if result.code != 1:
                raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

            return resp.policy_dn, resp.values, resp.locked

        def read(self, folder_dn: str, class_name: str, attribute_name: str):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            self._validate_object_is_folder(object_dn=folder_dn)

            resp = self.auth.websdk.Config.ReadPolicy.post(
                object_dn=folder_dn,
                class_name=class_name,
                attribute_name=attribute_name
            )

            result = resp.result
            if result.code != 1:
                FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result).log()

            return resp.values, resp.locked

        def write(self, folder_dn: str, class_name: str, attributes: dict, locked: bool):
            if self.auth.preference == ApiPreferences.aperture:
                self._log_not_implemented_warning(ApiPreferences.aperture)

            self._validate_object_is_folder(object_dn=folder_dn)

            for name, values in attributes.items():
                if not isinstance(values, list):
                    values = [values]

                result = self.auth.websdk.Config.WritePolicy.post(
                    object_dn=folder_dn,
                    class_name=class_name,
                    attribute_name=name,
                    values=values,
                    locked=locked,
                ).result

                if result.code != 1:
                    raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
