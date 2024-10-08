from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import (
    config,
    identity as ident,
)

class _Config(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Config')
        self.AddDnValue = self._AddDnValue(api_obj=api_obj, url=f'{self._url}/AddDnValue')
        self.AddPolicyValue = self._AddPolicyValue(api_obj=api_obj, url=f'{self._url}/AddPolicyValue')
        self.AddValue = self._AddValue(api_obj=api_obj, url=f'{self._url}/AddValue')
        self.ClearAttribute = self._ClearAttribute(api_obj=api_obj, url=f'{self._url}/ClearAttribute')
        self.ClearPolicyAttribute = self._ClearPolicyAttribute(api_obj=api_obj, url=f'{self._url}/ClearPolicyAttribute')
        self.ContainableClasses = self._ContainableClasses(api_obj=api_obj, url=f'{self._url}/ContainableClasses')
        self.CountObjects = self._CountObjects(api_obj=api_obj, url=f'{self._url}/CountObjects')
        self.Create = self._Create(api_obj=api_obj, url=f'{self._url}/Create')
        self.DefaultDN = self._DefaultDN(api_obj=api_obj, url=f'{self._url}/DefaultDN')
        self.Delete = self._Delete(api_obj=api_obj, url=f'{self._url}/Delete')
        self.DnToGuid = self._DnToGuid(api_obj=api_obj, url=f'{self._url}/DnToGuid')
        self.Enumerate = self._Enumerate(api_obj=api_obj, url=f'{self._url}/Enumerate')
        self.EnumerateAll = self._EnumerateAll(api_obj=api_obj, url=f'{self._url}/EnumerateAll')
        self.EnumerateObjectsDerivedFrom = self._EnumerateObjectsDerivedFrom(
            api_obj=api_obj,
            url=f'{self._url}/EnumerateObjectsDerivedFrom'
        )
        self.EnumeratePolicies = self._EnumeratePolicies(api_obj=api_obj, url=f'{self._url}/EnumeratePolicies')
        self.Find = self._Find(api_obj=api_obj, url=f'{self._url}/Find')
        self.FindContainers = self._FindContainers(api_obj=api_obj, url=f'{self._url}/FindContainers')
        self.FindObjectsOfClass = self._FindObjectsOfClass(api_obj=api_obj, url=f'{self._url}/FindObjectsOfClass')
        self.FindPolicy = self._FindPolicy(api_obj=api_obj, url=f'{self._url}/FindPolicy')
        self.GetHighestRevision = self._GetHighestRevision(api_obj=api_obj, url=f'{self._url}/GetHighestRevision')
        self.GetObjectTrustees = self._GetObjectTrustees(api_obj=api_obj, url=f'{self._url}/GetObjectTrustees')
        self.GetRevision = self._GetRevision(api_obj=api_obj, url=f'{self._url}/GetRevision')
        self.GuidToDn = self._GuidToDn(api_obj=api_obj, url=f'{self._url}/GuidToDn')
        self.IdInfo = self._IdInfo(api_obj=api_obj, url=f'{self._url}/IdInfo')
        self.IsValid = self._IsValid(api_obj=api_obj, url=f'{self._url}/IsValid')
        self.MutateObject = self._MutateObject(api_obj=api_obj, url=f'{self._url}/MutateObject')
        self.Read = self._Read(api_obj=api_obj, url=f'{self._url}/Read')
        self.ReadAll = self._ReadAll(api_obj=api_obj, url=f'{self._url}/ReadAll')
        self.ReadDn = self._ReadDn(api_obj=api_obj, url=f'{self._url}/ReadDn')
        self.ReadDnReferences = self._ReadDnReferences(api_obj=api_obj, url=f'{self._url}/ReadDnReferences')
        self.ReadEffectivePolicy = self._ReadEffectivePolicy(api_obj=api_obj, url=f'{self._url}/ReadEffectivePolicy')
        self.ReadPolicy = self._ReadPolicy(api_obj=api_obj, url=f'{self._url}/ReadPolicy')
        self.RemoveDnValue = self._RemoveDnValue(api_obj=api_obj, url=f'{self._url}/RemoveDnValue')
        self.RemovePolicyValue = self._RemovePolicyValue(api_obj=api_obj, url=f'{self._url}/RemovePolicyValue')
        self.RemoveValue = self._RemoveValue(api_obj=api_obj, url=f'{self._url}/GetObjectTrustees')
        self.RenameObject = self._RenameObject(api_obj=api_obj, url=f'{self._url}/RenameObject')
        self.Write = self._Write(api_obj=api_obj, url=f'{self._url}/Write')
        self.WriteDn = self._WriteDn(api_obj=api_obj, url=f'{self._url}/WriteDn')
        self.WritePolicy = self._WritePolicy(api_obj=api_obj, url=f'{self._url}/WritePolicy')

    class _AddDnValue(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddPolicyValue(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str, locked: bool):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Class'        : class_name,
                'Value'        : value,
                'Locked'       : locked
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _AddValue(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name,
                'Value'        : value,
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ClearAttribute(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'AttributeName': attribute_name
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ClearPolicyAttribute(WebSdkEndpoint):
        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                'ObjectDN'     : object_dn,
                'Class'        : class_name,
                'AttributeName': attribute_name
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ContainableClasses(WebSdkEndpoint):
        def post(self, object_dn: str):
            body = {
                'ObjectDN': object_dn
            }

            class Output(WebSdkOutputModel):
                class_names: list[str] = ApiField(alias='ClassNames', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CountObjects(WebSdkEndpoint):
        def post(self, object_dn: str, type_name: str, recursive: bool = False, pattern: str = None):
            body = {
                'ObjectDN' : object_dn,
                'Type'     : type_name,
                'Pattern'  : pattern,
                'Recursive': recursive
            }

            class Output(WebSdkOutputModel):
                count: int = ApiField(alias='Count')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Create(WebSdkEndpoint):
        def post(self, object_dn: str, class_name: str, name_attribute_list: list[config.NameAttribute]):
            body = {
                "ObjectDN"         : object_dn,
                "Class"            : class_name,
                "NameAttributeList": name_attribute_list
            }

            class Output(WebSdkOutputModel):
                object: config.Object = ApiField(alias='Object')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DefaultDN(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                default_dn: str = ApiField(alias='DefaultDN')
                result: int = ApiField(alias='Result')

            return generate_output(response=self._get(), output_cls=Output)

    class _Delete(WebSdkEndpoint):
        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _DnToGuid(WebSdkEndpoint):
        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn,
            }

            class Output(WebSdkOutputModel):
                class_name: str = ApiField(alias='ClassName')
                guid: str = ApiField(alias='GUID')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Enumerate(WebSdkEndpoint):
        def post(self, object_dn: str = None, recursive: bool = False, pattern: str = None):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive,
                "Pattern"  : pattern
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateAll(WebSdkEndpoint):
        def post(self, pattern: str):
            body = {
                "Pattern": pattern
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumerateObjectsDerivedFrom(WebSdkEndpoint):
        def post(self, derived_from: str, pattern: str = None):
            body = {
                "DerivedFrom": derived_from,
                "Pattern"    : pattern
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _EnumeratePolicies(WebSdkEndpoint):
        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Output(WebSdkOutputModel):
                policies: list[config.Policy] = ApiField(alias='Policies', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Find(WebSdkEndpoint):
        def post(self, pattern: str, attribute_names: list[str] = None):
            body = {
                "Pattern"       : pattern,
                "AttributeNames": attribute_names
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _FindContainers(WebSdkEndpoint):
        def post(self, object_dn: str, recursive: bool = False):
            body = {
                "ObjectDN" : object_dn,
                "Recursive": recursive
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _FindObjectsOfClass(WebSdkEndpoint):
        def post(
            self, classes: str = None, class_name: str = None, object_dn: str = None, pattern: str = None,
            recursive: bool = False
        ):
            if not (classes or class_name):
                raise AssertionError('One of "classes" or "class_name" parameters must be provided.')
            body = {
                "Classes"  : classes,
                "Class"    : class_name,
                'ObjectDN' : object_dn,
                'Pattern'  : pattern,
                'Recursive': recursive
            }

            class Output(WebSdkOutputModel):
                objects: list[config.Object] = ApiField(alias='Objects', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _FindPolicy(WebSdkEndpoint):
        def post(self, object_dn: str, class_name: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "Class"        : class_name,
                "AttributeName": attribute_name
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_dn: str = ApiField(alias='PolicyDN')
                values: list[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetHighestRevision(WebSdkEndpoint):
        def post(self, object_dn: str, classes: str = None):
            body = {
                "ObjectDN": object_dn,
                'Classes' : classes
            }

            class Output(WebSdkOutputModel):
                revision: int = ApiField(alias='Revision')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetRevision(WebSdkEndpoint):
        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Output(WebSdkOutputModel):
                revision: int = ApiField(alias='Revision')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _GetObjectTrustees(WebSdkEndpoint):
        def post(
            self,
            recursive: bool = None,
            include_derived_classes: bool = None,
            locked: bool = None,
            pattern: str = None,
            object_pattern: str = None,
            derived_from: str = None,
            object_id: int = None,
            object_dn: str = None,
            type: str = None,
            new_object_dn: str = None,
            object_guid: str = None,
            classes: list[str] = None,
            className: str = None,
            attribute_name: str = None,
            attribute_names: list[str] = None,
            value: str = None,
            values: list[str] = None,
            attribute_data: dict[str, any] = None,
            reference_attribute_name: str = None,
            name_attribute_list: dict[str, any] = None,
        ):
            body = {
                "Recursive"             : recursive,
                "IncludeDerivedClasses" : include_derived_classes,
                "Locked"                : locked,
                "Pattern"               : pattern,
                "ObjectPattern"         : object_pattern,
                "DerivedFrom"           : derived_from,
                "ObjectID"              : object_id,
                "ObjectDN"              : object_dn,
                "Type"                  : type,
                "NewObjectDN"           : new_object_dn,
                "ObjectGUID"            : object_guid,
                "Classes"               : classes,
                "Class"                 : className,
                "AttributeName"         : attribute_name,
                "AttributeNames"        : attribute_names,
                "Value"                 : value,
                "Values"                : values,
                "AttributeData"         : attribute_data,
                "ReferenceAttributeName": reference_attribute_name,
                "NameAttributeList"     : name_attribute_list,
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))
                count: int = ApiField(alias='Count')
                object: config.Object = ApiField(alias='Object')
                objects: list[config.Object] = ApiField(alias='Objects')
                name_values: list[config.NameValues] = ApiField(alias='NameValues')
                class_definition: config.ClassDefinition = ApiField(alias='ClassDefinition')
                class_name: str = ApiField(alias='ClassName')
                class_names: list[str] = ApiField(alias='ClassNames')
                object_dn: str = ApiField(alias='ObjectDN')
                guid: str = ApiField(alias='GUID')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                class_definitions: list[config.ClassDefinition] = ApiField(alias='ClassDefinitions')
                attribute_definition: config.AttributeDefinition = ApiField(alias='AttributeDefinition')
                attribute_definitions: list[config.AttributeDefinition] = ApiField(alias='AttributeDefinitions')
                values: list[str] = ApiField(alias='Values')
                rights: int = ApiField(alias='Rights')
                policies: list[config.Policy] = ApiField(alias='Policies')
                policy_dn: str = ApiField(alias='PolicyDN')
                locked: bool = ApiField(alias='Locked')
                overridden: bool = ApiField(alias='Overridden')
                revision: int = ApiField(alias='Revision')
                identities: list[ident.Identity] = ApiField(alias='Identities')
                default_dn: str = ApiField(alias='DefaultDN')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GuidToDn(WebSdkEndpoint):
        def post(self, object_guid: str):
            body = {
                "ObjectGUID": object_guid
            }

            class Output(WebSdkOutputModel):
                object_dn: str = ApiField(alias='ObjectDN')
                class_name: str = ApiField(alias='ClassName')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _IdInfo(WebSdkEndpoint):
        def post(self, object_id: str):
            body = {
                "ObjectID": object_id
            }

            class Output(WebSdkOutputModel):
                guid: str = ApiField(alias='GUID')
                class_name: str = ApiField(alias='ClassName')
                revision: str = ApiField(alias='Revision')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _IsValid(WebSdkEndpoint):
        def post(self, object_dn: str = None, object_guid: str = None):
            body = {
                "ObjectGUID": object_guid,
                "ObjectDN"  : object_dn
            }

            class Output(WebSdkOutputModel):
                object: config.Object = ApiField(alias='Object')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _MutateObject(WebSdkEndpoint):
        def post(self, object_dn: str, class_name: str):
            body = {
                "ObjectDN": object_dn,
                "Class"   : class_name
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Read(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Output(WebSdkOutputModel):
                values: list[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ReadAll(WebSdkEndpoint):
        def post(self, object_dn: str):
            body = {
                "ObjectDN": object_dn
            }

            class Output(WebSdkOutputModel):
                name_values: list[config.NameValues[str]] = ApiField(alias='NameValues', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ReadDn(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Output(WebSdkOutputModel):
                values: list[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ReadDnReferences(WebSdkEndpoint):
        def post(self, object_dn: str, reference_attribute_name: str, attribute_name: str):
            body = {
                "ObjectDN"              : object_dn,
                "ReferenceAttributeName": reference_attribute_name,
                "AttributeName"         : attribute_name
            }

            class Output(WebSdkOutputModel):
                values: list[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ReadEffectivePolicy(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name
            }

            class Output(WebSdkOutputModel):
                values: list[str] = ApiField(alias='Values', default_factory=list)
                locked: bool = ApiField(alias='Locked')
                overridden: bool = ApiField(alias='Overridden')
                policy_dn: str = ApiField(alias='PolicyDN')
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _ReadPolicy(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, class_name: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                values: list[str] = ApiField(alias='Values', default_factory=list)
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveDnValue(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Value"        : value
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemovePolicyValue(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, class_name: str, value: str):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Class"        : class_name,
                "Value"        : value
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _RemoveValue(WebSdkEndpoint):
        def post(
            self,
            recursive: bool = None,
            include_derived_classes: bool = None,
            locked: bool = None,
            pattern: str = None,
            object_pattern: str = None,
            derived_from: str = None,
            object_id: int = None,
            object_dn: str = None,
            type: str = None,
            new_object_dn: str = None,
            object_guid: str = None,
            classes: list[str] = None,
            className: str = None,
            attribute_name: str = None,
            attribute_names: list[str] = None,
            value: str = None,
            values: list[str] = None,
            attribute_data: dict[str, any] = None,
            reference_attribute_name: str = None,
            name_attribute_list: dict[str, any] = None,
        ):
            body = {
                "Recursive"             : recursive,
                "IncludeDerivedClasses" : include_derived_classes,
                "Locked"                : locked,
                "Pattern"               : pattern,
                "ObjectPattern"         : object_pattern,
                "DerivedFrom"           : derived_from,
                "ObjectID"              : object_id,
                "ObjectDN"              : object_dn,
                "Type"                  : type,
                "NewObjectDN"           : new_object_dn,
                "ObjectGUID"            : object_guid,
                "Classes"               : classes,
                "Class"                 : className,
                "AttributeName"         : attribute_name,
                "AttributeNames"        : attribute_names,
                "Value"                 : value,
                "Values"                : values,
                "AttributeData"         : attribute_data,
                "ReferenceAttributeName": reference_attribute_name,
                "NameAttributeList"     : name_attribute_list,
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))
                count: int = ApiField(alias='Count')
                object: config.Object = ApiField(alias='Object')
                objects: list[config.Object] = ApiField(alias='Objects')
                name_values: list[config.NameValues] = ApiField(alias='NameValues')
                class_definition: config.ClassDefinition = ApiField(alias='ClassDefinition')
                class_name: str = ApiField(alias='ClassName')
                class_names: list[str] = ApiField(alias='ClassNames')
                object_dn: str = ApiField(alias='ObjectDN')
                guid: str = ApiField(alias='GUID')
                hierarchical_guid: str = ApiField(alias='HierarchicalGUID')
                class_definitions: list[config.ClassDefinition] = ApiField(alias='ClassDefinitions')
                attribute_definition: config.AttributeDefinition = ApiField(alias='AttributeDefinition')
                attribute_definitions: list[config.AttributeDefinition] = ApiField(alias='AttributeDefinitions')
                values: list[str] = ApiField(alias='Values')
                rights: int = ApiField(alias='Rights')
                policies: list[config.Policy] = ApiField(alias='Policies')
                policy_dn: str = ApiField(alias='PolicyDN')
                locked: bool = ApiField(alias='Locked')
                overridden: bool = ApiField(alias='Overridden')
                revision: int = ApiField(alias='Revision')
                identities: list[ident.Identity] = ApiField(alias='Identities')
                default_dn: str = ApiField(alias='DefaultDN')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RenameObject(WebSdkEndpoint):
        def post(self, object_dn: str, new_object_dn: str):
            body = {
                "ObjectDN"   : object_dn,
                "NewObjectDN": new_object_dn
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Write(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_data: list[dict[str, list[str]]]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeData": attribute_data
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _WriteDn(WebSdkEndpoint):
        def post(self, object_dn: str, attribute_name: str, values: list[str]):
            body = {
                "ObjectDN"     : object_dn,
                "AttributeName": attribute_name,
                "Values"       : values
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _WritePolicy(WebSdkEndpoint):
        def post(
            self,
            object_dn: str,
            class_name: str,
            attribute_name: str,
            locked: bool = False,
            values: list[str] = None
        ):
            body = {
                "ObjectDN"     : object_dn,
                "Class"        : class_name,
                "AttributeName": attribute_name,
                "Locked"       : locked,
                "Values"       : values
            }

            class Output(WebSdkOutputModel):
                result: config.Result = ApiField(alias='Result', converter=lambda x: config.Result(code=x))

            return generate_output(response=self._post(data=body), output_cls=Output)
