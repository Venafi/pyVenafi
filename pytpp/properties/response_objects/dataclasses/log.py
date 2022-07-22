from datetime import datetime
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class LogEvent(PayloadModel):
    client_timestamp: datetime = PayloadField(alias='ClientTimestamp', default=None)
    component: str = PayloadField(alias='Component', default=None)
    component_id: int = PayloadField(alias='ComponentId', default=None)
    component_subsystem: str = PayloadField(alias='ComponentSubsystem', default=None)
    data: str = PayloadField(alias='Data', default=None)
    grouping: int = PayloadField(alias='Grouping', default=None)
    id: int = PayloadField(alias='Id', default=None)
    name: str = PayloadField(alias='Name', default=None)
    server_timestamp: datetime = PayloadField(alias='ServerTimestamp', default=None)
    severity: str = PayloadField(alias='Severity', default=None)
    source_ip: str = PayloadField(alias='SourceIp', default=None)
    text1: str = PayloadField(alias='Text1', default=None)
    text2: str = PayloadField(alias='Text2', default=None)
    value1: int = PayloadField(alias='Value1', default=None)
    value2: int = PayloadField(alias='Value2', default=None)


class LogEventApplicationDefinition(PayloadModel):
    application_name: str = PayloadField(alias='ApplicationName', default=None)
    id: int = PayloadField(alias='Id', default=None)


class LogEventDefinition(PayloadModel):
    data_format: str = PayloadField(alias='DataFormat', default=None)
    data_title: str = PayloadField(alias='DataTitle', default=None)
    description: str = PayloadField(alias='Description', default=None)
    grouping_title: str = PayloadField(alias='GroupingTitle', default=None)
    grouping_type: str = PayloadField(alias='GroupingType', default=None)
    id: int = PayloadField(alias='Id', default=None)
    text1_title: str = PayloadField(alias='Text1Title', default=None)
    text2_title: str = PayloadField(alias='Text2Title', default=None)
    value1_title: str = PayloadField(alias='Value1Title', default=None)
    value1_type: str = PayloadField(alias='Value1Type', default=None)
    value2_title: str = PayloadField(alias='Value2Title', default=None)
    value2_type: str = PayloadField(alias='Value2Type', default=None)
