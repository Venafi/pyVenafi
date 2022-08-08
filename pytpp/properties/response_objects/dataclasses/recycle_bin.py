from properties.resultcodes import ResultCodes
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField
from datetime import datetime
from typing import List, Literal


class Result(PayloadModel):
    code: int = PayloadField()

    @property
    def recycle_bin_result(self) -> str:
        return ResultCodes.RecycleBin.get(self.code, 'Unknown')

