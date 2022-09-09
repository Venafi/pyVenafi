from venafi.tpp.api.api_base import generate_output, ApiField
from venafi.tpp.plugins.api.api_base import ApertureEndpoint, ApertureOutputModel
from venafi.tpp.plugins.api.aperture.models import config


class _ConfigObjects(ApertureEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/configobjects')
        self.Policies = self._Policies(api_obj=self._api_obj, url=f'{self._url}/policies')

    class _Policies(ApertureEndpoint):
        def post(self, name, container):
            body = {
                "DN": container + "\\" + name
            }

            class Output(ApertureOutputModel):
                object: config.Object = ApiField()

            return generate_output(output_cls=Output, response=self._post(data=body), root_field='object')
