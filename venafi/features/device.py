from venafi.properties.config import DevicesClassNames, DeviceAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _DeviceBase(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth=auth)

    def delete(self, object_dn: str):
        """
        Deletes the device object specified. Since there are no secret store data attached to this object,
        only a config delete is performed.

        Args:
            object_dn: Absolute path to the device object.
        """
        self._config_delete(object_dn=object_dn)


@feature()
class Device(_DeviceBase):
    """
    This feature provides high-level interaction with TPP device objects.
    """
    def __init__(self, auth):
        super().__init__(auth=auth)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Device object in TPP.

        Args:
            name: Name of the device object .
            parent_folder_dn: Absolute path to the parent folder of the device object.
            hostname: DNS or IP Address of the device.
            credential_dn: Absolute path to the credential object for this device.
            attributes: List of attributes pertaining to the device object.

        Returns:
            Config object representing the device.

        """
        return self._config_create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            config_class=DevicesClassNames.device,
            attributes=attributes
        )
