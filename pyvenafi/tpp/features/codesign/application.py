from dataclasses import dataclass
from typing import (
    List,
    Union,
)

from pyvenafi.tpp.api.websdk.models.codesign import (
    Application,
    ApplicationCollection,
)
from pyvenafi.tpp.api.websdk.models.config import Object
from pyvenafi.tpp.features.bases.feature_base import (
    feature,
    FeatureBase,
)

class _CodeSignApplicationBase(FeatureBase):
    def count_references(
        self,
        application: Union[Application, ApplicationCollection]
    ):
        """
        Get the number of references to a :class:`~.models.codesign.Application`
        or a :class:`~.models.codesign.ApplicationCollection` that are currently in
        use within CodeSign Protect projects.

        Args:
            application: class:`~.models.codesign.Application` or :class:`~.models.codesign.ApplicationCollection`

        Returns:
            Integer
        """
        if isinstance(application, Application):
            key = 'application'
        elif isinstance(application, ApplicationCollection):
            key = 'application_collection'
        else:
            raise ValueError(f'Invalid type {application.__class__.__name__}')
        kwargs = {
            key: application
        }
        output = self._api.websdk.Codesign.CountReferences.post(**kwargs)
        return output.count

    def enumerate_references(
        self,
        application: Application = None,
        application_dn: str = None,
        application_guid: str = None,
        collection: ApplicationCollection = None,
        collection_dn: str = None,
        collection_guid: str = None
    ) -> List[str]:
        """
        Get the :ref:`dn`\s that references a :class:`~.models.codesign.Application`
        or a :class:`~.models.codesign.ApplicationCollection` using one parameter.

        Args:
            application: :class:`~.models.codesign.Application`.
            application_dn: :ref:`dn` of an application.
            application_guid: :ref:`guid` of an application.
            collection: :class:`~.models.codesign.ApplicationCollection`.
            collection_dn: :ref:`dn` of an application collection.
            collection_guid: :ref:`guid` of an application collection.

        Returns:
            List[:ref:`dn`]
        """
        params = [
            application,
            application_dn,
            application_guid,
            collection,
            collection_dn,
            collection_guid,
        ]
        if sum(map(bool, params)) != 1:
            raise ValueError('Please provide only one argument')
        output = self._api.websdk.Codesign.EnumerateReferences.post(
            application=application,
            application_collection=collection,
            application_dn=application_dn,
            application_guid=application_guid,
            collection_dn=collection_dn,
            collection_guid=collection_guid,
        )
        return output.reference_dns

