import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from objects.response_objects.config import Config


class _Config:
    def __init__(self, session, api_type):
        self.AddDnValue = self._AddDnValue(session, api_type)
        self.AddPolicyValue = self._AddPolicyValue(session, api_type)
        self.Create = self._Create(session, api_type)
        self.Delete = self._Delete(session, api_type)
        self.FindObjectsOfClass = self._FindObjectsOfClass(session, api_type)

    class _AddDnValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/AddDnValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not add DN Value. Received %s: %s.' %(result.code, result.config_result))
            self.logger.log('Successfully added DN value.')
            return result

        def post(self, object_dn, attribute_name, value):
            body = json.dumps({
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _AddPolicyValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/AddPolicyValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not add Policy Value. Received %s: %s.' %(result.code, result.config_result))
            self.logger.log('Successfully added Policy value.')

        def post(self, object_dn, attribute_name, class_name, value, locked):
            body = json.dumps({
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'ClassName': class_name,
                'Value': value,
                'Locked': locked
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _AddValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/AddValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not add Value. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully added Value.')

        def post(self, object_dn, attribute_name, value):
            body = json.dumps({
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value,
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ClearAttribute(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ClearAttribute',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not clear Attribute. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully cleared Attribute.')

        def post(self, object_dn, attribute_name):
            body = json.dumps({
                'ObjectDN': object_dn,
                'AttributeName': attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ClearPolicyAttribute(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ClearPolicyAttribute',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not clear Policy Attribute. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully cleared Policy Attribute.')

        def post(self, object_dn, class_name, attribute_name):
            body = json.dumps({
                'ObjectDN': object_dn,
                'Class': class_name,
                'AttributeName': attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _ContainableClasses(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ContainableClasses',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def class_names(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('ClassNames', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not retrieve names of container classes. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully retrieved containing classes.')

        def post(self, object_dn):
            body = json.dumps({
                'ObjectDN': object_dn
            })
            self.response = self._session.post(url=self._url, data=body)
            return self

    class _CountObjects(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/CountObjects',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def count(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Count'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could get a count of the objects. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully counted the objects.')

        def post(self, object_dn, type, recursive, pattern):
            body = json.dumps({
                'ObjectDN': object_dn,
                'Type': type,
                'Pattern': pattern
            })
            if recursive:
                body.update({'Recursive': recursive})

            self.response = self._session.post(url=self._url, data=body)
            return self

    class _Create(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Create',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Object'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not create config object. Received %s: %s.' %(result.code, result.config_result))
            return result

        def post(self, object_dn, class_name, name_attribute_list):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Class": class_name,
                "NameAttributeList": name_attribute_list
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _DefaultDN(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/DefaultDN',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def default_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('DefaultDN'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could get the default DN. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully retrieved the Default DN.')

        def post(self, default_dn):
            body = json.dumps({
                'DefaultDN': default_dn
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Delete(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Delete',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not delete config object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, recursive):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Recursive": recursive
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _FindObjectsOfClass(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/FindObjectsOfClass',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Objects', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find config object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, classes=None, class_name=None, object_dn=None, pattern=None, recursive=None):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = json.dumps({
                "Classes": classes,
                "Class": class_name,
            })
            if object_dn:
                body.update({'ObjectDN': object_dn})
            if pattern:
                body.update({'Pattern': pattern})
            if recursive:
                body.update({'Recursive': recursive})

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _FindPolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/FindPolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def locked(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Locked'), self._api_type)

        @property
        @response_property()
        def policy_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('PolicyDN'), self._api_type)

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the policy object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, class_name, attribute_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _GetHighestRevision(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/GetHighestRevision',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Revision'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the revision of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, classes=None):
            body = json.dumps({
                "ObjectDN": object_dn
            })
            if classes:
                body.update({'Classes': classes})

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _GetRevision(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/GetRevision',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Revision'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the revision of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn):
            body = json.dumps({
                "ObjectDN": object_dn
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _GuidToDn(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/GuidToDn',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('ObjectDN'), self._api_type)

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('ClassName'), self._api_type)

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Revision'), self._api_type)

        @property
        @response_property()
        def hierarchical_guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('HierarchicalGUID'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the GUID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_guid):
            body = json.dumps({
                "ObjectGUID": object_guid
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _IdInfo(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/IdInfo',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('GUID'), self._api_type)

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('ClassName'), self._api_type)

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Revision'), self._api_type)

        @property
        @response_property()
        def hierarchical_guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('HierarchicalGUID'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the given ID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_id):
            body = json.dumps({
                "ObjectID": object_id
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _IsValid(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/IsValid',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Object', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the GUID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, object_guid):
            if not (object_dn or object_guid):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = json.dumps({
                "ObjectGUID": object_guid,
                "ObjectDN": object_dn
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _MutateObject(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/MutateObject',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not mutate the object to the specified class. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, class_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Class": class_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Read(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Read',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def object_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('ObjectDN'), self._api_type)

        @property
        @response_property()
        def attribute_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('AttributeName'), self._api_type)

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object and attribute name combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ReadAll(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ReadAll',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def name_values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('NameValues', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn):
            body = json.dumps({
                "ObjectDN": object_dn
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ReadDn(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ReadDn',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ReadDnReferences(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ReadDnReferences',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, reference_attribute_name, attribute_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName": attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ReadEffectivePolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ReadEffectivePolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def locked(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Locked'), self._api_type)

        @property
        @response_property()
        def overridden(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Overridden'), self._api_type)

        @property
        @response_property()
        def policy_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('PolicyDN'), self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError(
                    'Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (
                    result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _ReadPolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/ReadPolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def locked(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('Locked'), self._api_type)

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return Config.Object(result.get('ClassName'), self._api_type)

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Object(obj, self._api_type) for obj in result.get('Values', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could read the policy for the given object, attribute_name and class. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name, class_name):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name
            })

            self.response = self._session.post(url=self._url, data=body)

            return self

    class _RemoveDnValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/RemoveDnValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not remove the value of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name, value):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Value": value
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _RemovePolicyValue(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/RemovePolicyValue',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not remove the policy value of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name, class_name, value):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "ClassName": class_name,
                "Value": value
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _RenameObject(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/RenameObject',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not rename the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, new_object_dn):
            body = json.dumps({
                "ObjectDN": object_dn,
                "NewObjectDN": new_object_dn
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Write(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Write',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not write the attribute data to the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_data):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeData": attribute_data
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _WriteDn(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/WriteDn',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not write the attribute data to the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, attribute_name, values):
            body = json.dumps({
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Values": values
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _WritePolicy(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/WritePolicy',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not write the attribute values for the given class. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn, class_name, attribute_name, locked, values):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name,
                "Locked": locked,
                "Values": values
            })
            self.response = self._session.post(url=self._url, data=body)

            return self
