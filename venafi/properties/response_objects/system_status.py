from venafi.tools.helpers.date_converter import from_date_string


class SystemStatus:
    class Services:
        def __init__(self, serv_dict: dict):
            if not isinstance(serv_dict, dict):
                serv_dict = {}

            self.vplatform = SystemStatus.Service(serv_dict.get('vPlatform'))
            self.log_server = SystemStatus.Service(serv_dict.get('logServer'))
            self.iis = SystemStatus.Service(serv_dict.get('iis'))

    class Service:
        def __init__(self, vplat_dict: dict):
            if not isinstance(vplat_dict, dict):
                vplat_dict = {}

            self.modules = vplat_dict.get('modules')  # type: list
            self.time_since_first_seen = from_date_string(vplat_dict.get('timeSinceFirstSeen'))
            self.time_since_last_seen = from_date_string(vplat_dict.get('timeSinceLastSeen'))
            self.status = vplat_dict.get('Status')  # type: str
