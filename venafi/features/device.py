from venafi.properties.config import ConfigClass, DeviceAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _DeviceBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str):
        self._config_delete(object_dn=object_dn)


@feature()
class Device(_DeviceBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, container: str, hostname: str, credential_dn: str, attributes: dict = None):
        attributes = attributes or {}
        device_attrs = DeviceAttributes.Device
        attributes.update({
            device_attrs.host: hostname,
            device_attrs.credential: credential_dn
        })
        return self._config_create(
            name=name,
            container=container,
            config_class=ConfigClass.device,
            attributes=attributes
        )
