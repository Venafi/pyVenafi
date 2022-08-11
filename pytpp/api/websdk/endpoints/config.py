from typing import Dict, List
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from pytpp.api.websdk.outputs import config


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

    class _AddDnValue(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _AddPolicyValue(WebSdkEndpoint):
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

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _AddValue(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/AddValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value,
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ClearAttribute(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearAttribute')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ClearPolicyAttribute(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ClearPolicyAttribute')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'Class'        : class_name,
                'AttributeName': attribute_name
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ContainableClasses(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ContainableClasses')

        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }

            class Response(WebSdkOutputModel):
                class_names: List[str] = ApiField(alias='ClassNames', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _CountObjects(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/CountObjects')

        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN' : object_dn,
                'Type'     : type_name,
                'Pattern'  : pattern,
                'Recursive': recursive
            }

            class Response(WebSdkOutputModel):
                count: int = ApiField(alias='Count')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Create(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Create')

        def post(self, object_dn: str, class_name: str, name_attribute_list: list):
            body = {
                "ObjectDN"         : object_dn,
                "Class"            : class_name,
                "NameAttributeList": name_attribute_list
            }

            class Response(WebSdkOutputModel):
                object: config.Object = ApiField(alias='Object')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _DefaultDN(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DefaultDN')

        def get(self):
            class Response(WebSdkOutputModel):
                default_dn: str = ApiField(alias='DefaultDN')
                result: int = ApiField(alias='Result')

            return generate_output(response=self._get(), response_cls=Response)

    class _Delete(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Delete')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _DnToGuid(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/DnToGuid')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }

            class Response(WebSdkOutputModel):
                class_name: str = ApiField(alias='ClassName')
                guid: str = ApiField(alias='GUID')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Enumerate(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Enumerate')

        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive,
                "Pattern"  : pattern
            }

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _EnumerateAll(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateAll')

        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _EnumerateObjectsDerivedFrom(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumerateObjectsDerivedFrom')

        def post(self, derived_from: str, pattern: str = None):
            body = {
                "DerivedFrom": derived_from,
                "Pattern"    : pattern
            }

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _EnumeratePolicies(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/EnumeratePolicies')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(WebSdkOutputModel):
                policies: List[config.Policy] = ApiField(alias='Policies', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Find(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Find')

        def post(self, pattern: str, attribute_names: List[str] = None):
            body = {
                "Pattern"       : pattern,
                "AttributeNames": attribute_names
            }

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _FindContainers(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindContainers')

        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _FindObjectsOfClass(WebSdkEndpoint):
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

            class Response(WebSdkOutputModel):
                objects: List[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _FindPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/FindPolicy')

        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "Class"        : class_name,
                "AttributeName": attribute_name
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_dn: str = ApiField(alias='PolicyDN')
                values: List[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _GetHighestRevision(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetHighestRevision')

        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn,
                'Classes' : classes
            }

            class Response(WebSdkOutputModel):
                revision: int = ApiField(alias='Revision')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _GetRevision(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GetRevision')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(WebSdkOutputModel):
                revision: int = ApiField(alias='Revision')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _GuidToDn(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/GuidToDn')

        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            class Response(WebSdkOutputModel):
                object_dn: str = ApiField(alias='ObjectDN')
                class_name: str = ApiField(alias='ClassName')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _IdInfo(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IdInfo')

        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            class Response(WebSdkOutputModel):
                guid: str = ApiField(alias='GUID')
                class_name: str = ApiField(alias='ClassName')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _IsValid(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/IsValid')

        def post(self, object_dn: str = None, object_guid: str = None):
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN"  : object_dn
            }

            class Response(WebSdkOutputModel):
                object: config.Object = ApiField(alias='Object')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _MutateObject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/MutateObject')

        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class"   : class_name
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Read(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Read')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(WebSdkOutputModel):
                values: List[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ReadAll(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadAll')

        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Response(WebSdkOutputModel):
                name_values: List[config.NameValues[str]] = ApiField(alias='NameValues', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ReadDn(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDn')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(WebSdkOutputModel):
                values: List[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ReadDnReferences(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadDnReferences')

        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN"              : object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName"         : attribute_name
            }

            class Response(WebSdkOutputModel):
                values: List[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ReadEffectivePolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadEffectivePolicy')

        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Response(WebSdkOutputModel):
                values: List[str] = ApiField(alias='Values', default_factory=list)
                locked: bool = ApiField(alias='Locked')
                overridden: bool = ApiField(alias='Overridden')
                policy_dn: str = ApiField(alias='PolicyDN')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _ReadPolicy(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/ReadPolicy')

        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name
            }

            class Response(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                values: List[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _RemoveDnValue(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemoveDnValue')

        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Value"        : value
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _RemovePolicyValue(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RemovePolicyValue')

        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name,
                "Value"        : value
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _RenameObject(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/RenameObject')

        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN"   : object_dn,
                "NewObjectDN": new_object_dn
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _Write(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/Write')

        def post(self, object_dn: str, attribute_data: List[Dict[str, List[str]]]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeData": attribute_data
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _WriteDn(WebSdkEndpoint):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Config/WriteDn')

        def post(self, object_dn: str, attribute_name: str, values: List[str]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Values"       : values
            }

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)

    class _WritePolicy(WebSdkEndpoint):
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

            class Response(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), response_cls=Response)
