from datetime import datetime, timedelta
from typing import List, Union, TYPE_CHECKING
from pytpp.tools.vtypes import Config
from pytpp.features.bases.feature_base import FeatureBase, FeatureError, feature
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Identity


class _CredentialBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def _create(self, name: str, parent_folder: 'Union[Config.Object]', friendly_name: str, values: List[dict], expiration: int,
                description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
                get_if_already_exists: bool = True):
        parent_folder_dn = self._get_dn(parent_folder)
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
            contact=[self._get_prefixed_universal(c) for c in contacts] if contacts else None
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
            ``Config.Object``
        """
        return self._get_config_object(
            object_dn=credential_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )


@feature('Amazon Credential')
class AmazonCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create_adfs(self, name: str, parent_folder: 'Union[Config.Object]', adfs_credential: 'Union[Config.Object, str]', adfs_url: str,
                    role: str, expiration: int = 6, description: str = None, encryption_key: str = None, shared: bool = False,
                    contacts: 'List[Union[Identity.Identity, str]]' = None, get_if_already_exists: bool = True):
        """
        Creates a Local Amazon Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            adfs_credential: ``Config.Object`` or DN of the ADFS username credential.
            adfs_url: ADFS URL.
            role: Role.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value( name='Source', type='string', value='ADFS'),
            self._name_type_value(name='AdfsUrl', type='string', value=adfs_url),
            self._name_type_value(name='AdfsCredential', type='string', value=self._get_dn(adfs_credential)),
            self._name_type_value(name='Role', type='string', value=role),
        ]
        return self._create(
            name=name,
            parent_folder=parent_folder,
            friendly_name='Amazon',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )

    def create_local(self, name: str, parent_folder: 'Union[Config.Object]', access_key: str, secret_key: str, role: str = None,
                     external_id: str = None, expiration: int = 6, description: str = None, encryption_key: str = None,
                     shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None, get_if_already_exists: bool = True):
        """
        Creates a Local Amazon Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            access_key: Access Key.
            secret_key: Secret Key.
            role: Role.
            external_id: External ID.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
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
            parent_folder=parent_folder,
            friendly_name='Amazon',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Certificate Credential')
class CertificateCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object]', certificate: str, password: str = None, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Certificate Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            certificate: Base64-encoded PKCS#12 or PFX certificate.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
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
            parent_folder=parent_folder,
            friendly_name='Certificate',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Google Credential')
class GoogleCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', json_content: 'str', expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Generic Password Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            json_content: JSON content as plain text.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        import json
        values = [
            self._name_type_value('Json', 'string', value=json.dumps(json_content)),
        ]

        return self._create(
            name=name,
            parent_folder=parent_folder,
            friendly_name='Google',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Generic Credential')
class GenericCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object]', generic: str, password: str = None, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Generic Password Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            generic: Unclassified binary data.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
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
            parent_folder=parent_folder,
            friendly_name='Generic',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Password Credential')
class PasswordCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object]', password: str, expiration: int = 6, description: str = None,
               encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Password Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
            get_if_already_exists: bool = True

        Returns:
            Config object representing the credential.
        """
        values = [
            self._name_type_value('Password', 'string', value=password)
        ]

        return self._create(
            name=name,
            parent_folder=parent_folder,
            friendly_name='Password',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Private Key Credential')
class PrivateKeyCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object]', private_key: str, username: str, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Private Key Credential object in TPP. The credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            private_key: Base64-encoded (PKCS#8) private key.
            username: Username.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
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
            parent_folder=parent_folder,
            friendly_name='PrivateKey',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )


@feature('Username/Password Credential')
class UsernamePasswordCredential(_CredentialBase):
    def __init__(self, api):
        super().__init__(api)

    def create(self, name: str, parent_folder: 'Union[Config.Object]', username: str, password: str, expiration: int = 6,
               description: str = None, encryption_key: str = None, shared: bool = False, contacts: 'List[Union[Identity.Identity, str]]' = None,
               get_if_already_exists: bool = True):
        """
        Creates a Username/Password Credential object in TPP. By default, the credential is set to expire 6 months from now.

        Args:
            name: Name of the credential object.
            parent_folder: ``Config.Object`` or DN of the parent folder.
            username: Username.
            password: Password.
            expiration: Number months from today at which the credential expires.
            description: Description of the credential object.
            encryption_key: Encryption Key used to protect the credential data.
            shared: If True, the credential can be shared between multiple objects.
            contacts: List of absolute paths to the users in TPP to be established as contacts.
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
            parent_folder=parent_folder,
            friendly_name='UsernamePassword',
            values=values,
            expiration=expiration,
            description=description,
            encryption_key=encryption_key,
            shared=shared,
            contacts=contacts,
            get_if_already_exists=get_if_already_exists
        )
