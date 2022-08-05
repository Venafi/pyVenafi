from typing import Dict, List
from pytpp.api.api_base import API, APIResponse, ResponseFactory, ResponseField
from pytpp.properties.response_objects.dataclasses import config


class _Config:
    def __init__(self, api_obj):
        self.AddDnValue = self._AddDnValue(api_obj=api_obj)
        self.AddPolicyValue = self._AddPolicyValue(api_obj=api_obj)
        self.AddValue = self._AddValue(api_obj=api_obj)
        self.ClearAttribute = self._ClearAttribute(api_obj=api_obj)
        self.ClearPolicyAttribute = self._ClearPolicyAttribute(api_obj=api_obj)
        self.ContainableClasses = self._ContainableClasses(api_obj=api_obj)
        self.Create = self._Create(api_obj=api_obj)
        self.DefaultDN = self._DefaultDN(api_obj=api_obj)
        self.Delete = self._Delete(api_obj=api_obj)
        self.DnToGuid = self._DnToGuid(api_obj=api_obj)
        self.Enumerate = self._Enumerate(api_obj=api_obj)
        self.EnumerateAll = self._EnumerateAll(api_obj=api_obj)
        self.EnumerateObjectsDerivedFrom = self._EnumerateObjectsDerivedFrom(api_obj=api_obj)
        self.EnumeratePolicies = self._EnumeratePolicies(api_obj=api_obj)
        self.Find = self._Find(api_obj=api_obj)
        self.FindObjectsOfClass = self._FindObjectsOfClass(api_obj=api_obj)
        self.FindPolicy = self._FindPolicy(api_obj=api_obj)
        self.GetHighestRevision = self._GetHighestRevision(api_obj=api_obj)
        self.GetRevision = self._GetRevision(api_obj=api_obj)
        self.GuidToDn = self._GuidToDn(api_obj=api_obj)
        self.IdInfo = self._IdInfo(api_obj=api_obj)
        self.IsValid = self._IsValid(api_obj=api_obj)
        self.MutateObject = self._MutateObject(api_obj=api_obj)
        self.Read = self._Read(api_obj=api_obj)
        self.ReadAll = self._ReadAll(api_obj=api_obj)
        self.ReadDn = self._ReadDn(api_obj=api_obj)
        self.ReadDnReferences = self._ReadDnReferences(api_obj=api_obj)
        self.ReadEffectivePolicy = self._ReadEffectivePolicy(api_obj=api_obj)
        self.ReadPolicy = self._ReadPolicy(api_obj=api_obj)
        self.RemoveDnValue = self._RemoveDnValue(api_obj=api_obj)
        self.RemovePolicyValue = self._RemovePolicyValue(api_obj=api_obj)
        self.RenameObject = self._RenameObject(api_obj=api_obj)
        self.Write = self._Write(api_obj=api_obj)
        self.WriteDn = self._WriteDn(api_obj=api_obj)
        self.WritePolicy = self._WritePolicy(api_obj=api_obj)

    class _AddDnValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _AddPolicyValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddPolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Class'        : class_name,
                'Value'        : value,
                'Locked'       : locked
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _AddValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value,
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ClearAttribute(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearAttribute')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ClearPolicyAttribute(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearPolicyAttribute')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'Class'        : class_name,
                'AttributeName': attribute_name
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ContainableClasses(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ContainableClasses')

        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }

            class Response(APIResponse):
                class_names: List[str] = ResponseField(alias='ClassNames', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _CountObjects(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/CountObjects')

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN' : object_dn,
                'Type'     : type_name,
                'Pattern'  : pattern,
                'Recursive': recursive
            }

            class Response(APIResponse):
                count: int = ResponseField(alias='Count')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Create(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Create')

        def post(self, object_dn: str, class_name: str, name_attribute_list: list):
            body = {
                "ObjectDN"         : object_dn,
                "Class"            : class_name,
                "NameAttributeList": name_attribute_list
            }

            class Response(APIResponse):
                object: config.Object = ResponseField(alias='Object')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _DefaultDN(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DefaultDN')

        def get(self):
            class Response(APIResponse):
                default_dn: str = ResponseField(alias='DefaultDN')
                result: int = ResponseField(alias='Result')

            return ResponseFactory(response=self._get(), response_cls=Response)

    class _Delete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Delete')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _DnToGuid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DnToGuid')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }

            class Response(APIResponse):
                class_name: str = ResponseField(alias='ClassName')
                guid: str = ResponseField(alias='GUID')
                revision: str = ResponseField(alias='Revision')
                hierarchical_guid: str = ResponseField(alias='HierarchicalGUID')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Enumerate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Enumerate')

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive,
                "Pattern"  : pattern
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _EnumerateAll(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateAll')

        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _EnumerateObjectsDerivedFrom(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateObjectsDerivedFrom')

        def post(self, derived_from: str, pattern: str = None):
            body = {
                "DerivedFrom": derived_from,
                "Pattern"    : pattern
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _EnumeratePolicies(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumeratePolicies')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(APIResponse):
                policies: List[config.Policy] = ResponseField(alias='Policies', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Find(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Find')

        def post(self, pattern: str, attribute_names: List[str] = None):
            body = {
                "Pattern"       : pattern,
                "AttributeNames": attribute_names
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _FindContainers(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindContainers')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _FindObjectsOfClass(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindObjectsOfClass')

        def post(self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None,
                 recursive: bool = False):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes"  : classes,
                "Class"    : class_name,
                'ObjectDN' : object_dn,
                'Pattern'  : pattern,
                'Recursive': recursive
            }

            class Response(APIResponse):
                object: List[config.Object] = ResponseField(alias='Object', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _FindPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindPolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "Class"        : class_name,
                "AttributeName": attribute_name
            }

            class Response(APIResponse):
                locked: bool = ResponseField(alias='Locked')
                policy_dn: str = ResponseField(alias='PolicyDN')
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _GetHighestRevision(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetHighestRevision')

        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn,
                'Classes' : classes
            }

            class Response(APIResponse):
                revision: int = ResponseField(alias='Revision')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _GetRevision(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetRevision')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(APIResponse):
                revision: int = ResponseField(alias='Revision')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _GuidToDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GuidToDn')

        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            class Response(APIResponse):
                object_dn: str = ResponseField(alias='ObjectDN')
                class_name: str = ResponseField(alias='ClassName')
                revision: str = ResponseField(alias='Revision')
                hierarchical_guid: str = ResponseField(alias='HierarchicalGUID')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _IdInfo(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IdInfo')

        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            class Response(APIResponse):
                guid: str = ResponseField(alias='GUID')
                class_name: str = ResponseField(alias='ClassName')
                revision: str = ResponseField(alias='Revision')
                hierarchical_guid: str = ResponseField(alias='HierarchicalGUID')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _IsValid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IsValid')

        def post(self, object_dn: str = None, object_guid: str = None):
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN"  : object_dn
            }

            class Response(APIResponse):
                object: config.Object = ResponseField(alias='Object')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _MutateObject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/MutateObject')

        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class"   : class_name
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Read(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Read')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(APIResponse):
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ReadAll(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadAll')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(APIResponse):
                name_values: List[config.NameValues[str]] = ResponseField(alias='NameValues', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ReadDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDn')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(APIResponse):
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ReadDnReferences(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDnReferences')

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN"              : object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName"         : attribute_name
            }

            class Response(APIResponse):
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ReadEffectivePolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadEffectivePolicy')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(APIResponse):
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                locked: bool = ResponseField(alias='Locked')
                overridden: bool = ResponseField(alias='Overridden')
                policy_dn: str = ResponseField(alias='PolicyDN')
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _ReadPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadPolicy')

        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name
            }

            class Response(APIResponse):
                locked: bool = ResponseField(alias='Locked')
                values: List[str] = ResponseField(alias='Values', default_factory=list)
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _RemoveDnValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemoveDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Value"        : value
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _RemovePolicyValue(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemovePolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name,
                "Value"        : value
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _RenameObject(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RenameObject')

        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN"   : object_dn,
                "NewObjectDN": new_object_dn
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _Write(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Write')

        def post(self, object_dn: str, attribute_data: List[Dict[str, List[str]]]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeData": attribute_data
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _WriteDn(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/WriteDn')

        def post(self, object_dn: str, attribute_name: str, values: List[str]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Values"       : values
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)

    class _WritePolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/WritePolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str, locked: bool = False, values: List[str] = None):
            body = {
                "ObjectDN"     : object_dn,
                "Class"        : class_name,
                "AttributeName": attribute_name,
                "Locked"       : locked,
                "Values"       : values
            }

            class Response(APIResponse):
                result: config.Result = ResponseField(alias='Result', converter=lambda x: config.Result(code=x))

            return ResponseFactory(response=self._post(data=body), response_cls=Response)
