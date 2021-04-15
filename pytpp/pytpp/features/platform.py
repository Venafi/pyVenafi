from typing import List, Dict
from pytpp.properties.config import PlatformsAttributes, PlatformsClassNames
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature


class _Platforms(FeatureBase):
    def __init__(self, api, module: str):
        super().__init__(api=api)
        self._engines_dn = r'\VED\Engines'
        self._module = module

    def _module_dn(self, engine_name: str):
        return f'{self._engines_dn}\\{engine_name}\\{self._module}'

    def _engine_has_module_enabled(self, engine_name: str):
        """
        Args:
            engine_name: Name of the platform engine.

        Returns:
            Return ``True`` if the module is enabled on the platform, otherwise ``False``.
        """
        engines = self._api.websdk.SystemStatus.get().engines
        for engine in engines:
            if engine.engine_name.lower() == engine_name.lower():
                if self._module in engine.services.vplatform.modules:
                    return True
        return False

    def update_engines(self, attributes: Dict[str, List[str]], engine_names: List[str] = None):
        """
        Updates a Platform's module attributes. Many platforms, or engines, can be provided.

        Examples:

            .. code-block:: python

                features.platforms.discovery.update_engines(
                    attributes={
                        AttributeNames.Platforms.DiscoveryManager.connection_timeout: "1"
                    },
                    engine_names=[
                        'COMPUTER_NAME_1234',
                        'DISCOVERY_ENGINE_6'
                    ]
                )

        Args:
            attributes: Dictionary of attributes and attribute values to update.
            engine_names: List of platform, or engine, names.
        """
        engine_names = engine_names or [engine.engine_name for engine in self._api.websdk.ProcessingEngines.get().engines]
        for engine_name in engine_names:
            response = self._api.websdk.Config.Write.post(
                object_dn=self._module_dn(engine_name=engine_name),
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            response.assert_valid_response()


@feature()
class AutoLayoutManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP Auto Layout Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Auto Layout Manager')


@feature()
class BulkProvisioningManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP Bulk Provisioning Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Bulk Provisioning Manager')


@feature()
class CAImportManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP CA Import Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='CA Import Manager')


@feature()
class CertificateManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP Certificate Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Manager')


@feature()
class CertificatePreEnrollment(_Platforms):
    """
    This feature provides high-level interaction with the TPP ficate Pre-Enrollment Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Pre-Enrollment')


@feature()
class CertificateRevocation(_Platforms):
    """
    This feature provides high-level interaction with the TPP Certificate Revocation Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Revocation')


@feature()
class CloudInstanceMonitor(_Platforms):
    """
    This feature provides high-level interaction with the TPP Cloud Instance Monitor Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Cloud Instance Monitor')


@feature()
class DiscoveryManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP Discovery Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Discovery')


@feature()
class Monitor(_Platforms):
    """
    This feature provides high-level interaction with the TPP Monitor module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Monitor')


@feature()
class OnboardDiscoveryManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP OnBoard Discovery Manager Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Onboard Discovery Manager')


@feature()
class Reporting(_Platforms):
    """
    This feature provides high-level interaction with the TPP Reporting module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Reporting')


@feature()
class SSHManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP SSH Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='SSH Manager')


@feature()
class TrustNetManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP TrustNet Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='TrustNet Manager')


@feature()
class ValidationManager(_Platforms):
    """
    This feature provides high-level interaction with the TPP Validation Manager module.
    """
    def __init__(self, api):
        super().__init__(api=api, module='Validation Manager')
