from enum_types.misc import ApiPreferences
from features.bases.feature_base import FeatureBase, FeatureError
from enum_types.config_classes import ConfigClass


class Folder(FeatureBase):
    def __init__(self, auth_obj, name=None, container=None, attributes=None):
        super().__init__(auth_obj)

        self.absolute_guid = None
        self.dn = None
        self.guid = None
        self.config_id = None
        self.name = None
        self.parent = None
        self.revision = None
        self.type_name = None

        self.name = name
        self.container = container
        self.attributes = attributes

    def __enter__(self):
        return self.create()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete(self.dn, recursive=True)

    def reinitialize(self):
        self.absolute_guid = None
        self.dn = None
        self.guid = None
        self.config_id = None
        self.name = None
        self.parent = None
        self.revision = None
        self.type_name = None

    def load(self, policy_object):
        self.absolute_guid = policy_object.absolute_guid
        self.dn = policy_object.dn
        self.guid = policy_object.guid
        self.config_id = policy_object.config_id
        self.name = policy_object.name
        self.parent = policy_object.parent
        self.revision = policy_object.revision
        self.type_name = policy_object.type_name

    def create(self, name=None, container=None, attributes=None):
        if not name:
            if not self.name:
                raise AssertionError('Must supply a name property.')
            name = self.name
        if not container:
            if not self.container:
                raise AssertionError('Must supply a container property.')
            container = self.container
        if not attributes:
            if self.attributes:
                if not isinstance(attributes, list):
                    raise TypeError('Attributes must be a list.')
                attributes = self.attributes

        dn = container + '\\' + name

        self._logger.log('Creating policy with DN "%s".' % dn)
        if self.auth.preference == ApiPreferences.websdk:
            policy = self.auth.websdk.Config.Create.post(dn, ConfigClass.policy, attributes or []).object
        elif self.auth.preference == ApiPreferences.aperture:
            policy = self.auth.aperture.ConfigObjects.Policies.post(name, container).object
        else:
            raise FeatureError.invalid_api_preference(self.auth.preference)

        self.load(policy)
        if self.dn:
            self._logger.log('Folder DN is %s.' % self.dn)
        else:
            raise ValueError('DN not created as expected.')

        return self

    def delete(self, object_dn, recursive=False):
        self._logger.log('Deleting policy with DN "%s".' % object_dn)
        if self.auth.preference == ApiPreferences.aperture:
            self._logger(FeatureError.not_implemented(ApiPreferences.aperture))

        result = self.auth.websdk.Config.Delete.post(object_dn, recursive).result
        self.reinitialize()
