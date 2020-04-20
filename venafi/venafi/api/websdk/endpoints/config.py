from typing import List 
from venafi.api.api_base import API, APIResponse, json_response_property
from venafi.properties.response_objects.config import Config


class _Config:
    def __init__(self, websdk_obj):
        self.AddDnValue = self._AddDnValue(websdk_obj=websdk_obj)
        self.AddPolicyValue = self._AddPolicyValue(websdk_obj=websdk_obj)
        self.AddValue = self._AddValue(websdk_obj=websdk_obj)
        self.ClearAttribute = self._ClearAttribute(websdk_obj=websdk_obj)
        self.ClearPolicyAttribute = self._ClearPolicyAttribute(websdk_obj=websdk_obj)
        self.ContainableClasses = self._ContainableClasses(websdk_obj=websdk_obj)
        self.Create = self._Create(websdk_obj=websdk_obj)
        self.DefaultDN = self._DefaultDN(websdk_obj=websdk_obj)
        self.Delete = self._Delete(websdk_obj=websdk_obj)
        self.DnToGuid = self._DnToGuid(websdk_obj=websdk_obj)
        self.Enumerate = self._Enumerate(websdk_obj=websdk_obj)
        self.EnumerateAll = self._EnumerateAll(websdk_obj=websdk_obj)
        self.EnumerateObjectsDerivedFrom = self._EnumerateObjectsDerivedFrom(websdk_obj=websdk_obj)
        self.EnumeratePolicies = self._EnumeratePolicies(websdk_obj=websdk_obj)
        self.Find = self._Find(websdk_obj=websdk_obj)
        self.FindObjectsOfClass = self._FindObjectsOfClass(websdk_obj=websdk_obj)
        self.FindPolicy = self._FindPolicy(websdk_obj=websdk_obj)
        self.GetHighestRevision = self._GetHighestRevision(websdk_obj=websdk_obj)
        self.GetRevision = self._GetRevision(websdk_obj=websdk_obj)
        self.GuidToDn = self._GuidToDn(websdk_obj=websdk_obj)
        self.IdInfo = self._IdInfo(websdk_obj=websdk_obj)
        self.IsValid = self._IsValid(websdk_obj=websdk_obj)
        self.MutateObject = self._MutateObject(websdk_obj=websdk_obj)
        self.Read = self._Read(websdk_obj=websdk_obj)
        self.ReadAll = self._ReadAll(websdk_obj=websdk_obj)
        self.ReadDn = self._ReadDn(websdk_obj=websdk_obj)
        self.ReadDnReferences = self._ReadDnReferences(websdk_obj=websdk_obj)
        self.ReadEffectivePolicy = self._ReadEffectivePolicy(websdk_obj=websdk_obj)
        self.ReadPolicy = self._ReadPolicy(websdk_obj=websdk_obj)
        self.RemoveDnValue = self._RemoveDnValue(websdk_obj=websdk_obj)
        self.RemovePolicyValue = self._RemovePolicyValue(websdk_obj=websdk_obj)
        self.RenameObject = self._RenameObject(websdk_obj=websdk_obj)
        self.Write = self._Write(websdk_obj=websdk_obj)
        self.WriteDn = self._WriteDn(websdk_obj=websdk_obj)
        self.WritePolicy = self._WritePolicy(websdk_obj=websdk_obj)

    class _AddDnValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/AddDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
                    
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _AddPolicyValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/AddPolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Class': class_name,
                'Value': value,
                'Locked': locked
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _AddValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/AddValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value,
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ClearAttribute(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ClearAttribute')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ClearPolicyAttribute(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ClearPolicyAttribute')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'Class': class_name,
                'AttributeName': attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ContainableClasses(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ContainableClasses')

        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def class_names(self) -> List[str]:
                    return self._from_json(key='ClassNames')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _CountObjects(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/CountObjects')

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN': object_dn,
                'Type': type_name,
                'Pattern': pattern,
                'Recursive': recursive
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def count(self) -> int:
                    return self._from_json(key='Count')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Create(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Create')

        def post(self, object_dn: str, class_name: str, name_attribute_list: list):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "NameAttributeList": name_attribute_list
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def object(self):
                    return Config.Object(self._from_json(key='Object'), self._api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _DefaultDN(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/DefaultDN')

        def post(self, default_dn: str):
            body = {
                'DefaultDN': default_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def default_dn(self) -> str:
                    return self._from_json(key='DefaultDN')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Delete')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _DnToGuid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/DnToGuid')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='GUID')

                @property
                @json_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @json_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Enumerate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Enumerate')

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive,
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _EnumerateAll(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumerateAll')

        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _EnumerateObjectsDerivedFrom(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumerateObjectsDerivedFrom')

        def post(self, derived_from: str, pattern: str = None, object_dn: str = None):
            body = {
                "ObjectDN": object_dn,
                "DerivedFrom": derived_from,
                "Pattern": pattern
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _EnumeratePolicies(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumeratePolicies')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def policies(self):
                    return [Config.Policy(obj, self._api_source) for obj in self._from_json(key='Policies')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Find(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Find')

        def post(self, pattern: str, attribute_names: str = None):
            body = {
                "Pattern": pattern,
                "AttributeNames": attribute_names
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _FindContainers(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindContainers')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _FindObjectsOfClass(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindObjectsOfClass')

        def post(self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None, recursive: bool = False):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes": classes,
                "Class": class_name,
                'ObjectDN': object_dn,
                'Pattern': pattern,
                'Recursive': recursive
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def objects(self):
                    return [Config.Object(obj, self._api_source) for obj in self._from_json(key='Objects')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _FindPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindPolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @json_response_property()
                def policy_dn(self) -> str:
                    return self._from_json(key='PolicyDN')

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetHighestRevision(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GetHighestRevision')

        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn,
                'Classes': classes
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GetRevision(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GetRevision')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _GuidToDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GuidToDn')

        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def object_dn(self) -> str:
                    return self._from_json(key='ObjectDN')

                @property
                @json_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @json_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @json_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _IdInfo(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/IdInfo')

        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def guid(self) -> str:
                    return self._from_json(key='GUID')

                @property
                @json_response_property()
                def class_name(self) -> str:
                    return self._from_json(key='ClassName')

                @property
                @json_response_property()
                def revision(self) -> str:
                    return self._from_json(key='Revision')

                @property
                @json_response_property()
                def hierarchical_guid(self) -> str:
                    return self._from_json(key='HierarchicalGUID')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _IsValid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/IsValid')

        def post(self, object_dn: str = None, object_guid: str = None):
            if not (object_dn or object_guid):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def object(self):
                    return Config.Object(self._from_json(key='Object'), self._api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _MutateObject(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/MutateObject')

        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Read(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Read')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def object_dn(self) -> str:
                    return self._from_json(key='ObjectDN')

                @property
                @json_response_property()
                def attribute_name(self) -> str:
                    return self._from_json(key='AttributeName')

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ReadAll(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadAll')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def name_values(self):
                    return [Config.NameValues(nv, self._api_source) for nv in self._from_json(key='NameValues')]

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ReadDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadDn')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ReadDnReferences(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadDnReferences')

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values', return_on_error=list)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ReadEffectivePolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadEffectivePolicy')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values')

                @property
                @json_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @json_response_property()
                def overridden(self) -> bool:
                    return self._from_json(key='Overridden')

                @property
                @json_response_property()
                def policy_dn(self) -> str:
                    return self._from_json(key='PolicyDN')

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _ReadPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadPolicy')

        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def locked(self) -> bool:
                    return self._from_json(key='Locked')

                @property
                @json_response_property()
                def values(self) -> List[str]:
                    return self._from_json(key='Values', return_on_error=list)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _RemoveDnValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RemoveDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Value": value
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))                    
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _RemovePolicyValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RemovePolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name,
                "Value": value
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _RenameObject(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RenameObject')

        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN": object_dn,
                "NewObjectDN": new_object_dn
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))

            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _Write(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Write')

        def post(self, object_dn: str, attribute_data: dict):
            body = {
                "ObjectDN": object_dn,
                "AttributeData": attribute_data
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _WriteDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/WriteDn')

        def post(self, object_dn: str, attribute_name: str, values: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Values": values
            }

            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )

    class _WritePolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/WritePolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str, locked: bool = False, values: str = None):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name,
                "Locked": locked,
                "Values": values
            }
            
            class _Response(APIResponse):
                def __init__(self, response, expected_return_codes, api_source):
                    super().__init__(response=response, expected_return_codes=expected_return_codes, api_source=api_source)

                @property
                @json_response_property()
                def result(self):
                    return Config.Result(self._from_json(key='Result'))
            
            return _Response(
                response=self._post(data=body),
                expected_return_codes=[200],
                api_source=self._api_source
            )
