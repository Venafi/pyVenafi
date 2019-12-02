from enums.config import ConfigClass
from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _DeviceBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def _create(self, config_class:str, name: str, container: str, attributes: dict = None):
        if attributes:
            attributes = self._name_value_attributes(attributes=attributes)

        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        ca = self.auth.websdk.Config.Create.post(dn, config_class, attributes or [])

        result = ca.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return ca.object

    def delete(self, object_dn: str):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Config.Delete.post(object_dn).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)


@feature()
class Device(_DeviceBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, attributes: dict = None):
        return self._create(config_class=ConfigClass.device, name=name, container=container, attributes=attributes)