@feature('Application')
class CodeSignApplication(_CodeSignApplicationBase):
    def create(
        self,
        name: str,
        parent_folder: Union[Object, str] = r'\VED\Code Signing\Signing Applications',
        description: str = None,
        hash: str = None,  # noqa
        location: str = None,
        permitted_argument_pattern: str = None,
        signatory_issuer: str = None,
        signatory_subject: str = None,
        size: int = None,
        version: str = None,
        raise_if_already_exists: bool = False,
    ) -> Application:
        """
        Create an application with specified values.

        Args:
            name: Name of the application.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            description: Description of the application.
            hash: The SHA256 checksum of the application binary.
            location: The physical path where the signing application is installed.
            permitted_argument_pattern: The pattern of arguments that the signing application uses to run.
            signatory_issuer: The X.500 certificate issuer that signs the application.
            signatory_subject: The X.500 certificate subject.
            size: The size of the signing application executable.
            version: The signing application version.
            raise_if_already_exists: If the object already exists, raise an error.

        Returns:
            :class:`~.models.codesign.Application`
        """
        parent_dn = self._get_dn(parent_folder)
        dn = rf'{parent_dn}\{name}'
        try:
            self._api.websdk.Codesign.CreateApplication.post(dn=dn)
        except:
            if raise_if_already_exists:
                raise
        application = self.get(dn=dn)

        if any(
                [
                    description,
                    hash,
                    location,
                    permitted_argument_pattern,
                    signatory_issuer,
                    signatory_subject,
                    size,
                    version,
                ]
        ):
            application.description = description
            application.hash = hash
            application.location = location
            application.permitted_argument_pattern = permitted_argument_pattern
            application.signatory_issuer = signatory_issuer
            application.signatory_subject = signatory_subject
            application.size = size
            application.version = version
            self.update(application=application)
            application = self.get(dn=dn)

        return application

    def update(
        self,
        application: Union[Object, Application]
    ):
        """
        Update an application.

        Args:
            application: The updated :class:`~.models.codesign.Application`.
        """
        self._api.websdk.Codesign.UpdateApplication.post(application=application)

    def rename(
        self,
        application: Union[str, Object, Application],
        new_dn: str
    ):
        """
        Rename an application by giving it a new :ref:`dn`.

        Args:
            application: :class:`~.models.codesign.Application`, :ref:`config_object`, or :ref:`dn` of the application.
            new_dn: The new :ref:`dn` for the application.
        """
        dn = self._get_dn(application)
        self._api.websdk.Codesign.RenameApplication.post(new_dn=new_dn, dn=dn)

    def get(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> Application:
        """
        Get an application using a :ref:`dn`, :ref:`guid`, or Identifier.

        Args:
            dn: :ref:`dn` of the application.
            guid: :ref:`guid` of the application.
            id: Identifier of the application.

        Returns:
            :class:`~.models.codesign.Application`
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetApplication.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError('You must provide a dn, guid, or id to get an application.')
        if not output.application:
            raise Exception('Application does not exist.')
        return output.application

    def enumerate(
        self,
        _filter: str = None
    ) -> List[Application]:
        """
        Enumerate the applications.

        Args:
            _filter: The partial tool name and optional trailing asterisk (*) wild card.

        Returns:
            List[:class:`~.models.codesign.Application`]
        """
        output = self._api.websdk.Codesign.EnumerateApplications.post(filter=_filter)
        return output.applications

    def delete(
        self,
        application: Union[str, Object, Application]
    ):
        """
        Delete an application.

        Args:
            application: :class:`~.models.codesign.Application`, :ref:`dn` , or :ref:`config_object` of the application.
        """
        dn = self._get_dn(application)
        if dn:
            self._api.websdk.Codesign.DeleteApplication.post(dn=dn)
        else:
            guid = self._get_guid(application)
            if guid:
                self._api.websdk.Codesign.DeleteApplication.post(guid=guid)
            else:
                raise ValueError('Invalid argument to delete the application.')

@feature('Application Collection')
class CodeSignApplicationCollection(FeatureBase):
    def create(
        self,
        name: str,
        parent_folder: Union[Object, str] = r'\VED\Code Signing\Signing Applications',
        applications: List[Union[str, Object, Application]] = None,
        raise_if_already_exists: bool = False,
    ) -> ApplicationCollection:
        """
        Create an application collection.

        Args:
            name: Name of the application collection.
            parent_folder: :ref:`dn` of the parent folder.
            applications: List of applications to include in the application collection.
            raise_if_already_exists: If the object already exists, raise an error.

        Returns:
            :class:`~.models.codesign.ApplicationCollection`
        """
        parent_dn = self._get_dn(parent_folder)
        dn = rf'{parent_dn}\{name}'
        try:
            self._api.websdk.Codesign.CreateApplicationCollection.post(dn=dn)
        except:
            if raise_if_already_exists:
                raise

        collection = self.get(dn=dn)
        if applications:
            application_dns = [self._get_dn(a) for a in applications]
            collection.application_dns.items = application_dns
            self.update(collection=collection)
            collection = self.get(dn=dn)

        return collection

    def update(
        self,
        collection: Union[Object, ApplicationCollection]
    ):
        """
        Update an application collection.

        Args:
            collection: The updated :class:`~.models.codesign.ApplicationCollection`.
        """
        self._api.websdk.Codesign.UpdateApplicationCollection.post(application_collection=collection)

    def rename(
        self,
        collection: Union[str, Object, Application],
        new_dn: str
    ):
        """
        Rename an application collection object by giving it a new :ref:`dn`.

        Args:
            collection: :class:`~.models.codesign.ApplicationCollection`, :ref:`config_object`, or :ref:`dn` of the application collection object.
            new_dn: The new :ref:`dn` for the application collection.
        """
        dn = self._get_dn(collection)
        self._api.websdk.Codesign.RenameApplicationCollection.post(new_dn=new_dn, dn=dn)

    def get(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> ApplicationCollection:
        """
        Get an application collection object using a :ref:`dn`, :ref:`guid`, or Identifier.

        Args:
            dn: :ref:`dn` of the application collection object.
            guid: :ref:`guid` of the application collection object.
            id: Identifier of the application collection object.

        Returns:
            :class:`~.models.codesign.ApplicationCollection`
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetApplicationCollection.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError('You must provide a dn, guid, or id to get an application collection.')
        if not output.application_collection:
            raise Exception('Application collection does not exist.')
        return output.application_collection

    def get_members(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ) -> ApplicationCollection:
        """
        Get :ref:`dn`\s of applications and application collections that are members of an application collection.

        Args:
            dn: :ref:`dn` of the application collection object.
            guid: :ref:`guid` of the application collection object.
            id: Identifier of the application collection object.

        Returns:
            List[:ref:`dn`\s.]
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetApplicationCollectionMembers.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError("You must provide a dn, guid, or id to get an application collection's members.")
        if not output.application_collection:
            raise Exception('Application collection does not exist.')
        return output.application_collection.application_dns.items

    def get_member_dns(
        self,
        dn: str = None,
        guid: str = None,
        id: str = None
    ):
        """
        Get :ref:`dn`\s of applications and application collections that are members of an application collection.

        Args:
            dn: :ref:`dn` of the application collection object.
            guid: :ref:`guid` of the application collection object.
            id: Identifier of the application collection object.

        Returns:
            Dataclass object containing:
            * :class:`~.models.codesign.ApplicationCollection`
            * List[:ref:`dn`] of application collections.
            * List[:ref:`dn`] of applications.
        """
        if any([dn, guid, id]):
            output = self._api.websdk.Codesign.GetApplicationCollectionMemberDNs.post(dn=dn, guid=guid, id=id)
        else:
            raise ValueError("You must provide a dn, guid, or id to get an application collection's members.")

        @dataclass
        class ApplicationCollectionDns:
            application_collection: ApplicationCollection = output.application_collection
            application_collection_dns: List[str] = output.application_collection_dns
            application_dns: List[str] = output.application_dns

        return ApplicationCollectionDns(
            application_collection=output.application_collection,
            application_collection_dns=output.application_collection_dns,
            application_dns=output.application_dns
        )

    def enumerate(
        self,
        _filter: str = None
    ) -> List[ApplicationCollection]:
        """
        Enumerate the application collections.

        Args:
            _filter: The partial tool name and optional trailing asterisk (*) wild card.

        Returns:
            List[:class:`~.models.codesign.ApplicationCollection`]
        """
        output = self._api.websdk.Codesign.EnumerateApplicationCollections.post(filter=_filter)
        return output.application_collections

    def delete(
        self,
        collection: Union[str, Object, ApplicationCollection]
    ):
        """
        Delete an application collection.

        Args:
            collection: :class:`~.models.codesign.ApplicationCollection`, :ref:`dn`, or :ref:`config_object` of the application.
        """
        dn = self._get_dn(collection)
        if dn:
            self._api.websdk.Codesign.DeleteApplicationCollection.post(dn=dn)
        else:
            guid = self._get_guid(collection)
            if guid:
                self._api.websdk.Codesign.DeleteApplicationCollection.post(guid=guid)
            else:
                raise ValueError('Invalid argument to delete the application collection.')
