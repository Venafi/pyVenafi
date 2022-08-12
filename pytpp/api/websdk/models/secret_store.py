from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField


class Result(OutputModel):
    code: int = ApiField()

    @property
    def secret_store_result(self) -> str:
        return ResultCodes.SecretStore.get(self.code, 'Unknown')


class TypedNameValues(OutputModel):
    name: str = ApiField(alias='Name')
    type: str = ApiField(alias='Type')
    value: str = ApiField(alias='Value')
