from pytpp.api.websdk.outputs.resultcodes import ResultCodes
from pytpp.api.api_base import OutputModel, ApiField


class Result(OutputModel):
    code: int = ApiField()

    @property
    def recycle_bin_result(self) -> str:
        return ResultCodes.RecycleBin.get(self.code, 'Unknown')
