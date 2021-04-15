from pytpp.tools.helpers.date_converter import from_date_string


class Stats:
    class Counter:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.a_name = response_object.get('AName')  # type: str
            self.b_name = response_object.get('BName')  # type: str
            self.c_name = response_object.get('CName')  # type: str
            self.description = response_object.get('Description')  # type: str
            self.name = response_object.get('Name')  # type: str
            self.stats_type = response_object.get('StatsType')  # type: int

    class Result:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.key = Stats.Key(response_object.get('Key'))
            self.value = [Stats.Value(value) for value in response_object.get('Value')]

    class Key:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.m_item1 = response_object.get('m_Item1')  # type: str
            self.m_item2 = response_object.get('m_Item2')  # type: str
            self.m_item3 = response_object.get('m_Item3')  # type: str

    class Value:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.tag_a = response_object.get('TagA')  # type: str
            self.tag_b = response_object.get('TagB')  # type: str
            self.tag_c = response_object.get('TagC')  # type: str
            self.time_frame = from_date_string(response_object.get('TimeFrame'))
            self.type = response_object.get('Type')  # type: int
