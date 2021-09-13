from datetime import datetime, timedelta
from typing import List, Union
from pytpp.vtypes import Config
from pytpp.properties.config import CredentialAttributes, CredentialClassNames
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature


class _CredentialBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def _create(self, name: str, parent_folder_dn: str, friendly_name: str, values: List[dict], expiration: int,
                description: str, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
                get_if_already_exists: bool = True):
        dn = f'{parent_folder_dn}\\{name}'

        expiration = int((datetime.now() + timedelta(expiration * (365 / 12))).timestamp() * 1000)

        result = self._api.websdk.Credentials.Create.post(
            credential_path=dn,
            friendly_name=friendly_name,
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact
        ).result

        if result.code != 1:
            if result.code == 401 and get_if_already_exists:
                return self._get_config_object(object_dn=dn)
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.credential_result)

        return self._get_config_object(object_dn=dn)

    def delete(self, credential: Union['Config.Object', str]):
        """
        Deletes the credential object.

        Args:
            credential: Config object of the credential object.
        """
        result = self._api.websdk.Credentials.Delete.post(credential_path=credential.dn).result
        if result.code != 1:
            raise FeatureError.InvalidResultCode(code=result.code, code_description=result.credential_result)

    def get(self, credential_dn: str, raise_error_if_not_exists: bool = True):
        """
        Gets the credential Config.Object from TPP.

        Args:
            credential_dn: DN of the credential object.
            raise_error_if_not_exists: Raise an exception if the credential DN does not exist.

        Returns:
            Config object of the credential object.
        """
        return self._get_config_object(
            object_dn=credential_dn,
            raise_error_if_not_exists=raise_error_if_not_exists,
            valid_class_names=list(CredentialClassNames)
        )


@feature()
class AmazonCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP Amazon Credentials.
    """

    def __init__(self, api):
        super().__init__(api)

    def create_adfs(self, name: str, parent_folder_dn: str, adfs_credential_dn: str, adfs_url: str, role: str, expiration: int = 6,
                    description: str = None, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
                    get_if_already_exists: bool = True):
        """
        Creates a Local Amazon Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            adfs_credential_dn: Absolute path to the ADFS credential object in TPP.
            adfs_url: ADFS URL.
            role: Role.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value( name='Source', type='string', value='ADFS'),
            self._name_type_value(name='AdfsUrl', type='string', value=adfs_url),
            self._name_type_value(name='AdfsCredential', type='string', value=adfs_credential_dn),
            self._name_type_value(name='Role', type='string', value=role),
        ]
        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='Amazon',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )

    def create_local(self, name: str, parent_folder_dn: str, access_key: str, secret_key: str, role: str = None,
                     external_id: str = None, expiration: int = 6, description: str = None, encryption_key: str = None,
                     shared: bool = False, contact: List[str] = None, get_if_already_exists: bool = True):
        """
        Creates a Local Amazon Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            access_key: Access Key.
            secret_key: Secret Key.
            role: Role.
            external_id: External ID.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value(name='Source', type='string', value='Local'),
            self._name_type_value(name='AccessKey', type='string', value=access_key),
            self._name_type_value(name='ExternalId', type='string', value=external_id),
            self._name_type_value(name='SecretKey', type='string', value=secret_key),
            self._name_type_value(name='Role', type='string', value=role),
        ]
        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='Amazon',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class CertificateCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP Certificate Credentials.
    """

    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder_dn: str, certificate: str, password: str = None, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
               get_if_already_exists: bool = True):
        """
        Creates a Certificate Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            certificate: Base64-encoded PKCS#12 or PFX certificate.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value(name='Certificate', type='byte[]', value=certificate)
        ]
        if password:
            values.append(self._name_type_value('Password', 'string', value=password))

        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='Certificate',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class GenericCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP Generic Credentials.
    """

    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder_dn: str, generic: str, password: str = None, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
               get_if_already_exists: bool = True):
        """
        Creates a Generic Password Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            generic: Unclassified binary data.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value('Generic', 'byte[]', value=generic),
            self._name_type_value('Password', 'string', value=password)
        ]

        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='Generic',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class PasswordCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP Password Credentials.
    """

    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder_dn: str, password: str, expiration: int = 6, description: str = None,
               encryption_key: str = None, shared: bool = False, contact: List[str] = None,
               get_if_already_exists: bool = True):
        """
        Creates a Password Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value('Password', 'string', value=password)
        ]

        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='Password',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class PrivateKeyCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP PrivateKey Credentials.
    """

    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder_dn: str, private_key: str, username: str, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
               get_if_already_exists: bool = True):
        """
        Creates a Private Key Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            private_key: Base64-encoded (PKCS#8) private key.
            username: Username.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value('Key', 'byte[]', value=private_key),
            self._name_type_value('Username', 'string', value=username)
        ]

        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='PrivateKey',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )


@feature()
class UsernamePasswordCredential(_CredentialBase):
    """
    This feature provides high-level interaction with TPP Username/Password Credentials.
    """
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder_dn: str, username: str, password: str, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contact: List[str] = None,
               get_if_already_exists: bool = True):
        """
        Creates a Username/Password Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder_dn: Absolute path to the parent folder of the credential object.
            username: Username.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contact: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.

        """
        values = [
            self._name_type_value(name='Username', type='string', value=username),
            self._name_type_value(name='Password', type='string', value=password)
        ]
        return self._create(
            name=name,
            parent_folder_dn=parent_folder_dn,
            friendly_name='UsernamePassword',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contact=contact,
            get_if_already_exists=get_if_already_exists
        )
