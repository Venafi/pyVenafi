class Log:
    class LogEvent:
        def __init__(self, log_event_dict: dict):
            if not isinstance(log_event_dict, dict):
                log_event_dict = {}

            self.client_timestamp = log_event_dict.get('ClientTimestamp')  # type: str
            self.component = log_event_dict.get('Component')  # type: str
            self.component_id = log_event_dict.get('ComponentId')  # type: int
            self.component_subsystem = log_event_dict.get('ComponentSubsystem')  # type: str
            self.data = log_event_dict.get('Data')  # type: str
            self.grouping = log_event_dict.get('Grouping')  # type: int
            self.id = log_event_dict.get('Id')  # type: int
            self.name = log_event_dict.get('Name')  # type: str
            self.server_timestamp = log_event_dict.get('ServerTimestamp')  # type: str
            self.severity = log_event_dict.get('Severity')  # type: str
            self.source_ip = log_event_dict.get('SourceIP')  # type: str
            self.text1 = log_event_dict.get('Text1')  # type: str
            self.text2 = log_event_dict.get('Text2')  # type: str
            self.value1 = log_event_dict.get('Value1')  # type: int
            self.value2 = log_event_dict.get('Value2')  # type: int

