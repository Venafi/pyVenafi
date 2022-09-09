from datetime import datetime
from typing import List, Union
from uuid import UUID
from venafi.vaas.api.sdk.models import edge_management
from venafi.vaas.api.api_base import VaasSdkEndpoint, VaasSdkOutputModel, generate_output, ApiField


class _PairingCodes(VaasSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/v1/pairingcodes')

    def get(self):
        class Output(VaasSdkOutputModel):
            pairing_codes: List[edge_management.PairingCodeInformation] = ApiField(alias='pairingCodes')

        return generate_output(output_cls=Output, response=self._get())

    def post(self, environment_id: Union[UUID, str], expiration_date: datetime, reuse_count: int = None):
        body = {
            'environmentId': environment_id,
            'expirationDate': expiration_date,
            'reuseCount': reuse_count
        }

        class Output(VaasSdkOutputModel, edge_management.PairingCodeInformation):
            pass

        # This cannot be inherited as that method is broken. Instead, manually update the fields.
        Output.__fields__.update(edge_management.PairingCodeInformation.__fields__)

        return generate_output(output_cls=Output, response=self._post(data=body))
