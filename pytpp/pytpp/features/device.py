from typing import Union
from pytpp.vtypes import Config
from pytpp.properties.config import DevicesClassNames, DeviceAttributes, DeviceAttributeValues
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature


class _DeviceBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, device: Union['Config.Object', str]):
        """
        Deletes the device object specified. Since there are no secret store data attached to this object,
        only a config delete is performed.

        Args:
            device: Config object of to the device object.
        """
        dn = self._get_dn(device)
        self._config_delete(object_dn=dn)


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

    def get(self, device_dn: str):
        response = self._api.websdk.Config.IsValid.post(object_dn=device_dn)

        if response.result.code != 1:
            raise FeatureError.InvalidResultCode(code=response.result.code,
                                                 code_description=response.result.credential_result)
        return response.object

    def scan_for_ssh_keys(self, device: Union['Config.Object', str]):
        """
        Args:
            device: Config.Object, DN, or GUID of the device object in TPP.
        """
        dn = self._get_dn(device)
        result = self._api.websdk.Config.Write.post(
            object_dn=dn,
            attribute_data=[{"Name": "Agentless Discovery To Do",
                            "Value": "1"}]
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)


