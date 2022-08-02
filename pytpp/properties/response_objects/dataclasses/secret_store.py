from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def secret_store_result(self) -> str:
        return ResultCodes.SecretStore.get(self.code, 'Unknown')


class TypedNameValues(PayloadModel):
    name: str = PayloadField(alias='Name')
    type: str = PayloadField(alias='Type')
    value: str = PayloadField(alias='Value')
