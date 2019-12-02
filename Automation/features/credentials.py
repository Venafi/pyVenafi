import time
from typing import *
from enums.config import CredentialAttributes
from features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class UsernamePasswordCredential(FeatureBase):
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, username: str, password: str, expiration: int = None, description: str = None,
               encryption_key: str = None, shared: bool = False, contact: List[str] = None):
        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        expiration = expiration or int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)  # Default to expire in 10 years.

        result = self.auth.websdk.Credentials.Create.post(
            credential_path=dn,
            friendly_name='UsernamePassword',
            values=[
                {'Name': 'Username', 'Type': 'string', 'Value': username},
                {'Name': 'Password', 'Type': 'string', 'Value': password}
            ],
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact
        ).result

        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)

        return self.auth.websdk.Config.IsValid.post(object_dn=dn).object

    def delete(self, object_dn: str):
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Credentials.Delete.post(credential_path=object_dn).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.credential_result)
