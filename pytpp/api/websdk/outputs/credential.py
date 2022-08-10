from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField
from typing import Literal

CredentialType = Literal[
    'Username and Password Credential',
    'Password Credential'
]


class Result(OutputModel):
    code: int = ApiField()

    @property
    def credential_result(self):
        return ResultCodes.Credential.get(self.code, 'Unknown')


class CredentialInfo(OutputModel):
    class_name: str = ApiField(alias='ClassName')
    full_name: str = ApiField(alias='FullName')


class NameTypeValue(OutputModel):
    name: str = ApiField(alias='Name')
    type: str = ApiField(alias='Type')
    value: str = ApiField(alias='Value')
