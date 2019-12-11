class Log:
    class LogEvent:
        def __init__(self, log_event_dict: dict):
            if not isinstance(log_event_dict, dict):
                log_event_dict = {}

            self.client_timestamp = log_event_dict.get('ClientTimestamp')
            self.component = log_event_dict.get('Component')
            self.component_id = log_event_dict.get('ComponentId')
            self.component_subsystem = log_event_dict.get('ComponentSubsystem')
            self.data = log_event_dict.get('Data')
            self.grouping = log_event_dict.get('Grouping')
            self.id = log_event_dict.get('Id')
            self.name = log_event_dict.get('Name')
            self.server_timestamp = log_event_dict.get('ServerTimestamp')
            self.severity = log_event_dict.get('Severity')
            self.source_ip = log_event_dict.get('SourceIP')
            self.text1 = log_event_dict.get('Text1')
            self.text2 = log_event_dict.get('Text2')
            self.value1 = log_event_dict.get('Value1')
            self.value2 = log_event_dict.get('Value2')

