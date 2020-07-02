from venafi.tools.helpers.date_converter import from_date_string


class Log:
    class LogEvent:
        def __init__(self, log_event_dict: dict):
            if not isinstance(log_event_dict, dict):
                log_event_dict = {}

            self.client_timestamp = from_date_string(log_event_dict.get('ClientTimestamp'))
            self.component = log_event_dict.get('Component')  # type: str
            self.component_id = log_event_dict.get('ComponentId')  # type: int
            self.component_subsystem = log_event_dict.get('ComponentSubsystem')  # type: str
            self.data = log_event_dict.get('Data')  # type: str
            self.grouping = log_event_dict.get('Grouping')  # type: int
            self.id = log_event_dict.get('Id')  # type: int
            self.name = log_event_dict.get('Name')  # type: str
            self.server_timestamp = from_date_string(log_event_dict.get('ServerTimestamp'))
            self.severity = log_event_dict.get('Severity')  # type: str
            self.source_ip = log_event_dict.get('SourceIP')  # type: str
            self.text1 = log_event_dict.get('Text1')  # type: str
            self.text2 = log_event_dict.get('Text2')  # type: str
            self.value1 = log_event_dict.get('Value1')  # type: int
            self.value2 = log_event_dict.get('Value2')  # type: int

    class LogEventApplicationDefinition:
        def __init__(self, log_event_app_def_dict: dict):
            if not isinstance(log_event_app_def_dict, dict):
                log_event_app_def_dict = {}

            self.application_name = log_event_app_def_dict.get('ApplicationName')  # type: str
            self.id = log_event_app_def_dict.get('ID')  # type: int

    class LogEventDefinition:
        def __init__(self, log_event_def_dict: dict):
            if not isinstance(log_event_def_dict, dict):
                log_event_def_dict = {}

            self.data_format = log_event_def_dict.get('DataFormat')  # type: str
            self.data_title = log_event_def_dict.get('DataTitle')  # type: str
            self.description = log_event_def_dict.get('Description')  # type: str
            self.grouping_title = log_event_def_dict.get('GroupingTitle')  # type: str
            self.grouping_type = log_event_def_dict.get('GroupingType')  # type: str
            self.id = log_event_def_dict.get('ID')  # type: int
            self.text1_title = log_event_def_dict.get('Text1Title')  # type: str
            self.text2_title = log_event_def_dict.get('Text2Title')  # type: str
            self.value1_title = log_event_def_dict.get('Value1Title')  # type: str
            self.value1_type = log_event_def_dict.get('Value1Type')  # type: str
            self.value2_title = log_event_def_dict.get('Value2Title')  # type: str
            self.value2_type = log_event_def_dict.get('Value2Type')  # type: str
