import json
from apilibs.base import API, response_property
from apilibs.session import WEBSDK_URL
from objects.response_objects.config import Config


class _Config:
    def __init__(self, session, api_type):
        self.AddDnValue = self._AddDnValue(session, api_type)
        self.AddPolicyValue = self._AddPolicyValue(session, api_type)
        self.AddValue = self._AddValue(session, api_type)
        self.ClearAttribute = self._ClearAttribute(session, api_type)
        self.ClearPolicyAttribute = self._ClearPolicyAttribute(session, api_type)
        self.ContainableClasses = self._ContainableClasses(session, api_type)
        self.Create = self._Create(session, api_type)
        self.DefaultDN = self._DefaultDN(session, api_type)
        self.Delete = self._Delete(session, api_type)
        self.DnToGuid = self._DnToGuid(session, api_type)
        self.Enumerate = self._Enumerate(session, api_type)
        self.EnumerateAll = self._EnumerateAll(session, api_type)
        self.EnumerateObjectsDerivedFrom = self._EnumerateObjectsDerivedFrom(session, api_type)
        self.EnumeratePolicies = self._EnumeratePolicies(session, api_type)
        self.FindObjectsOfClass = self._FindObjectsOfClass(session, api_type)
        self.FindPolicy = self._FindPolicy(session, api_type)
        self.GetHighestRevision = self._GetHighestRevision(session, api_type)
        self.GetRevision = self._GetRevision(session, api_type)
        self.GuidToDn = self._GuidToDn(session, api_type)
        self.IdInfo = self._IdInfo(session, api_type)
        self.IsValid = self._IsValid(session, api_type)
        self.MutateObject = self._MutateObject(session, api_type)
        self.Read = self._Read(session, api_type)
        self.ReadAll = self._ReadAll(session, api_type)
        self.ReadDn = self._ReadDn(session, api_type)
        self.ReadDnReferences = self._ReadDnReferences(session, api_type)
        self.ReadEffectivePolicy = self._ReadEffectivePolicy(session, api_type)
        self.ReadPolicy = self._ReadPolicy(session, api_type)
        self.RemoveDnValue = self._RemoveDnValue(session, api_type)
        self.RemovePolicyValue = self._RemovePolicyValue(session, api_type)
        self.RenameObject = self._RenameObject(session, api_type)
        self.Write = self._Write(session, api_type)
        self.WriteDn = self._WriteDn(session, api_type)
        self.WritePolicy = self._WritePolicy(session, api_type)

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

        def post(self, object_dn: str, attribute_name: str, value: str):
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
            return result

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
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

            return result

        def post(self, object_dn: str, attribute_name: str, value: str):
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
            return result

        def post(self, object_dn: str, attribute_name: str):
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
            return result

        def post(self, object_dn: str, class_name: str, attribute_name: str):
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
            return self.response.json()['ClassNames']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not retrieve names of container classes. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully retrieved containing classes.')

        def post(self, object_dn: str):
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
            return self.response.json()['Count']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could get a count of the objects. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully counted the objects.')

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = json.dumps({
                'ObjectDN': object_dn,
                'Type': type_name,
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

        def post(self, object_dn: str, class_name: str, name_attribute_list: str):
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
            return self.response.json()['DefaultDN']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not get the default DN. Received %s: %s.' % (result.code, result.config_result))
            self.logger.log('Successfully retrieved the Default DN.')

        def post(self, default_dn: str):
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

        def post(self, object_dn: str, recursive: bool = False):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Recursive": recursive
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _DnToGuid(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/DnToGuid',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['ClassName']

        @property
        @response_property()
        def guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['GUID']

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['Revision']

        @property
        @response_property()
        def hierarchical_guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['HierarchicalGUID']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not convert the given DN. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str):
            body = json.dumps({
                "ObjectDN": object_dn,
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Enumerate(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Enumerate',
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

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Recursive": recursive,
                "Pattern": pattern
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _EnumerateAll(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/EnumerateAll',
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
                raise ValueError('Could not find config objects. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, pattern: str):
            body = json.dumps({
                "Pattern": pattern
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _EnumerateObjectsDerivedFrom(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/EnumerateObjectsDerivedFrom',
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
                raise ValueError('Could not find config objects. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, derived_from: str, pattern: str = None):
            body = json.dumps({
                "DerivedFrom": derived_from,
                "Pattern": pattern
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _EnumeratePolicies(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/EnumeratePolicies',
                valid_return_codes=[200]
            )

        @property
        @response_property()
        def policies(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return [Config.Policies(obj, self._api_type) for obj in result.get('Policies', [])]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find config objects. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str):
            body = json.dumps({
                "ObjectDN": object_dn
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _Find(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/Find',
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
                raise ValueError('Could not find config objects. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, pattern: str, attribute_names: str = None):
            body = json.dumps({
                "Pattern": pattern,
                "AttributeNames": attribute_names
            })
            self.response = self._session.post(url=self._url, data=body)

            return self

    class _FindContainers(API):
        def __init__(self, session, api_type):
            super().__init__(
                session=session,
                api_type=api_type,
                url=WEBSDK_URL + '/Config/FindContainers',
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
                raise ValueError('Could not find config objects. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, recursive: bool = False):
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

        def post(self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None, recursive: bool = False):
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
            return self.response.json()['Locked']

        @property
        @response_property()
        def policy_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['PolicyDN']

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['Values']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the policy object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, class_name: str, attribute_name: str):
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
            return self.response.json()['Revision']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the revision of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, classes: str = None):
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
            return self.response.json()['Revision']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the revision of the object. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str):
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
            return self.response.json()['ObjectDN']

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
                return self.response.json()['ClassName']

        @property
        @response_property()
        def revision(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
                return self.response.json()['Revision']

        @property
        @response_property()
        def hierarchical_guid(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
                return self.response.json()['HierarchicalGUID']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the GUID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_guid: str):
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
            return self.response.json()['GUID']

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['ClassName']

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
            return self.response.json()['HierarchacalGUID']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the given ID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_id: str):
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
            return Config.Object(result['Object'], self._api_type)

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the GUID. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, object_guid: str):
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

        def post(self, object_dn: str, class_name: str):
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
            return self.response.json()['ObjectDN']

        @property
        @response_property()
        def attribute_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['AttributeName']

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
                return self.response.json()['Values']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object and attribute name combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, attribute_name: str):
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
            return [Config.NameValue(name, value) for name, value in self.response.json()['NameValues'].items()]

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str):
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
            return self.response.json()['Values']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, attribute_name: str):
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
            return self.response.json('Values')

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
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
            return self.response.json()['Values']

        @property
        @response_property()
        def locked(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['Locked']

        @property
        @response_property()
        def overridden(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['Overridden']

        @property
        @response_property()
        def policy_dn(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['PolicyDN']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError(
                    'Could not find the information for the object_dn and attribute combination. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, attribute_name: str):
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
            return self.response.json()['Locked']

        @property
        @response_property()
        def class_name(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
                return self.response.json()['ClassName']

        @property
        @response_property()
        def values(self):
            result = self.response.json()
            if 'Error' in result.keys():
                raise AssertionError('An error occurred: "%s"' % result['Error'])
            return self.response.json()['Values']

        @property
        @response_property()
        def result(self):
            code = self.response.json()['Result']
            result = Config.Result(code)
            if result.code != 1:
                raise ValueError('Could read the policy for the given object, attribute_name and class. Received %s: %s.' % (result.code, result.config_result))
            return result

        def post(self, object_dn: str, attribute_name: str, class_name: str):
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

        def post(self, object_dn: str, attribute_name: str, value: str):
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

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
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

        def post(self, object_dn: str, new_object_dn: str):
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

        def post(self, object_dn: str, attribute_data: str):
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

        def post(self, object_dn: str, attribute_name: str, values: str):
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

        def post(self, object_dn: str, class_name: str, attribute_name: str, locked: bool = False, values: str = None):
            body = json.dumps({
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name,
                "Locked": locked,
                "Values": values
            })
            self.response = self._session.post(url=self._url, data=body)

            return self
