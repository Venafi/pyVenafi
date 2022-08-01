from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField(default=None)

    @property
    def config_result(self):
        return ResultCodes.Credential.get(self.code, 'Unknown')


class CredentialInfo(PayloadModel):
    class_name: str = PayloadField(alias='ClassName')
    full_name: str = PayloadField(alias='FullName')


class NameTypeValue(PayloadModel):
    name: str = PayloadField(alias='Name')
    type: str = PayloadField(alias='Type')
    value: str = PayloadField(alias='Value')
