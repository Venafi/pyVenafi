from datetime import datetime, timedelta
from typing import *
from venafi.properties.config import CredentialAttributes
from venafi.features.bases.feature_base import FeatureBase, FeatureError, ApiPreferences, feature


@feature()
class UsernamePasswordCredential(FeatureBase):
    """
    This feature provides high-level interaction with TPP Username/Password Credentials.
    """
    def __init__(self, auth):
        super().__init__(auth)

    def create(self, name: str, container: str, username: str, password: str, expiration: int = 6, description: str = None,
               encryption_key: str = None, shared: bool = False, contact: List[str] = None):
        """
        Creates a Username/Password Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            container: Absolute path to the parent folder of the credential object.
            username: Username.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.

        Returns:
            Config object representing the credential.

        """
        dn = f'{container}\\{name}'

        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        expiration = int((datetime.now() + timedelta(expiration * (365/12))).timestamp() * 1000)

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

        response = self.auth.websdk.Config.IsValid.post(object_dn=dn)
        result = response.result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.config_result)
        return response.object

    def delete(self, object_dn: str):
        """
        Deletes the credential object.

        Args:
            object_dn: Absolute path to the credential object.
        """
        if self.auth.preference == ApiPreferences.aperture:
            self._log_not_implemented_warning(ApiPreferences.aperture)

        result = self.auth.websdk.Credentials.Delete.post(credential_path=object_dn).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.credential_result)
