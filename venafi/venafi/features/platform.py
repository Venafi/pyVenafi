from typing import List, Dict
from venafi.properties.config import PlatformsAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


class _Platforms(FeatureBase):
    def __init__(self, auth, module: str):
        super().__init__(auth=auth)
        self._engines_dn = r'\VED\Engines'
        self._module = module

    def _module_dn(self, engine_name: str):
        return f'{self._engines_dn}\\{engine_name}\\{self._module}'

    def _engine_has_module_enabled(self, engine_name: str):
        engines = self._auth.websdk.SystemStatus.get().engines
        for engine in engines:
            if engine.engine_name.lower() == engine_name.lower():
                if self._module in engine.services.vplatform.modules:
                    return True
        return False

    def update_engines(self, attributes: Dict[str, List[str]], engine_names: List[str] = None):
        if self._auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        engine_names = engine_names or [engine.engine_name for engine in self._auth.websdk.ProcessingEngines.get().engines]
        for engine_name in engine_names:
            response = self._auth.websdk.Config.Write.post(
                object_dn=self._module_dn(engine_name=engine_name),
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            response.assert_valid_response()


@feature()
class AutoLayoutManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Auto Layout Manager')


@feature()
class BulkProvisioningManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Bulk Provisioning Manager')


@feature()
class CAImportManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='CA Import Manager')


@feature()
class CertificateManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Certificate Manager')


@feature()
class CertificatePreEnrollment(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Certificate Pre-Enrollment')


@feature()
class CertificateRevocation(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Certificate Revocation')


@feature()
class CloudInstanceMonitor(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Cloud Instance Monitor')


@feature()
class DiscoveryManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Discovery')


@feature()
class Monitor(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Monitor')


@feature()
class OnboardDiscoveryManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Onboard Discovery Manager')


@feature()
class Reporting(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Reporting')


@feature()
class SSHManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='SSH Manager')


@feature()
class TrustNetManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='TrustNet Manager')


@feature()
class ValidationManager(_Platforms):
    def __init__(self, auth):
        super().__init__(auth=auth, module='Validation Manager')
