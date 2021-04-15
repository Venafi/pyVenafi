from pytpp.vtypes import Config
from pytpp.properties.config import DevicesClassNames, DeviceAttributes, DeviceAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, feature


class _DeviceBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, device: 'Config.Object'):
        """
        Deletes the device object specified. Since there are no secret store data attached to this object,
        only a config delete is performed.

        Args:
            device: Config object of to the device object.
        """
        self._config_delete(object_dn=device.dn)


@feature()
class Device(_DeviceBase):
    """
    This feature provides high-level interaction with TPP device objects.
    """
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder_dn: str, attributes: dict = None):
        """
        Creates a Device object in TPP.

        Args:
            name: Name of the device object .
            parent_folder_dn: Absolute path to the parent folder of the device object.
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
