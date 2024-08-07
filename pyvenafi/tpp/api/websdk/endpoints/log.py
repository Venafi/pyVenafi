from __future__ import annotations

from pyvenafi.tpp.api.api_base import (
    ApiField,
    generate_output,
    WebSdkEndpoint,
    WebSdkOutputModel,
)
from pyvenafi.tpp.api.websdk.models import log

class _Log(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Log')
        self.LogSchema = self._LogSchema(api_obj=api_obj, url=f'{self._url}/LogSchema')
        self.EvaluateMacro = self._EvaluateMacro(api_obj=api_obj, url=f'{self._url}/EvaluateMacro')
        self.AdaptableInfo = self._AdaptableInfo(api_obj=api_obj, url=f'{self._url}/AdaptableInfo')

    def get(
        self, component: str = None, from_time: str = None, grouping: int = None, id: int = None,
        limit: int = None, offset: int = None, order: str = None, severity: str = None, text1: str = None,
        text2: str = None, to_time: str = None, value1: str = None, value2: str = None
    ):
        params = {
            'Component': component,
            'FromTime' : from_time,
            'Grouping' : grouping,
            'Id'       : id,
            'Limit'    : limit,
            'Offset'   : offset,
            'Order'    : order,
            'Severity' : severity,
            'Text1'    : text1,
            'Text2'    : text2,
            'ToTime'   : to_time,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Output(WebSdkOutputModel):
            log_events: list[log.LogEvent] = ApiField(default_factory=list, alias='LogEvents')

        return generate_output(output_cls=Output, response=self._get(params=params))

    def post(
        self, component: str, id: int, grouping: int = None, severity: int = None, source_ip: str = None,
        text1: str = None, text2: str = None, value1: str = None, value2: str = None
    ):
        body = {
            'Component': component,
            'ID'       : id,
            'Grouping' : grouping,
            'Severity' : severity,
            'SourceIp' : source_ip,
            'Text1'    : text1,
            'Text2'    : text2,
            'Value1'   : value1,
            'Value2'   : value2
        }

        class Output(WebSdkOutputModel):
            log_result: int = ApiField(alias='LogResult')

        return generate_output(output_cls=Output, response=self._post(data=body))

    def Guid(self, guid: str):
        return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

    class _Guid(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                log_events: list[log.LogEvent] = ApiField(default_factory=list, alias='LogEvents')

            return generate_output(output_cls=Output, response=self._get())

    class _LogSchema(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                log_event_application_definitions: list[log.LogEventApplicationDefinition] = ApiField(
                    alias='LogEventApplicationDefinitions'
                )
                log_event_definitions: list[log.LogEventDefinition] = ApiField(
                    alias='LogEventDefinitions',
                    default_factory=list
                )
                log_result: int = ApiField(alias='LogResult')

            return generate_output(output_cls=Output, response=self._get())

    class _AdaptableInfo(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                scripts: list[log.Script] = ApiField(alias='Scripts')
                script_errors: list[str] = ApiField(alias='ScriptErrors')

            return generate_output(output_cls=Output, response=self._get())

    class _EvaluateMacro(WebSdkEndpoint):
        def post(
            self,
            macro_source: str = None,
            id: int = None,
            severity: int = None,
            component: str = None,
            text_1: str = None,
            text_2: str = None,
            value_1: int = None,
            value_2: int = None,
        ):
            body = {
                "MacroSource": macro_source,
                "ID"         : id,
                "Severity"   : severity,
                "Component"  : component,
                "Text1"      : text_1,
                "Text2"      : text_2,
                "Value1"     : value_1,
                "Value2"     : value_2,
            }

            class Output(WebSdkOutputModel):
                macro_result: str = ApiField(alias='MacroResult')
                log_result: int = ApiField(alias='LogResult')

            return generate_output(output_cls=Output, response=self._post(data=body))
