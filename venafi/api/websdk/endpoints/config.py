from typing import List 
from venafi.api.api_base import API, json_response_property
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
            super().__init__(api_obj=websdk_obj, url='/Config/AddDnValue', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value
            }

            self.json_response = self._post(data=body)
            return self

    class _AddPolicyValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/AddPolicyValue', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Class': class_name,
                'Value': value,
                'Locked': locked
            }

            self.json_response = self._post(data=body)
            return self

    class _AddValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/AddValue', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name,
                'Value': value,
            }

            self.json_response = self._post(data=body)
            return self

    class _ClearAttribute(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ClearAttribute', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'AttributeName': attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ClearPolicyAttribute(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ClearPolicyAttribute', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN': object_dn,
                'Class': class_name,
                'AttributeName': attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ContainableClasses(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ContainableClasses', valid_return_codes=[200])

        @property
        @json_response_property()
        def class_names(self) -> List[str]:
            return self._from_json(key='ClassNames')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }
            self.json_response = self._post(data=body)
            return self

    class _CountObjects(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/CountObjects', valid_return_codes=[200])

        @property
        @json_response_property()
        def count(self) -> int:
            return self._from_json(key='Count')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN': object_dn,
                'Type': type_name,
                'Pattern': pattern
            }
            if recursive:
                body.update({'Recursive': recursive})

            self.json_response = self._post(data=body)
            return self

    class _Create(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Create', valid_return_codes=[200])

        @property
        @json_response_property()
        def object(self):
            return Config.Object(self._from_json(key='Object'), self._api_type)

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, class_name: str, name_attribute_list: list):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "NameAttributeList": name_attribute_list
            }

            self.json_response = self._post(data=body)
            return self

    class _DefaultDN(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/DefaultDN', valid_return_codes=[200])

        @property
        @json_response_property()
        def default_dn(self) -> str:
            return self._from_json(key='DefaultDN')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, default_dn: str):
            body = {
                'DefaultDN': default_dn
            }
            self.json_response = self._post(data=body)
            return self

    class _Delete(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Delete', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }
            self.json_response = self._post(data=body)
            return self

    class _DnToGuid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/DnToGuid', valid_return_codes=[200])

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

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }
            self.json_response = self._post(data=body)
            return self

    class _Enumerate(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Enumerate', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive,
                "Pattern": pattern
            }
            self.json_response = self._post(data=body)
            return self

    class _EnumerateAll(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumerateAll', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }
            self.json_response = self._post(data=body)
            return self

    class _EnumerateObjectsDerivedFrom(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumerateObjectsDerivedFrom', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, derived_from: str, pattern: str = None, object_dn: str = None):
            body = {
                "ObjectDN": object_dn,
                "DerivedFrom": derived_from,
                "Pattern": pattern
            }
            self.json_response = self._post(data=body)
            return self

    class _EnumeratePolicies(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/EnumeratePolicies', valid_return_codes=[200])

        @property
        @json_response_property()
        def policies(self):
            return [Config.Policy(obj, self._api_type) for obj in self._from_json(key='Policies')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }
            self.json_response = self._post(data=body)
            return self

    class _Find(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Find', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, pattern: str, attribute_names: str = None):
            body = {
                "Pattern": pattern,
                "AttributeNames": attribute_names
            }
            self.json_response = self._post(data=body)
            return self

    class _FindContainers(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindContainers', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN": object_dn,
                "Recursive": recursive
            }
            self.json_response = self._post(data=body)
            return self

    class _FindObjectsOfClass(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindObjectsOfClass', valid_return_codes=[200])

        @property
        @json_response_property()
        def objects(self):
            return [Config.Object(obj, self._api_type) for obj in self._from_json(key='Objects')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None, recursive: bool = False):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes": classes,
                "Class": class_name,
            }
            if object_dn:
                body.update({'ObjectDN': object_dn})
            if pattern:
                body.update({'Pattern': pattern})
            if recursive:
                body.update({'Recursive': recursive})

            self.json_response = self._post(data=body)
            return self

    class _FindPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/FindPolicy', valid_return_codes=[200])

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

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _GetHighestRevision(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GetHighestRevision', valid_return_codes=[200])

        @property
        @json_response_property()
        def revision(self) -> str:
            return self._from_json(key='Revision')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn
            }
            if classes:
                body.update({'Classes': classes})

            self.json_response = self._post(data=body)
            return self

    class _GetRevision(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GetRevision', valid_return_codes=[200])

        @property
        @json_response_property()
        def revision(self) -> str:
            return self._from_json(key='Revision')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            self.json_response = self._post(data=body)
            return self

    class _GuidToDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/GuidToDn', valid_return_codes=[200])

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

        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            self.json_response = self._post(data=body)
            return self

    class _IdInfo(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/IdInfo', valid_return_codes=[200])

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

        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            self.json_response = self._post(data=body)
            return self

    class _IsValid(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/IsValid', valid_return_codes=[200])

        @property
        @json_response_property()
        def object(self):
            return Config.Object(self._from_json(key='Object'), self._api_type)

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str = None, object_guid: str = None):
            if not (object_dn or object_guid):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN": object_dn
            }

            self.json_response = self._post(data=body)
            return self

    class _MutateObject(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/MutateObject', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name
            }

            self.json_response = self._post(data=body)
            return self

    class _Read(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Read', valid_return_codes=[200])

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

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ReadAll(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadAll', valid_return_codes=[200])

        @property
        @json_response_property()
        def name_values(self):
            return [Config.NameValues(nv, self._api_type) for nv in self._from_json(key='NameValues')]

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            self.json_response = self._post(data=body)
            return self

    class _ReadDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadDn', valid_return_codes=[200])

        @property
        @json_response_property()
        def values(self) -> List[str]:
            return self._from_json(key='Values')

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ReadDnReferences(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadDnReferences', valid_return_codes=[200])

        @property
        @json_response_property()
        def values(self) -> List[str]:
            return self._from_json(key='Values', return_on_error=list)

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName": attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ReadEffectivePolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadEffectivePolicy', valid_return_codes=[200])

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

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name
            }

            self.json_response = self._post(data=body)
            return self

    class _ReadPolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/ReadPolicy', valid_return_codes=[200])

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

        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name
            }

            self.json_response = self._post(data=body)
            return self

    class _RemoveDnValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RemoveDnValue', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Value": value
            }
            self.json_response = self._post(data=body)
            return self

    class _RemovePolicyValue(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RemovePolicyValue', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Class": class_name,
                "Value": value
            }
            self.json_response = self._post(data=body)
            return self

    class _RenameObject(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/RenameObject', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN": object_dn,
                "NewObjectDN": new_object_dn
            }
            self.json_response = self._post(data=body)
            return self

    class _Write(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/Write', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_data: dict):
            body = {
                "ObjectDN": object_dn,
                "AttributeData": attribute_data
            }
            self.json_response = self._post(data=body)
            return self

    class _WriteDn(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/WriteDn', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, attribute_name: str, values: str):
            body = {
                "ObjectDN": object_dn,
                "AttributeName": attribute_name,
                "Values": values
            }
            self.json_response = self._post(data=body)
            return self

    class _WritePolicy(API):
        def __init__(self, websdk_obj):
            super().__init__(api_obj=websdk_obj, url='/Config/WritePolicy', valid_return_codes=[200])

        @property
        @json_response_property()
        def result(self):
            return Config.Result(self._from_json(key='Result'))

        def post(self, object_dn: str, class_name: str, attribute_name: str, locked: bool = False, values: str = None):
            body = {
                "ObjectDN": object_dn,
                "Class": class_name,
                "AttributeName": attribute_name,
                "Locked": locked,
                "Values": values
            }
            self.json_response = self._post(data=body)
            return self