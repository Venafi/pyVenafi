from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)

class _Actions(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/actions')
        self.Codesign = self._Codesign(api_obj=api_obj, url=f'{self._url}/codesign')

    class _Codesign(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Prequalify = self._Prequalify(api_obj=self._api_obj, url=f'{self._url}/prequalify')

        class _Prequalify(WebSdkEndpoint):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.Create = self._Create(api_obj=self._api_obj, url=f'{self._url}/create')

            class _Create(WebSdkEndpoint):
                def post(self):
                    class Output(WebSdkOutputModel):
                        dn: str = ApiField(alias='Dn')
                        user: str = ApiField(alias='User')
                        comment: str = ApiField(alias='Comment')
                        data: str = ApiField(alias='Data')
                        single_use: bool = ApiField(alias='SingleUse')
                        ip_address: str = ApiField(alias='IPAddress')
                        signing_executable: str = ApiField(alias='SigningExecutable')
                        hours: int = ApiField(alias='Hours')

                    return generate_output(response=self._post(data={}), output_cls=Output)
