from datetime import datetime
from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class LogEvent(PayloadModel):
    client_timestamp: datetime = PayloadField(alias='ClientTimestamp')
    component: str = PayloadField(alias='Component')
    component_id: int = PayloadField(alias='ComponentId')
    component_subsystem: str = PayloadField(alias='ComponentSubsystem')
    data: str = PayloadField(alias='Data')
    grouping: int = PayloadField(alias='Grouping')
    id: int = PayloadField(alias='Id')
    name: str = PayloadField(alias='Name')
    server_timestamp: datetime = PayloadField(alias='ServerTimestamp')
    severity: str = PayloadField(alias='Severity')
    source_ip: str = PayloadField(alias='SourceIp')
    text1: str = PayloadField(alias='Text1')
    text2: str = PayloadField(alias='Text2')
    value1: int = PayloadField(alias='Value1')
    value2: int = PayloadField(alias='Value2')


class LogEventApplicationDefinition(PayloadModel):
    application_name: str = PayloadField(alias='ApplicationName')
    id: int = PayloadField(alias='Id')


class LogEventDefinition(PayloadModel):
    data_format: str = PayloadField(alias='DataFormat')
    data_title: str = PayloadField(alias='DataTitle')
    data_type: str = PayloadField(alias='DataType')
    description: str = PayloadField(alias='Description')
    grouping_title: str = PayloadField(alias='GroupingTitle')
    grouping_type: str = PayloadField(alias='GroupingType')
    id: int = PayloadField(alias='Id')
    text1_title: str = PayloadField(alias='Text1Title')
    text2_title: str = PayloadField(alias='Text2Title')
    value1_title: str = PayloadField(alias='Value1Title')
    value1_type: str = PayloadField(alias='Value1Type')
    value2_title: str = PayloadField(alias='Value2Title')
    value2_type: str = PayloadField(alias='Value2Type')
