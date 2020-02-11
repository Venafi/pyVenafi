from venafi.tools.helpers.date_converter import from_date_string


class Stats:
    class Counter:
        def __init__(self, counter_dict: dict):
            if not isinstance(counter_dict, dict):
                counter_dict = {}

            self.a_name = counter_dict.get('AName')  # type: str
            self.b_name = counter_dict.get('BName')  # type: str
            self.c_name = counter_dict.get('CName')  # type: str
            self.description = counter_dict.get('Description')  # type: str
            self.name = counter_dict.get('Name')  # type: str
            self.stats_type = counter_dict.get('StatsType')  # type: int

    class Result:
        def __init__(self, results_dict: dict):
            if not isinstance(results_dict, dict):
                results_dict = {}

            self.key = Stats.Key(results_dict.get('Key'))
            self.value = [Stats.Value(value) for value in results_dict.get('Value')]

    class Key:
        def __init__(self, key_dict: dict):
            if not isinstance(key_dict, dict):
                key_dict = {}

            self.m_item1 = key_dict.get('m_Item1')  # type: str
            self.m_item2 = key_dict.get('m_Item2')  # type: str
            self.m_item3 = key_dict.get('m_Item3')  # type: str

    class Value:
        def __init__(self, value_dict: dict):
            if not isinstance(value_dict, dict):
                value_dict = {}

            self.tag_a = value_dict.get('TagA')  # type: str
            self.tag_b = value_dict.get('TagB')  # type: str
            self.tag_c = value_dict.get('TagC')  # type: str
            self.time_frame = from_date_string(value_dict.get('TimeFrame'))
            self.type = value_dict.get('Type')  # type: int
