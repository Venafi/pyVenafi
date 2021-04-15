from pytpp.tools.helpers.date_converter import from_date_string


class Log:
    class LogEvent:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.client_timestamp = from_date_string(response_object.get('ClientTimestamp'))
            self.component = response_object.get('Component')  # type: str
            self.component_id = response_object.get('ComponentId')  # type: int
            self.component_subsystem = response_object.get('ComponentSubsystem')  # type: str
            self.data = response_object.get('Data')  # type: str
            self.grouping = response_object.get('Grouping')  # type: int
            self.id = response_object.get('Id')  # type: int
            self.name = response_object.get('Name')  # type: str
            self.server_timestamp = from_date_string(response_object.get('ServerTimestamp'))
            self.severity = response_object.get('Severity')  # type: str
            self.source_ip = response_object.get('SourceIP')  # type: str
            self.text1 = response_object.get('Text1')  # type: str
            self.text2 = response_object.get('Text2')  # type: str
            self.value1 = response_object.get('Value1')  # type: int
            self.value2 = response_object.get('Value2')  # type: int

    class LogEventApplicationDefinition:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.application_name = response_object.get('ApplicationName')  # type: str
            self.id = response_object.get('ID')  # type: int

    class LogEventDefinition:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.data_format = response_object.get('DataFormat')  # type: str
            self.data_title = response_object.get('DataTitle')  # type: str
            self.description = response_object.get('Description')  # type: str
            self.grouping_title = response_object.get('GroupingTitle')  # type: str
            self.grouping_type = response_object.get('GroupingType')  # type: str
            self.id = response_object.get('ID')  # type: int
            self.text1_title = response_object.get('Text1Title')  # type: str
            self.text2_title = response_object.get('Text2Title')  # type: str
            self.value1_title = response_object.get('Value1Title')  # type: str
            self.value1_type = response_object.get('Value1Type')  # type: str
            self.value2_title = response_object.get('Value2Title')  # type: str
            self.value2_type = response_object.get('Value2Type')  # type: str
